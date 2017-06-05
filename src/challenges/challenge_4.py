import util.file as file
import util.xor as xor
import util.ascii as ascii
import codecs
import pprint


def solve():
    a = file.read('challenge_4')

    max_accept_vals = 0
    accept = []

    pp = pprint.PrettyPrinter(indent=4)

    for i in range(len(a)):
        for j in range(0, 2**8):
            num_accept_vals = 0
            xor_res = xor.byte_xor(codecs.decode(a[i], 'hex'), j)
            for b in xor_res:
                if b in ascii.acceptable_values():
                    num_accept_vals += 1
            # new potential winner
            if num_accept_vals >= max_accept_vals:
                if num_accept_vals > max_accept_vals:
                    max_accept_vals = num_accept_vals
                    accept = []
                accept.append((i, j, xor_res))

    pp.pprint(accept) # Now that the party is jumping

if __name__ == "__main__":
    solve()
