from util import file, crypto, convert
import pprint


def solve():
    pp = pprint.PrettyPrinter(indent=4)

    plaintext = file.read("challenge_5")
    key = b'ICE'

    encrypted = crypto.repeating_key(plaintext, key)
    pp.pprint(convert.to_hex(encrypted))


if __name__ == "__main__":
    solve()
