from util import crypto


def solve():
    print(crypto.detect_mode(crypto.encrypt_oracle))


if __name__ == "__main__":
    solve()
