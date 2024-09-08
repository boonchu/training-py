# https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
#
# Memoization effectively refers to remembering ("memoization" → "memorandum" → to be remembered)
# results of method calls based on the method inputs and then returning the remembered result
# rather than computing the result again.

# https://docs.python.org/3/library/functools.html#functools.wraps
# decorator with functools.wraps

from functools import wraps


def memoize(function):
    memo = {}

    @wraps(function)
    def wrapper(*args):

        # add the new key to dict if it doesn't exist already
        if args not in memo:
            memo[args] = function(*args)

        return memo[args]

    return wrapper


# https://zlliu.substack.com/i/147474066/wrapped-to-undecorate
# 7) __wrapped__ to undecorate


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    fibonacci(25)


if __name__ == "__main__":
    main()
