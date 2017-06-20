from util import pkcs7
from challenges.decorator import challenge, expect

PT = b"YELLOW SUBMARINE"
EXPECTED = b'YELLOW SUBMARINE\x04\x04\x04\x04'


@challenge(9)
def solve():
    actual = pkcs7.add(PT, 20)
    expect(actual, EXPECTED)


if __name__ == "__main__":
    solve()
