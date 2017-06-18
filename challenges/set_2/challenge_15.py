from util import crypto


def solve():
    s_block = 16
    inp = b'A' * 8

    inp_padded = crypto.add_padding(inp, s_block)

    outp = crypto.del_padding(inp_padded, s_block)
    print(outp)


if __name__ == "__main__":
    solve()
