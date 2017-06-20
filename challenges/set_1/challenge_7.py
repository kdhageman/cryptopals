from util import file, convert, aes
from challenges.decorator import challenge, expect

CT = convert.from_base64(file.read("set_1/challenge_7"))
EXPECTED = convert.from_base64(file.read("set_1/challenge_7_expected"))
KEY = "YELLOW SUBMARINE"


@challenge(7)
def solve():
    pt = aes.ecb_decrypt(CT, KEY)

    expect(pt, EXPECTED)

    print(convert.to_string(pt))


if __name__ == "__main__":
    solve()
