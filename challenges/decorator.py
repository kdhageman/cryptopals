from time import time
from exception.exceptions import CompareException

challenges = {}


def challenge(n):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print("+" + ("-" * (12 + __numdigits(n))) + "+")
            print("| Challenge {} |".format(n))
            print("+" + ("-" * (12 + __numdigits(n))) + "+")
            print()
            t_begin = time()
            f(*args, **kwargs)
            passed = time() - t_begin
            print()
            print("Took {:.1f} ms".format(passed * 1000))

        challenges[n] = wrapper
        return wrapper

    return decorator


def expect(actual, expected):
    if actual != expected:
        msg = "Failed:\n"
        msg += "  Expected: {}\n".format(expected)
        msg += "  Actual:   {}".format(actual)
        raise CompareException(msg)


def contains(item, l):
    if item not in l:
        msg = "Failed:\n"
        msg += "  Expected: {}\n".format(l)
        msg += "  Actual:   {}".format(item)
        raise CompareException(msg)


def __numdigits(n):
    ctr = 0
    while n >= 1:
        n /= 10
        ctr += 1
    return ctr
