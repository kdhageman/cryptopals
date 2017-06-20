from util import aes, file, convert
from challenges.decorator import challenge, expect

CT_ORIGINAL = convert.from_base64(file.read("set_2/challenge_10"))
EXPECTED = convert.from_base64(file.read("set_2/challenge_10_expected"))


@challenge(10)
def solve():
    key = b"YELLOW SUBMARINE"
    iv = bytes(16)

    pt = aes.cbc_decrypt(CT_ORIGINAL, key, iv)
    expect(pt, EXPECTED)

    print(convert.to_string(pt))


if __name__ == "__main__":
    solve()
