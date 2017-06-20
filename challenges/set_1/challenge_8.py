import pprint
from util import file, aes
from challenges.decorator import challenge, expect

CTS = file.read_lines("set_1/challenge_8")
EXPECTED = [b'd880619740a8a19b7840a8a31c810a3d08649af70dc06f4fd5d2d69c744cd283e2dd052f6b641dbf9d11b0348542bb5708649af70'
            b'dc06f4fd5d2d69c744cd2839475c9dfdbc1d46597949d9c7e82bf5a08649af70dc06f4fd5d2d69c744cd28397a93eab8d6aecd566'
            b'489154789a6b0308649af70dc06f4fd5d2d69c744cd283d403180c98c8f6db1f2a3f9c4040deb0ab51b29933f2c123c58386b06fb'
            b'a186a']


@challenge(8)
def solve():
    correct_cts = []
    for ct in CTS:
        if aes.is_encrypted(ct):
            correct_cts.append(ct)
    expect(correct_cts, EXPECTED)


if __name__ == "__main__":
    solve()
