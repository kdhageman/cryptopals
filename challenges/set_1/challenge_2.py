from util import crypto, convert
from challenges.decorator import challenge, expect

INPUT_A = "1c0111001f010100061a024b53535009181c"
INPUT_B = "686974207468652062756c6c277320657965"
EXPECTED = convert.from_hex('746865206b696420646f6e277420706c6179')


@challenge(2)
def solve():
    a_bytes = convert.from_hex(INPUT_A)
    b_bytes = convert.from_hex(INPUT_B)

    actual = crypto.bytes_xor(a_bytes, b_bytes)
    expect(actual, EXPECTED)


if __name__ == "__main__":
    solve()
