import pprint
from util import file, crypto

pp = pprint.PrettyPrinter(indent=4)


def solve():
    cts = file.read_lines("challenge_8")

    for ct in cts:
        if is_aes_encrypted(ct):
            pp.pprint("{} is AES encrypted".format(ct))


def is_aes_encrypted(ct):
    res = False

    blocks = crypto.in_blocks(ct, 16)

    for block in blocks:
        counts = blocks.count(block)
        if counts > 1:
            res = True
            break
    return res

if __name__ == "__main__":
    solve()

