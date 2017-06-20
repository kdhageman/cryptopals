from Crypto.Cipher import AES
from util import crypto, pkcs7

S_BLOCK = 16


def ecb_decrypt(ct, key):
    """
    Decrypts the cipher text using AES ECB mode
    :param ct: cipher text
    :param key: decryption key
    :return: plain text
    """
    aes = AES.new(key, mode=AES.MODE_ECB)
    return aes.decrypt(ct)


def ecb_encrypt(pt, key):
    """
    Encrypts the plain text using AES ECB mode
    :param pt: plain text
    :param key: encryption key
    :return: cipher text
    """
    aes = AES.new(key, mode=AES.MODE_ECB)
    return aes.encrypt(pkcs7.add(pt, S_BLOCK))


def cbc_decrypt(ct, key, iv):
    """
    Decrypts the cipher text using AES' CBC mode
    :param ct: cipher text
    :param key: decryption key
    :param iv: initialization vector
    :return: plain text
    """
    res = b''
    ct_blocks = crypto.in_blocks(ct, len(key))
    for ct_block in ct_blocks:
        bc_decrypted = ecb_decrypt(ct_block, key)
        pt_block = crypto.bytes_xor(bc_decrypted, iv)
        iv = ct_block
        res += pt_block
    return res


def cbc_encrypt(pt, key, iv):
    """
    Encrypts the plain text using AES' CBC mode
    :param pt: plain text
    :param key: encryption key
    :param iv: initialization vector
    :return:
    """
    res = b''
    pt_blocks = crypto.in_blocks(pt, len(key))
    for pt_block in pt_blocks:
        bc_in = crypto.bytes_xor(pt_block, iv)
        bc_out = ecb_encrypt(bc_in, key)
        iv = bc_out
        res += bc_out
    return res

def is_encrypted(ct):
    """
    Returns whether the provided ciphertext is encrypted with AES
    :param ct: ciphertext
    :return: true if ciphertext is encrypted with AES
    """
    res = False

    blocks = crypto.in_blocks(ct, 16)

    for block in blocks:
        counts = blocks.count(block)
        if counts > 1:
            res = True
            break
    return res
