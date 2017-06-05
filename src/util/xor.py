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

def repeating_key(pt, key):
    res = []
    key_ctr = 0

    for b in pt:
        res.append(bytes([b ^ key[key_ctr % len(key)]]))
        key_ctr += 1
    return b''.join(res)
