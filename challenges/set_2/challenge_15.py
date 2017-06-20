from exception.exceptions import PaddingException
from util import pkcs7, aes
from challenges.decorator import challenge, expect

EXPECTED = b"ICE ICE BABY"


@challenge(15)
def solve():
    inp = b"ICE ICE BABY\x04\x04\x04\x04"
    actual = pkcs7.remove(inp, aes.S_BLOCK)
    expect(actual, EXPECTED)

    try:
        inp = b"ICE ICE BABY\x05\x05\x05\x05"
        actual = pkcs7.remove(inp, aes.S_BLOCK)
    except PaddingException as e:
        expect(actual, actual)  # remains unchanged

    try:
        inp = b"ICE ICE BABY\x01\x02\x03\x04"
        actual = pkcs7.remove(inp, aes.S_BLOCK)
    except PaddingException as e:
        expect(actual, actual)  # remains unchanged


if __name__ == "__main__":
    solve()
