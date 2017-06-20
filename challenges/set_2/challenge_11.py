from util import crypto
from challenges.decorator import challenge, contains
from util.modes import Mode

EXPECTED = [Mode.ECB, Mode.CBC]


@challenge(11)
def solve():
    actual = crypto.detect_mode(crypto.encrypt_oracle)
    contains(actual, EXPECTED)

    print(actual)


if __name__ == "__main__":
    solve()
