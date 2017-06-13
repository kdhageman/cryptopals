import util.file as file
import util.xor as xor
import util.convert as convert
import pprint


def solve():
    pp = pprint.PrettyPrinter(indent=4)

    plaintext = file.read("challenge_5")
    key = b'ICE'

    encrypted = xor.repeating_key(plaintext, key)
    pp.pprint(convert.shex_to_bytes(encrypted))

if __name__ == "__main__":
    solve()
