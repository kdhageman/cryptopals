from util import convert


def solve():
    input = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

    raw = convert.from_hex(input)
    actual = convert.to_base64(raw)

    print(actual == expected)


if __name__ == "__main__":
    solve()
