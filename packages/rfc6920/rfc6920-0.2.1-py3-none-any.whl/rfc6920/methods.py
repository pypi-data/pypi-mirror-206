#!/usr/bin/env python
# -*- coding: utf-8 -*-

# rfc6920, a library to generate and validate RFC6920 URIs
# Copyright (C) 2022-2023 Barcelona Supercomputing Center, José M. Fernández
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA

import genluhn

import base64
import hashlib
import urllib.parse

from typing import (
	cast,
	TYPE_CHECKING,
)

if TYPE_CHECKING:
	from typing import (
		Callable,
		IO,
		Iterable,
		Mapping,
		Optional,
		Sequence,
		Tuple,
		Union,
	)

	from typing_extensions import (
		Literal,
		TypedDict,
		NotRequired,
	)

	from genluhn import Digit

	class IndexedHashName(TypedDict):
		name: "str"
		algo: "str"
		trunc: "Optional[int]"
		instance: "NotRequired[hashlib._Hash]"


INDEXED_HASH_NAMES: "Sequence[Optional[IndexedHashName]]" = [
	None,  # Reserved
	{"name": "sha-256", "algo": "sha256", "trunc": None},
	{"name": "sha-256-128", "algo": "sha256", "trunc": 128},
	{"name": "sha-256-120", "algo": "sha256", "trunc": 120},
	{"name": "sha-256-96", "algo": "sha256", "trunc": 96},
	{"name": "sha-256-64", "algo": "sha256", "trunc": 64},
	{"name": "sha-256-32", "algo": "sha256", "trunc": 32},
]

NI_SCHEME = "ni"
NIH_SCHEME = "nih"

HASH_NAMES = {
	desc["name"]: desc
	for desc in cast(
		"Iterable[IndexedHashName]",
		filter(lambda desc: desc is not None, INDEXED_HASH_NAMES),
	)
}

STATIC_DEFAULT_BUFFER_SIZE = 65536


def compute_digest_from_filelike_and_callback(
	filelike: "IO[bytes]",
	h: "hashlib._Hash",
	bufferSize: "int" = STATIC_DEFAULT_BUFFER_SIZE,
	cback: "Optional[Callable[[bytes], None]]" = None,
) -> "bytes":
	"""
	Accessory method used to compute the digest of an input file-like object
	"""

	buf = filelike.read(bufferSize)
	while len(buf) > 0:
		h.update(buf)
		if cback:
			cback(buf)
		buf = filelike.read(bufferSize)

	return h.digest()


def _generate_ni_pre(
	filename: "Union[str, IO[bytes], bytes, bytearray]",
	algo: "Union[str, int, hashlib._Hash]" = "sha-256",
	trunc: "Optional[int]" = None,
) -> "Tuple[bytes, IndexedHashName]":
	"""
	The first parameter can be either the suite id (an integer)
	or an algorithm
	"""
	desc: "IndexedHashName"
	if isinstance(algo, str):
		# First, try matching by name
		gotdesc = HASH_NAMES.get(algo)

		if gotdesc is None:
			# Second, give a try later
			name = algo
			if trunc is not None:
				name += "-" + str(trunc)
			desc = {"name": name, "algo": algo, "trunc": trunc}
		elif (trunc is not None) and (desc.get("trunc") is None):
			# Overriding default value
			desc = gotdesc.copy()
			desc["trunc"] = trunc
			desc["name"] += "-{}".format(trunc)
	elif isinstance(algo, int):
		if algo < 1 or algo >= len(INDEXED_HASH_NAMES):
			raise ValueError(
				"Unrecognized or invalid RFC6920 suite id '{}'".format(algo)
			)

		gotdesc = INDEXED_HASH_NAMES[algo]
		assert gotdesc is not None
		desc = gotdesc
		if (trunc is not None) and (desc.get("trunc") is None):
			# Overriding default value
			desc = desc.copy()
			desc["trunc"] = trunc
			desc["name"] += "-{}".format(trunc)
	elif hasattr(algo, "digest_size"):
		desc = {
			"name": algo.name,
			"algo": algo.name,
			"trunc": algo.digest_size * 8,
			"instance": algo,
		}
	else:
		raise ValueError("Unsupported algo type of {}".format(type(algo)))

	# Now, prepare the instance
	instance = desc.get("instance")
	if instance is None:
		instance = hashlib.new(desc["algo"])

	if isinstance(filename, (bytes, bytearray)):
		instance.update(filename)
		digest = instance.digest()
	elif hasattr(filename, "seek"):
		# It is a file-like object
		digest = compute_digest_from_filelike_and_callback(
			cast("IO[bytes]", filename), instance
		)
	else:
		# Time to open file
		with open(filename, mode="rb") as f:
			digest = compute_digest_from_filelike_and_callback(f, instance)

	return digest, desc


def prettify_digest(digest: "Union[bytes, bytearray]") -> "str":
	pretty_digest = ""
	for ib, b in enumerate(digest):
		pretty_digest += ("-{:02x}" if ib > 0 and (ib & 1) == 0 else "{:02x}").format(b)

	return pretty_digest


def generate_nih_from_digest(
	digest: "Union[bytes, bytearray]",
	algo: "str" = "sha-256",
	trunc: "Optional[int]" = None,
) -> "str":
	# First, let's truncate to the bytes limit
	if trunc is not None:
		truncbytes = trunc // 8
		if len(digest) > truncbytes:
			digest = digest[:truncbytes]

	checkdigit = genluhn.compute(digest, 16)
	pretty_digest = prettify_digest(digest)

	return urllib.parse.urlunparse(
		(
			NIH_SCHEME,
			"",
			"{};{};{:x}".format(algo, pretty_digest, checkdigit),
			"",
			"",
			"",
		)
	)


def generate_nih(
	filename: "Union[str, IO[bytes], bytes, bytearray]",
	algo: "Union[str, int, hashlib._Hash]" = "sha-256",
	trunc: "Optional[int]" = None,
) -> "str":
	digest, desc = _generate_ni_pre(filename, algo, trunc)

	return generate_nih_from_digest(digest, desc["name"], desc["trunc"])


def generate_ni_from_digest(
	digest: "Union[bytes, bytearray]",
	algo: "str" = "sha-256",
	trunc: "Optional[int]" = None,
	authority: "str" = "",
) -> "str":
	# First, let's truncate to the bytes limit
	if trunc is not None:
		truncbytes = trunc // 8
		if len(digest) > truncbytes:
			digest = digest[:truncbytes]

	b64digest = base64.urlsafe_b64encode(digest).decode("utf-8")

	if authority:
		upat = "/{};{}"
	else:
		upat = "///{};{}"

	return urllib.parse.urlunparse(
		(NI_SCHEME, authority, upat.format(algo, b64digest), "", "", "")
	)


def generate_ni(
	filename: "Union[str, IO[bytes], bytes, bytearray]",
	algo: "Union[str, int, hashlib._Hash]" = "sha-256",
	trunc: "Optional[int]" = None,
) -> "str":
	digest, desc = _generate_ni_pre(filename, algo, trunc)

	return generate_ni_from_digest(digest, desc["name"], desc["trunc"])


def extract_digest(
	the_uri: "str",
) -> "Union[Tuple[None, None], Tuple[Union[Literal[False], bytes, bytearray], str]]":
	"""
	It extracts both the digest and the hashing algorithm from
	nih and ni URIs
	"""
	parsed = urllib.parse.urlparse(the_uri)
	if parsed.scheme not in (NI_SCHEME, NIH_SCHEME):
		return None, None

	lsemicolon = parsed.path.index(";")
	algo = parsed.path[0:lsemicolon]
	if algo[0] == "/":
		algo = algo[1:]
	encoded_digest = parsed.path[lsemicolon + 1 :]
	digest: "Optional[bytes]" = None
	# Obtaining the digest
	if parsed.scheme == NIH_SCHEME:
		checkdigit = None
		rsemicolon = encoded_digest.rfind(";")
		if ";" in encoded_digest:
			checkdigit = cast("Digit", int(encoded_digest[rsemicolon + 1], 16))
			hexdigest = encoded_digest[:rsemicolon]

			# Return false if the check digit validation fails
			if not genluhn.validate(hexdigest, 16, checkdigit):
				return False, algo
		else:
			hexdigest = encoded_digest

		digest = bytearray.fromhex(hexdigest.replace("-", ""))
	else:
		digest = base64.urlsafe_b64decode(encoded_digest)

	return digest, algo


def validate(
	the_uri: "str", filename: "Union[str, IO[bytes], bytes, bytearray]"
) -> "bool":
	digest, algo = extract_digest(the_uri)

	if digest is None or digest is False:
		return False

	assert algo is not None

	computed_digest, _ = _generate_ni_pre(filename, algo)

	# When the length of the computed digest is smaller, it is not
	# going to end well....
	if len(digest) > len(computed_digest):
		return False

	# Last, compare the common part
	return digest == computed_digest[: len(digest)]
