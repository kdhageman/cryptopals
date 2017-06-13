import codecs


def shex_to_bytes(input):
    return codecs.decode(input, 'hex')
