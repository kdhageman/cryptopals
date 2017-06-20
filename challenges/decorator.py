challenges = {}


def challenge(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print("+------------" + ("-" * __numdigits(n)) + "-+")
            print("| Challenge {} |".format(n))
            print("+------------" + ("-" * __numdigits(n)) + "-+")
            print()
            f(*args, **kwargs)

        return wrapper

    return decorator


def expect(actual, expected):
    if actual != expected:
        print("Failed:")
        print("  Expected: {}".format(expected))
        print("  Actual:   {}".format(actual))
        return False
    return True


def __numdigits(n):
    ctr = 0
    while n > 1:
        n /= 10
        ctr += 1
    return ctr
