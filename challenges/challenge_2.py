import codecs
import util.xor as xor


def solve():
    input_a = '1c0111001f010100061a024b53535009181c'
    input_b = '686974207468652062756c6c277320657965'
    expected = codecs.decode('746865206b696420646f6e277420706c6179', 'hex')

    a_bytes = codecs.decode(input_a, 'hex')
    b_bytes = codecs.decode(input_b, 'hex')

    actual = xor.bytes_xor(a_bytes, b_bytes)
    print(actual == expected)

if __name__ == "__main__":
    solve()

