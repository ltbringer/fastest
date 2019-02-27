import random


def random_integers(lower_limit=0, upper_limit=100):
    return random.randint(lower_limit, upper_limit)


def random_ascii_chars(max_char_len=1000):
    char_len = random_integers(lower_limit=0, upper_limit=max_char_len)
    return ''.join([chr(random_integers(0, 128)) for n in range(char_len)])


def random_float(lower_limit=0, upper_limit=100):
    return (random.random() * (upper_limit - lower_limit)) + lower_limit
