from exception.exceptions import CryptoException, NotFoundException
from util import crypto, convert, file
from util.modes import Mode
from challenges.decorator import challenge, expect

BYTE = b'A'
NULL_BYTE = b''

EXPECTED = convert.from_base64(file.read("set_2/challenge_12_expected"))

@challenge(12)
def solve():
    crypto.set_global_key()  # set the global encryption key

    s_block = detect_s_block()  # find the block size of the cipher

    expect(crypto.detect_mode(crypto.encrypt_oracle_consistent_12), Mode.ECB) # validate that ECB mode is used

    unknown = get_unknown_string(s_block)  # retrieve the unknown string
    expect(unknown, EXPECTED)

    print(convert.to_string(unknown))


def get_unknown_string(s_block):
    """
    Returns the unknown string that is appended in the encrypt_oracle_consistent_12 function
    :param s_block: block size
    :return: the unknown string
    """
    unknown = NULL_BYTE

    block_ctr = 0

    for k in range(64):  # loop over (up to 64) blocks; answers is shorter but make sure that loop terminates
        offset = block_ctr * s_block
        for j in range(s_block):  # loop over each byte in the block
            incomplete_pt = (BYTE * (s_block - (j + 1)))
            incomplete_ct = crypto.encrypt_oracle_consistent_12(incomplete_pt)

            base_pt = incomplete_pt + unknown

            ct_dict = {}  # dictionary that holds every cipher text
            for i in range(256):  # create every possible cipher text for the full block
                pt = base_pt + bytes([i])
                ct = crypto.encrypt_oracle_consistent_12(pt)
                ct_dict[ct[offset:offset + s_block]] = i

            if incomplete_ct[
               offset:offset + s_block] not in ct_dict:  # cannot match any of the 256 possible bytes; end has been found
                return unknown
            unknown += bytes(
                [ct_dict[incomplete_ct[offset:offset + s_block]]])  # add found byte to the end of the unknown string
        block_ctr += 1
    raise NotFoundException("Failed to find unknown string")


def detect_s_block():
    """
    Detects the block size of the encrypt_oracle_consistent function
    :return:
    """
    for i in range(1, 128):
        base_pt = BYTE * i
        pt = base_pt + BYTE
        base_ct = crypto.encrypt_oracle_consistent_12(base_pt)
        ct = crypto.encrypt_oracle_consistent_12(pt)
        if base_ct[0:i] == ct[0:i]:
            return i
    raise CryptoException("Failed to detect block size")


if __name__ == "__main__":
    solve()
