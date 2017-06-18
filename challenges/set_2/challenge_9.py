from util import crypto


def solve():
    pt = b"YELLOW SUBMARINE"
    result = crypto.add_padding(pt, 20)
    print(result)


if __name__ == "__main__":
    solve()
