from Crypto.Cipher import AES

import util.ascii as ascii


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
    res = b''
    for a in a:
        res += bytes([a ^ b])
    return res


def sbxor(ctext):
    """
    Compute the best single-byte XOR
    :param ctext:
    :return:
    """
    max_accept_vals = 0
    res = []
    for i in range(0, 2 ** 8):
        num_accept_vals = 0
        xor_res = byte_xor(ctext, i)
        for b in xor_res:
            if b in ascii.acceptable_values():
                num_accept_vals += 1
        # new potential winner
        if num_accept_vals > max_accept_vals:
            max_accept_vals = num_accept_vals
            res = []
            res.append((i, xor_res))
        # another potential winner
        elif num_accept_vals == max_accept_vals:
            res.append((i, xor_res))
    return res


def repeating_key(pt, key):
    res = []
    key_ctr = 0

    for b in pt:
        res.append(bytes([b ^ key[key_ctr % len(key)]]))
        key_ctr += 1
    return b''.join(res)


def hdist(a, b):
    """
    Computes the hamming distance between two byte arrays
    :param a:
    :param b:
    :return: the hamming distance, or -1 if the byte arrays are of unequal length
    """
    if len(a) != len(b):
        return -1

    res = 0
    for i in range(len(a)):  # loop over bytes
        for j in range(0, 8):
            if get_bit(a[i], j) != get_bit(b[i], j):
                res += 1
    return res


def get_bit(byte, n):
    """
    Returns the n-th bit of the provided byte (starting from the right)
    :param byte:
    :param n: 0-7
    :return:
    """
    return (byte >> n) % 2


def in_blocks(inp, ksize):
    """
    Break the plain text in blocks of size ksize
    :param inp:
    :param ksize:
    :return:
    """
    cur_index = 0
    res = []
    while cur_index + ksize <= len(inp):
        res.append(inp[cur_index:cur_index + ksize])
        cur_index += ksize
    return res


def pkcs7_padding(inp, length):
    """
    Applies PKCS#7 padding
    :param inp: the input being padded
    :param length:
    :return:
    """
    padding_length = length - (len(inp) % length)

    res = inp
    for i in range(padding_length):
        res += bytes([padding_length])

    return res


def aes_ecb_decrypt(ct, key):
    aes = AES.new(key, mode=AES.MODE_ECB)
    return aes.decrypt(ct)


def aes_ecb_encrypt(pt, key):
    aes = AES.new(key, mode=AES.MODE_ECB)
    return aes.encrypt(pt)


def aes_cbc_decrypt(ct, key, iv):
    """
    Decrypts the cipher text using AES' CBC mode
    :param ct: cipher text
    :param key: decryption key
    :param iv: initialization vector
    :return:
    """
    res = b''
    ct_blocks = in_blocks(ct, len(key))
    for ct_block in ct_blocks:
        bc_decrypted = aes_ecb_decrypt(ct_block, key)
        pt_block = bytes_xor(bc_decrypted, iv)
        iv = ct_block
        res += pt_block
    return res


def aes_cbc_encrypt(pt, key, iv):
    """
    Encrypts the plain text using AES' CBC mode
    :param pt: plain text
    :param key: encryption key
    :param iv: initialization vector
    :return:
    """
    res = b''
    pt_blocks = in_blocks(pt, len(key))
    for pt_block in pt_blocks:
        bc_in = bytes_xor(pt_block, iv)
        bc_out = aes_ecb_encrypt(bc_in, key)
        iv = bc_out
        res += bc_out
    return res
