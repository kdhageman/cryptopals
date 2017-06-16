from util import crypto


def solve():
    pt = b'0' * 64
    ct = crypto.encryption_oracle(pt)

    second_block = ct[16:32]
    third_block = ct[32:48]
    if second_block == third_block:
        print("ECB")
    else:
        print("CBC")


if __name__ == "__main__":
    solve()
