from util import crypto, file


def solve():
    ct_original = file.read("set_2/challenge_10")
    key = b"YELLOW SUBMARINE"
    iv = bytes(16)

    pt = crypto.aes_cbc_decrypt(ct_original, key, iv)
    ct_self = crypto.aes_cbc_encrypt(pt, key, iv)

    print(ct_original == ct_self)

if __name__ == "__main__":
    solve()
