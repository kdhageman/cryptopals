def bytes_xor(a, b):
    """
    Returns the XOR of two bytes objects
    :param a: first bytes
    :param b: second bytes
    :return: a XOR b
    """
    res = []
    for a, b in zip(a, b):
        res.append(bytes([a ^ b]))
    return b''.join(res)

def byte_xor(a, b):
    """
    Returns the XOR of one bytes and one byte object
    :param a: bytes
    :param b: byte
    :return:
    """
    res = []
    for a in a:
        res.append(bytes([a ^ b]))
    return b''.join(res)