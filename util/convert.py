import codecs
import base64


def from_hex(input):
    return codecs.decode(input, 'hex')

def from_base64(input):
    return base64.b64decode(input)

def to_hex(input):
    return input.hex()