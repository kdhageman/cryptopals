from util import parser, crypto, convert

key = crypto.randbytes(16)
uid = 10
role = 'user'


def solve():
    pt = "{}@bar.com".format("a" * 5)
    ct = profile_for(pt)

    pt = __decrypt(ct)

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
