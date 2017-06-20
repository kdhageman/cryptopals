from util import file, crypto, convert
import numpy as np
from operator import itemgetter
from challenges.decorator import challenge, expect, contains

EXPECTED_KSIZE = 29
EXPECTED = [84, 101, 114, 109, 105, 110, 97, 116, 111, 114, 32, 88, 58, 32, 66,
            114, 105, 110, 103, 32, 116, 104, 101, 32, 110, 111, 105, 115, 101]


@challenge(6)
def solve():
    ct = convert.from_base64(file.read("set_1/challenge_6"))

    krange = range(2, 41)

    # compute best key size (lowest normalized hamming distances averaged over 3 attempts)
    ksizes = top_hdists(ct, krange, 3, 3)
    contains(EXPECTED_KSIZE, ksizes)

    # break plaintext into blocks
    blocks = crypto.in_blocks(ct, EXPECTED_KSIZE)

    # transpose
    blocks = transpose(blocks)

    # use single-byte XOR to find each byte of key
    key = []
    for block in blocks.values():
        i = crypto.sbxor(block)
        key.append(i[0])
    expect(key, EXPECTED)

    plaintext_bytes = crypto.repeating_key(ct, key)
    plaintext = convert.to_string(plaintext_bytes)
    print(plaintext)


def top_hdists(ct, krange, n, t):
    """
    Returns the best 'top' candidate key sizes for the provide ciphertext.
    The candidates are selected by comparing the hamming distances for all keys in krange.
    The algorithm averages over 'n' hamming distances.
    Computes the top normalized hamming distances for the provided ciphertext;
    :param t: the number of results to return
    :param ct: the plaintext for which the hamming distance is observed
    :param krange: the key size
    :param n: number of attempts of which the average is taken
    :return:
    """
    res = {}

    for ksize in krange:
        hdists = []

        offset = ksize
        prev = ct[0:ksize]

        for i in range(n):
            cur = ct[offset:offset + ksize]
            hdist = crypto.hdist(prev, cur)
            hdist_norm = hdist / ksize
            hdists.append(hdist_norm)
            offset += ksize
            prev = cur
        res[ksize] = np.mean(hdists)
    res = sorted(res.items(), key=itemgetter(1), reverse=False)
    return [i[0] for i in res[:t]]


def transpose(blocks):
    """
    Transposes a list of byte blocks
    :param blocks: the list of blocks being transposed
    :return: a list of byte blocks
    """
    res = {}
    for block in blocks:  # loop over all blocks
        for i in range(len(block)):  # loop over all bytes of block
            if i not in res:
                res[i] = []
            res[i].append(block[i])
    return res


if __name__ == "__main__":
    solve()
