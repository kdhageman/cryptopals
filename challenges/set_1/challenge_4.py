from util import file, crypto, ascii, convert
from challenges.decorator import challenge, expect

INPUT = file.read_lines("set_1/challenge_4")
EXPECTED = b"Now that the party is jumping\n"


@challenge(4)
def solve():
    max_accept_vals = 0
    actual = []

    for i in range(len(INPUT)):
        for j in range(0, 2 ** 8):
            num_accept_vals = 0
            xor_res = crypto.byte_xor(convert.from_hex(INPUT[i]), j)
            for b in xor_res:
                if b in ascii.acceptable_values():
                    num_accept_vals += 1
            # new potential winner
            if num_accept_vals >= max_accept_vals:
                if num_accept_vals > max_accept_vals:
                    max_accept_vals = num_accept_vals
                    actual = []
                actual.append(xor_res)
    actual = actual[0]

    expect(actual, EXPECTED)


if __name__ == "__main__":
    solve()
