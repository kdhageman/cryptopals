from util import file, convert
from Crypto.Cipher import AES
import pprint

pp = pprint.PrettyPrinter(indent=4)


def solve():
    ct = convert.from_base64(file.read("challenge_7"))
    key = "YELLOW SUBMARINE"

    aes = AES.new(key, mode=AES.MODE_ECB)
    pt = aes.decrypt(ct)
    pp.pprint(pt)


if __name__ == "__main__":
    solve()
