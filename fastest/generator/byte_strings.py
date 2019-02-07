import random
import binascii


def gen_string(length=8):
    return '0b'+''.join([random.choice(['0', '1']) for _ in range(length)])
