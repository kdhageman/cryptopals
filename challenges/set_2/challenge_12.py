from util import crypto, convert
from util.modes import Mode


def solve():
    crypto.set_global_key()
    bs = detect_block_size()

    if crypto.detect_mode(crypto.encrypt_oracle_consistent) != Mode.ECB:
        print("Error!")
        return

    unknown = get_unknown_string(bs)
    print(convert.to_string(unknown))


def get_unknown_string(bs):
    unknown = b''

    block_ctr = 0

    for k in range(40):
        offset = block_ctr * bs
        for j in range(16):
            base_pt = (b'A' * (bs - (j + 1)))
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
    return 16

if __name__ == "__main__":
    solve()
