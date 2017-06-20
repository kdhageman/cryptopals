from util import file, crypto, convert
from challenges.decorator import challenge, expect

plaintext = file.read("set_1/challenge_5")
EXPECTED = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a2622632427276527" \
           "2a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"


@challenge(5)
def solve():
    key = b'ICE'

    encrypted = crypto.repeating_key(plaintext, key)

    expect(convert.to_hex(encrypted), EXPECTED)


if __name__ == "__main__":
    solve()
