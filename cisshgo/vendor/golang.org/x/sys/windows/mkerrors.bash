#!/bin/bash

# Copyright 2019 The Go Authors. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

set -e
shopt -s nullglob

[[ $# -eq 1 ]] || { echo "Usage: $0 OUTPUT_FILE.go" >&2; exit 1; }
winerror="$(printf '%s\n' "/mnt/c/Program Files (x86)/Windows Kits/"/*/Include/*/shared/winerror.h | sort -Vr | head -n 1)"
[[ -n $winerror ]] || { echo "Unable to find winerror.h" >&2; exit 1; }

declare -A errors

{
	echo "// Code generated by 'go generate'; DO NOT EDIT."
	echo
	echo "package windows"
	echo "import \"syscall\""
	echo "const ("

	while read -r line; do
		unset vtype
		if [[ $line =~ ^#define\ +([A-Z0-9_]+k?)\ +([A-Z0-9_]+\()?([A-Z][A-Z0-9_]+k?)\)? ]]; then
			key="${BASH_REMATCH[1]}"
			value="${BASH_REMATCH[3]}"
		elif [[ $line =~ ^#define\ +([A-Z0-9_]+k?)\ +([A-Z0-9_]+\()?((0x)?[0-9A-Fa-f]+)L?\)? ]]; then
			key="${BASH_REMATCH[1]}"
			value="${BASH_REMATCH[3]}"
			vtype="${BASH_REMATCH[2]}"
		elif [[ $line =~ ^#define\ +([A-Z0-9_]+k?)\ +\(\(([A-Z]+)\)((0x)?[0-9A-Fa-f]+)L?\) ]]; then
			key="${BASH_REMATCH[1]}"
			value="${BASH_REMATCH[3]}"
			vtype="${BASH_REMATCH[2]}"
		else
			continue
		fi
		[[ -n $key && -n $value ]] || continue
		[[ -z ${errors["$key"]} ]] || continue
		errors["$key"]="$value"
		if [[ -v vtype ]]; then
			if [[ $key == FACILITY_* || $key == NO_ERROR ]]; then
				vtype=""
			elif [[ $vtype == *HANDLE* || $vtype == *HRESULT* ]]; then
				vtype="Handle"
			else
				vtype="syscall.Errno"
			fi
			last_vtype="$vtype"
		else
			vtype=""
			if [[ $last_vtype == Handle && $value == NO_ERROR ]]; then
				value="S_OK"
			elif [[ $last_vtype == syscall.Errno && $value == NO_ERROR ]]; then
				value="ERROR_SUCCESS"
			fi
		fi

		echo "$key $vtype = $value"
	done < "$winerror"

	echo ")"
} | gofmt > "$1"
