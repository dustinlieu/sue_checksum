#!/usr/bin/env python3

import sys

def make_crc_table(polynomial):
	table = []

	for byte in range(256):
		crc = 0

		for bit in range(8):
			if (byte ^ crc) & 1:
				crc = (crc >> 1) ^ polynomial
			else:
				crc = crc >> 1

			byte = byte >> 1

		table.append(crc)

	return table

def calc_crc32(table, crc, data):
	inv_crc = ~crc & 0xFFFFFFFF

	for byte in data:
		inv_crc = table[(byte ^ inv_crc) & 0xFF] ^ (inv_crc >> 8);

	return ~inv_crc & 0xFFFFFFFF

if len(sys.argv) < 3:
	print("Not enough arguments")
	exit()

table = make_crc_table(0xC385B254)

# CRC A
crc_a = 0
input_file = open(sys.argv[1], "rb")
try:
	while True:
		chunk = input_file.read(32768)

		if len(chunk) == 0:
			break

		crc_a = calc_crc32(table, crc_a, chunk)
finally:
	input_file.close()

# CRC B
model = "DR590W1"
model_bytes = []

for c in model:
	model_bytes.append(ord(c))

crc_b = calc_crc32(table, crc_a, model_bytes)

# CRC C
byte_swapped_crc_b = [crc_b & 0xFF, (crc_b >> 8) & 0xFF, (crc_b >> 16) & 0xFF, (crc_b >> 24) & 0xFF]
crc_c = calc_crc32(table, crc_a, byte_swapped_crc_b)

# Output to file
output_file = open(sys.argv[2], "wb")
try:
	output_file.write(crc_a.to_bytes(4, byteorder="little"))
	output_file.write(crc_b.to_bytes(4, byteorder="little"))
	output_file.write(crc_c.to_bytes(4, byteorder="little"))
finally:
	output_file.close()
