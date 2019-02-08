from binascii import Error


def env(raw_input):
    try:
        str(raw_input)
        return 1
    except UnicodeDecodeError:
        return -1
    except Error:
        return -1
