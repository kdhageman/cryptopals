from util import file, convert, crypto
import pprint

pp = pprint.PrettyPrinter(indent=4)


def solve():
    ct = convert.from_base64(file.read("set_1/challenge_7"))
    key = "YELLOW SUBMARINE"

    pt = crypto.aes_ecb_decrypt(ct, key)
    pp.pprint(pt)


if __name__ == "__main__":
    solve()
