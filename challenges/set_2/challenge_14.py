from util import crypto, convert
from exception.exceptions import NotFoundException

BYTE = b'A'
NULL_BYTE = b''


def solve():
    s_block = 16

    crypto.set_global_key()
    crypto.set_global_prefix()

    prefix_size = get_s_prefix(s_block)

    pt = get_unknown_string(prefix_size, s_block)
    print(convert.to_string(pt))


def get_s_prefix(s_block):
    """
    Retrieves the size of the current prefix of the 'encrypt_oracle_consistent_14' function
    :return: the prefix size
    """
    base_pattern = BYTE * s_block * 2

    for i in range(s_block):
        ct = crypto.encrypt_oracle_consistent_14((BYTE * i) + base_pattern)
        if ct[s_block:2 * s_block] == ct[2 * s_block:3 * s_block]:
            return s_block - i
    raise NotFoundException("Failed to find prefix length")


def get_unknown_string(s_prefix, s_block):
    """
    Returns the unknown string that is appended in the encrypt_oracle_consistent_14 function
    :param s_prefix: prefix size
    :param s_block: block size
    :return: the unknown string
    """
    counter_prefix = (s_block - s_prefix) * BYTE  # counters the size of the prefix in the cipher

    unknown = NULL_BYTE

    block_ctr = 0

    for k in range(64):  # loop over (up to 64) blocks; answers is shorter but make sure that loop terminates
        offset = (block_ctr * s_block) + s_block  # prefix + counter_prefix use exact one block size of space
        for j in range(s_block):  # loop over each byte in the block
            incomplete_pt = counter_prefix + (BYTE * (s_block - j - 1))
            incomplete_ct = crypto.encrypt_oracle_consistent_14(incomplete_pt)

            base_pt = incomplete_pt + unknown

            ct_dict = {}  # dictionary that holds every cipher text
            for i in range(256):  # create every possible cipher text for the full block
                pt = base_pt + bytes([i])
                ct = crypto.encrypt_oracle_consistent_14(pt)
                ct_dict[ct[offset:offset + s_block]] = i

            if incomplete_ct[offset:offset + s_block] not in ct_dict:  # cannot match any of the 256 possible bytes; end has been found
                return unknown
            unknown += bytes(
                [ct_dict[incomplete_ct[offset:offset + s_block]]])  # add found byte to the end of the unknown string
        block_ctr += 1
    raise NotFoundException("Failed to find unknown string")


if __name__ == "__main__":
    solve()
