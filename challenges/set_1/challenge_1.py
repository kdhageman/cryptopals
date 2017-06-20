from util import convert
from challenges.decorator import challenge, expect

EXPECTED = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
INPUT = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'


@challenge(1)
def solve():
    raw = convert.from_hex(INPUT)
    actual = convert.to_base64(raw)

    expect(actual, EXPECTED)


if __name__ == "__main__":
    solve()
