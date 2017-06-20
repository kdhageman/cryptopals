from util import parser, crypto, convert, aes
from challenges.decorator import challenge, expect, contains

KEY = crypto.randbytes(16)
UID = 10
ROLE = 'user'


@challenge(13)
def solve():
    # create a cipher text block consisting of only "admin" (with trailing spaces which will be stripped)
    malicious_pt = " " * 10 + "admin" + " " * 11
    malicious_ct = profile_for(malicious_pt)[16:32]

    # create the base ciphertext, where the 'user' role is in block [32:48]
    base_pt = "f{}@bar.com".format("o" * 4)
    base_ct = profile_for(base_pt)[0:32]

    # replace the 'user' role with the 'admin' role
    pt = __decrypt(base_ct + malicious_ct)
    contains('role', pt)
    expect(pt['role'].strip(), 'admin')

    print(pt)


def profile_for(inp):
    inp = inp.split("&")[0].split("=")[0]
    pt = "email={}&uid=10&role=user".format(inp)
    return __encrypt(pt)


def __encrypt(pt):
    ct = aes.ecb_encrypt(str.encode(pt), KEY)
    return ct


def __decrypt(ct):
    pt = aes.ecb_decrypt(ct, KEY)
    pt = convert.to_string(pt)
    return parser.parse_kv(pt)


if __name__ == "__main__":
    solve()
