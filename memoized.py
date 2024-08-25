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


@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    fibonacci(25)


if __name__ == "__main__":
    main()
