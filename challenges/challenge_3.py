import codecs
import util.xor as xor
import util.ascii as ascii


def solve():
    input = codecs.decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', 'hex')

    max_accept_vals = 0
    accept = []
    for i in range(0, 2**8):
        num_accept_vals = 0
        xor_res = xor.byte_xor(input, i)
        for b in xor_res:
            if b in ascii.acceptable_values():
                num_accept_vals += 1
        # new potential winner
        if num_accept_vals > max_accept_vals:
            max_accept_vals = num_accept_vals
            accept = []
            accept.append((i, xor_res))
        # another potential winner
        elif num_accept_vals == max_accept_vals:
            accept.append((i, xor_res))
    print(accept) # answer is 88: Cooking MC's like a pound of bacon

if __name__ == "__main__":
    solve()
