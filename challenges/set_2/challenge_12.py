from exception.cryptoexception import CryptoException
from util import crypto, convert
from util.modes import Mode

BYTE = b'A'
NULL_BYTE = b''

def solve():
    crypto.set_global_key()
    try:
        bs = detect_block_size()
    except CryptoException as e:
        print(e.args[0])
        return

    if crypto.detect_mode(crypto.encrypt_oracle_consistent) != Mode.ECB:
        print("Error!")
        return

    unknown = get_unknown_string(bs)
    print(convert.to_string(unknown))


def get_unknown_string(bs):
    unknown = NULL_BYTE

    block_ctr = 0

    for k in range(40):
        offset = block_ctr * bs
        for j in range(16):
            base_pt = (BYTE * (bs - (j + 1)))
            base_key_pt = base_pt + unknown
            base_ct = crypto.encrypt_oracle_consistent(base_pt)

            ct_dict = {}
            for i in range(256):
                pt = base_key_pt + bytes([i])
                ct = crypto.encrypt_oracle_consistent(pt)
                ct_dict[ct[offset:offset + bs]] = i

            if base_ct[offset:offset + bs] not in ct_dict:
                return unknown
            unknown += bytes([ct_dict[base_ct[offset:offset + bs]]])
        block_ctr += 1


def detect_block_size():
    for i in range(1, 128):
        base_pt = BYTE * i
        pt = base_pt + BYTE
        base_ct = crypto.encrypt_oracle_consistent(base_pt)
        ct = crypto.encrypt_oracle_consistent(pt)
        if base_ct[0:i] == ct[0:i]:
            return i
    raise CryptoException("Failed to detect block size")

if __name__ == "__main__":
    solve()
