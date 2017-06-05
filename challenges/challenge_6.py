import util.file as file
import util.xor as xor
import pprint
from collections import OrderedDict
from operator import itemgetter


def solve():
    pp = pprint.PrettyPrinter(indent=4)

    plaintext = file.read("challenge_6")
    krange = range(2, 41)

    # compute top 3 normalized hamming distances
    hdists = top_hdists(plaintext, krange, 3)
    pp.pprint(hdists)


def top_hdists(plaintext, krange, top):
    """
    Computes the top normalized hamming distances for the provided plaintext;
    :param plaintext:
    :param krange:
    :param top:
    :return:
    """
    res = {}

    for ksize in krange:
        first = plaintext[0:ksize]
        second = plaintext[ksize:ksize*2]
        hdist = xor.hdist(first, second)
        hdist_norm = hdist / ksize
        res[ksize] = hdist_norm
    res = sorted(res.items(), key=itemgetter(1), reverse=False)
    return OrderedDict(res[0:top])

if __name__ == "__main__":
        solve()