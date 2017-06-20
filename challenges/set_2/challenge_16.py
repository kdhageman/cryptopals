from util import crypto, aes, pkcs7, convert
from challenges.decorator import challenge, contains

IV = bytes([0]) * aes.S_BLOCK
KEY = crypto.randbytes(aes.S_BLOCK)


@challenge(16)
def solve():
    pt = " admin true"

    ct = encrypt(pt)
    for i in range(256):
        for j in range(256):
            new_ct = ct[0:16] + bytes([i]) + ct[17:22] + bytes([j]) + ct[23:]
            if contains_admin(new_ct):
                pt = aes.cbc_decrypt(new_ct, KEY, IV)
                contains(b';admin=true;', pt)
                print(pt)
                return
    print("Error: failed to find solution")


def encrypt(inp):
    """
    Encrypts the input after adding pre- and suffix
    :param key: encryption key
    :param inp: user date
    :return: encoded string
    """
    # prepare plaintext
    prefix = "comment1=cooking%20MCs;userdata="
    suffix = ";comment2=%20like%20a%20pound%20of%20bacon"
    pt = inp.replace(";", "").replace("=", "")  # remove invalid character
    pt = prefix + pt + suffix  # add prefix and suffix
    pt_encoded = pt.encode("utf-8")
    pt_padded = pkcs7.add(pt_encoded, aes.S_BLOCK)

    # encrypt
    ct = aes.cbc_encrypt(pt_padded, KEY, IV)

    return ct


def contains_admin(ct):
    """
    Returns whether the resulting plaintext contains an admin tuple (i.e ';admin=true;')
    :param ct: ciphertext
    :param key: decryption key
    :return: true if plaintext contains admin tuple; false otherwise
    """
    pt = aes.cbc_decrypt(ct, KEY, IV)
    return b";admin=true;" in pt


if __name__ == "__main__":
    solve()
