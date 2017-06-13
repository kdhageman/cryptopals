from util import crypto, convert


def solve():
    input = convert.from_hex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    res = crypto.sbxor(input)
    print(res)


if __name__ == "__main__":
    solve()
