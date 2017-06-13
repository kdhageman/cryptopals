from util import crypto, file, convert


def solve():
    ct_original = convert.from_base64(file.read("set_2/challenge_10"))
    key = b"YELLOW SUBMARINE"
    iv = bytes(16)

    pt = crypto.aes_cbc_decrypt(ct_original, key, iv)
    print(convert.to_string(pt))

if __name__ == "__main__":
    solve()
