from util import crypto, convert


def solve():
    inp = b'A'

    print(convert.to_hex(crypto.encryption_oracle(inp)))


if __name__ == "__main__":
    solve()
