def find_missing(input):
    # Find a sum of elements of all the numbers in the array O(n)
    actual_sum = sum(input)
    # There is exactly 1 number missing
    n = len(input)
    # Find the expected sum of the first n numbers using (n(n+1))/2, a linear O(n)
    sum_of_elements = (n * (n + 1)) / 2
    # differences between total and sum is the missing number
    return int(sum_of_elements - actual_sum)


def main():
    v = [3, 7, 1, 2, 0, 4, 5]
    actual_missing = find_missing(v)
    print(f"Missing Number = {actual_missing}")

    v = [9, 6, 4, 2, 3, 5, 7, 0, 1]
    actual_missing = find_missing(v)
    print(f"Missing Number = {actual_missing}")


if __name__ == "__main__":
    main()
