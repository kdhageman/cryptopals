from exception.exceptions import PaddingException


def add(inp, s_block):
    """
    Applies PKCS#7 padding
    :param inp: the input being padded
    :param s_block: block size
    :return:
    """
    if len(inp) % s_block == 0:
        return inp
    padding_length = s_block - (len(inp) % s_block)

    res = inp
    for i in range(padding_length):
        res += bytes([padding_length])

    return res


def remove(inp, s_block):
    """
    Removes the PKCS#7 padding, or raises exception if invalid padding
    :param inp: input whose padding is being removed
    :param s_block: the block size
    :return:
    """
    s_padding = inp[-1]

    if len(inp) % s_block != 0:
        raise PaddingException("Invalid PKCS#7 padding: input should be multiple of {}".format(s_block))

    if s_padding >= s_block:
        raise PaddingException("Invalid PKCS#7 padding: wrong size")

    padding = inp[-s_padding:]
    for p in padding:
        if p != s_padding:
            raise PaddingException("Invalid PKCS#7 padding: padding value not equal to size")
    return inp[:s_block - s_padding]