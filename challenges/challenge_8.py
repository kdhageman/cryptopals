import pprint
import util.file as file

pp = pprint.PrettyPrinter(indent=4)

def solve():
    cts = file.read_lines("challenge_8")

    for ct in cts:
        if is_aes_encrypted(ct):
            pp.pprint("{} is AES encrypted".format(ct))

def break_in_blocks(plaintext, ksize):
    """
    Break the plain text in blocks of size ksize
    :param plaintext:
    :param ksize:
    :return:
    """
    cur_index = 0
    res = []
    while cur_index + ksize < len(plaintext):
        res.append(plaintext[cur_index:cur_index+ksize])
        cur_index += ksize
    return res

def is_aes_encrypted(ct):
    res = False

    blocks = break_in_blocks(ct, 16)

    for block in blocks:
        counts = blocks.count(block)
        if counts > 1:
            res = True
            break
    return res

if __name__ == "__main__":
    solve()

