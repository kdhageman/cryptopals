from util import ascii, file, convert
from util.modes import Mode
from util import aes
import random

global_key = b' ' * 16
global_prefix = b' ' * 8


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
    candidates = []
    for i in range(0, 2 ** 8):
        num_accept_vals = 0
        xor_res = byte_xor(ctext, i)
        for b in xor_res:
            if b in ascii.acceptable_values():
                num_accept_vals += 1
        # new candidate byte
        if num_accept_vals > max_accept_vals:
            max_accept_vals = num_accept_vals
            candidates = [i]
        # another candidate byte
        elif num_accept_vals == max_accept_vals:
            candidates.append(i)
    return candidates


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

    key = randbytes(aes.S_BLOCK)

    if random.randrange(2) == 1:  # CBC
        iv = randbytes(aes.S_BLOCK)
        res = aes.cbc_encrypt(inp, key, iv)
    else:  # ECB
        res = aes.ecb_encrypt(inp, key)
    return res


def encrypt_oracle_consistent_12(inp):
    """
    Implements a consistent encryption oracle (challenge 12)
    :param inp: plaintext to encrypt
    :return: ciphertext
    """
    append_bytes = convert.from_base64(file.read("set_2/challenge_12"))
    key = global_key
    return aes.ecb_encrypt(inp + append_bytes, key)


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

    second_block = ct[aes.S_BLOCK:aes.S_BLOCK * 2]
    third_block = ct[aes.S_BLOCK * 2:aes.S_BLOCK * 3]
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
    global_key = randbytes(aes.S_BLOCK)


def set_global_prefix():
    """
    Sets the global random prefix
    :return:
    """
    global global_prefix
    size = random.randrange(1, aes.S_BLOCK)
    global_prefix = randbytes(size)
