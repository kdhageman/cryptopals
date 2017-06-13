from util import file, crypto, convert
import pprint
import numpy as np
from operator import itemgetter

pp = pprint.PrettyPrinter(indent=4)


def solve():
    ct = convert.from_base64(file.read("set_1/challenge_6"))

    krange = range(2, 41)

    # compute best key size (lowest normalized hamming distances averaged over 3 attempts)
    (ksize, hdist) = top_hdists(ct, krange, 3)
    ksize = 29

    # break plaintext into blocks
    blocks = crypto.in_blocks(ct, ksize)

    # transpose
    blocks = transpose(blocks)

    key = []

    for block in blocks.values():
        i = crypto.sbxor(block)
        key.append(i[0][0])

    pp.pprint(key)
    res_bytes = crypto.repeating_key(ct, key)
    res = convert.to_string(res_bytes)
    pp.pprint(res)


def top_hdists(plaintext, krange, attempts):
    """
    Computes the top normalized hamming distances for the provided plaintext;
    :param plaintext: the plaintext for which the hamming distance is observed
    :param krange: the key size
    :param attempts: number of attempts of which the average is taken
    :return:
    """
    res = {}

    for ksize in krange:
        hdists = []

        offset = ksize
        prev = plaintext[0:ksize]

        for i in range(attempts):
            cur = plaintext[offset:offset + ksize]
            hdist = crypto.hdist(prev, cur)
            hdist_norm = hdist / ksize
            hdists.append(hdist_norm)
            offset += ksize
            prev = cur
        res[ksize] = np.mean(hdists)
    res = sorted(res.items(), key=itemgetter(1), reverse=False)
    pp.pprint(res)
    return res[0]


def transpose(blocks):
    res = {}
    for block in blocks:  # loop over all blocks
        for i in range(len(block)):  # loop over all bytes of block
            if i not in res:
                res[i] = []
            res[i].append(block[i])
    return res


if __name__ == "__main__":
    solve()
