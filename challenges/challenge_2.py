import util.xor as xor
import util.convert as convert


def solve():
    input_a = '1c0111001f010100061a024b53535009181c'
    input_b = '686974207468652062756c6c277320657965'
    expected = convert.from_hex('746865206b696420646f6e277420706c6179')

    a_bytes = convert.from_hex(input_a)
    b_bytes = convert.from_hex(input_b)

    actual = xor.bytes_xor(a_bytes, b_bytes)
    print(actual == expected)

if __name__ == "__main__":
    solve()

