import util.xor as xor
import util.convert as convert


def solve():
    input = convert.shex_to_bytes('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    res = xor.sbxor(input)
    print(res)

if __name__ == "__main__":
    solve()
