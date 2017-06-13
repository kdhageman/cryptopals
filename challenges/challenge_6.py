import util.file as file
import util.xor as xor
import pprint
import numpy as np
from operator import itemgetter


def solve():
    pp = pprint.PrettyPrinter(indent=4)

    plaintext = file.read("challenge_6")

    krange = range(2, 41)

    # compute best key size (lowest normalized hamming distances averaged over 3 attempts)
    (ksize, hdist) = top_hdists(plaintext, krange, 3)
    pp.pprint("{}: {}".format(ksize, hdist))

    # break plaintext into blocks
    blocks = break_in_blocks(plaintext, ksize)

    # transpose
    blocks = transpose(blocks)

    for block in blocks.values():
        pp.pprint(xor.sbxor(block))


def top_hdists(plaintext, krange, attempts):
    """
    Computes the top normalized hamming distances for the provided plaintext;
    :param plaintext:
    :param krange:
    :param attempts:
    :return:
    """
    res = {}

    for ksize in krange:
        hdists = []

        offset = ksize
        prev = plaintext[0:ksize]

        for i in range(attempts):
            cur = plaintext[offset:offset+ksize]
            hdist = xor.hdist(prev, cur)
            hdist_norm = hdist / ksize
            hdists.append(hdist_norm)
            offset += ksize
            prev = cur
        res[ksize] = np.mean(hdists)
    res = sorted(res.items(), key=itemgetter(1), reverse=False)
    return res[0]

def break_in_blocks(plaintext, ksize):
    """
    Break the plain text in blocks of size ksize
    :param plaintext:
    :param ksize:
    :return:
    """
    cur_index = 0
    res = []
    while cur_index + ksize < len(plaintext):
        res.append(plaintext[cur_index:cur_index+ksize])
        cur_index += ksize
    return res

def transpose(blocks):
    res = {}
    for block in blocks: # loop over all blocks
        for i in range(len(block)): # loop over all bytes of block
            if i not in res:
                res[i] = []
            res[i].append(block[i])
    return res

if __name__ == "__main__":
        solve()