from util import crypto, convert
from challenges.decorator import challenge, expect

INPUT = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
EXPECTED = 88


@challenge(3)
def solve():
    inp = convert.from_hex(INPUT)

    key = crypto.sbxor(inp)[0]
    expect(key, EXPECTED)

    res_bytes = crypto.byte_xor(inp, key)
    res = convert.to_string(res_bytes)
    print(res)

if __name__ == "__main__":
    solve()
