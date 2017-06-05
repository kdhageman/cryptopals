import util.file as file
import util.xor as xor
import pprint
import codecs


def solve():
    pp = pprint.PrettyPrinter(indent=4)

    plaintext = file.readfull("challenge_5")
    key = b'ICE'

    encrypted = xor.repeating_key(plaintext, key)
    pp.pprint(codecs.encode(encrypted, 'hex'))

if __name__ == "__main__":
    solve()
