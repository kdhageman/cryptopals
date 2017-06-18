from util import parser, crypto, convert

key = crypto.randbytes(16)
uid = 10
role = 'user'


def solve():
    # create a cipher text block consisting of only "admin" (with trailing spaces which will be stripped)
    malicious_pt = " " * 10 + "admin" + " " * 11
    malicious_ct = profile_for(malicious_pt)[16:32]

    # create the base ciphertext, where the 'user' role is in block [32:48]
    base_pt = "f{}@bar.com".format("o" * 4)
    base_ct = profile_for(base_pt)[0:32]

    # replace the 'user' role with the 'admin' role
    pt = __decrypt(base_ct + malicious_ct)
    print(pt)


def profile_for(inp):
    inp = inp.split("&")[0].split("=")[0]
    pt = "email={}&uid=10&role=user".format(inp)
    return __encrypt(pt)


def __encrypt(pt):
    ct = crypto.aes_ecb_encrypt(str.encode(pt), key)
    return ct


def __decrypt(ct):
    pt = crypto.aes_ecb_decrypt(ct, key)
    pt = convert.to_string(pt)
    return parser.parse_kv(pt)


if __name__ == "__main__":
    solve()
