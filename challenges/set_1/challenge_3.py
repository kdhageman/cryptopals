from util import crypto, convert
from challenges.decorator import challenge, expect

INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
EXPECTED = b"Cooking MC's like a pound of bacon"


@challenge(3)
def solve():
    inp = convert.from_hex(INPUT)

    actual = crypto.sbxor(inp)[0]
    expect(actual, EXPECTED)


if __name__ == "__main__":
    solve()
