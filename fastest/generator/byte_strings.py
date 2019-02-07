import random
import binascii
import struct


def gen_bit_string(length=8):
    bitstring = ''.join([random.choice(['0', '1']) for _ in range(length)])
    return bitstring


def gen_raw_int(size=8):
    return int(gen_bit_string(size), 2)


def gen_raw_string(length=8):
    return binascii.unhexlify('%x' % gen_raw_int(length))


def int_to_bytes(n, byte_order='big'):
    return n.to_bytes(8, byte_order)


def gen_floats():
    return struct.unpack('>d', int_to_bytes(gen_raw_int()))[0]
