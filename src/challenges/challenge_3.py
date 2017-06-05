import codecs
import util.xor as xor

def solve():
    input = codecs.decode('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736', 'hex')

    for i in range(0, 2**8):
        print("{}: {}".format(i, xor.byte_xor(input, i)))
    # answer is 88: Cooking MC's like a pound of bacon

if __name__ == "__main__":
    solve()

