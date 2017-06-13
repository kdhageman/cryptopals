import codecs
import base64


def from_hex(input):
    return codecs.decode(input, 'hex')


def from_base64(input):
    return base64.b64decode(input)


def to_hex(input):
    return input.hex()


def to_base64(input):
    return codecs.encode(input, 'base64').strip()


def to_bit_string(input):
    """
    Converts a bytes object to a bit string
    :param input: a bytes object
    :return: the bit string representation
    """
    res = ""
    for i in input:
        binstr = bin(i)[2:]
        while len(binstr) < 8: # append zeroes to maintain 8 bit size
            binstr = "0"+binstr
        res += binstr
    return res


def to_string(input):
    """
    Converts a bytes object to a string
    e.g. to_string(b'abcd') == 'abcd'
    :param input: bytes object
    :return: string representation
    """
    return input.decode("utf-8")
