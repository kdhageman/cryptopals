from Crypto.Cipher import AES

from exception.exceptions import PaddingException
from util import ascii, file, convert
from util.modes import Mode
import random

global_key = b' ' * 16
global_prefix = b' ' * 8

s_block = 16


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
    while cur_index < len(inp):
        last_index = min(cur_index + ksize, len(inp))
        res.append(inp[cur_index:last_index])
        cur_index += ksize
    return res


def add_padding(inp, s_block):
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


def del_padding(inp, s_block):
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


def aes_ecb_decrypt(ct, key):
    """
    Decrypts the cipher text using AES ECB mode
    :param ct: cipher text
    :param key: decryption key
    :return: plain text
    """
    aes = AES.new(key, mode=AES.MODE_ECB)
    return aes.decrypt(ct).strip()


def aes_ecb_encrypt(pt, key):
    """
    Encrypts the plain text using AES ECB mode
    :param pt: plain text
    :param key: encryption key
    :return: cipher text
    """
    aes = AES.new(key, mode=AES.MODE_ECB)
    return aes.encrypt(add_padding(pt, s_block))


def aes_cbc_decrypt(ct, key, iv):
    """
    Decrypts the cipher text using AES' CBC mode
    :param ct: cipher text
    :param key: decryption key
    :param iv: initialization vector
    :return: plain text
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


def randbytes(size):
    """
    Creates random bytes of size
    :param size: size of the returned bytes object
    """
    res = b''
    for i in range(size):
        rand_byte = random.randrange(256)
        res += bytes([rand_byte])
    return res


def encrypt_oracle(inp):
    """
    Implements a random encryption oracle (challenge 11);
    :param inp: plaintext to encrypt
    :return: ciphertext
    """
    prepend_size = random.randrange(5, 10)
    append_size = random.randrange(5, 10)
    inp = randbytes(prepend_size) + inp + randbytes(append_size)

    key = randbytes(s_block)

    if random.randrange(2) == 1:  # CBC
        iv = randbytes(s_block)
        res = aes_cbc_encrypt(inp, key, iv)
    else:  # ECB
        res = aes_ecb_encrypt(inp, key)
    return res


def encrypt_oracle_consistent_12(inp):
    """
    Implements a consistent encryption oracle (challenge 12)
    :param inp: plaintext to encrypt
    :return: ciphertext
    """
    append_bytes = convert.from_base64(file.read("set_2/challenge_12"))
    key = global_key
    return aes_ecb_encrypt(inp + append_bytes, key)


def encrypt_oracle_consistent_14(inp):
    """
    Implements a consistent encryption oracle with random prefix (challenge 14)
    :param inp: plaintext to encrypt
    :return: ciphertext
    """
    return encrypt_oracle_consistent_12(global_prefix + inp)


def detect_mode(func):
    """
    Detects the encryption mode of the provided function
    :param func: Mode.ECB or Mode.CBC
    :return:
    """
    pt = b'0' * 64
    ct = func(pt)

    second_block = ct[s_block:s_block * 2]
    third_block = ct[s_block * 2:s_block * 3]
    if second_block == third_block:
        return Mode.ECB
    else:
        return Mode.CBC


##########################################
# -------- SET GLOBAL VARIABLES -------- #
##########################################
def set_global_key():
    """
    Sets the global encryption key
    :return:
    """
    global global_key
    global_key = randbytes(s_block)


def set_global_prefix():
    """
    Sets the global random prefix
    :return:
    """
    global global_prefix
    size = random.randrange(1, s_block)
    global_prefix = randbytes(size)
