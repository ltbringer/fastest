import random
import binascii
import struct


def gen_bit_string(length=8):
    """
    :param length: int
    :return: str
    """
    return ''.join([random.choice(['0', '1']) for _ in range(length)])


def gen_raw_int(size=8):
    """
    :param size: int
    :return: int
    """
    return int(gen_bit_string(size), 2)


def gen_raw_string(length=8):
    """
    :param length: int
    :return: str
    """
    return binascii.unhexlify('%x' % gen_raw_int(length))


def int_to_bytes(n, byte_order='big'):
    """
    :param n: int
    :param byte_order: str
    :return: str
    """
    return n.to_bytes(8, byte_order)


def gen_floats():
    """
    :return: float
    """
    return struct.unpack('>d', int_to_bytes(gen_raw_int()))[0]
