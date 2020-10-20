
import doctest


def fizz_buzz(numbers):
    """
    Given a list of integers:
    1. Replace all integers that are evenly divisible by 3 with "fizz"
    2. Replace all integers divisible by 5 with "buzz"
    3. Replace all integers divisible by both 3 & 5 with "fizzbuzz"

    >>> numbers = [45, 22, 14, 65, 97, 72]
    >>> fizz_buzz(numbers)
    ['fizzbuzz', 22, 14, 'buzz', 97, 'fizz']
    """
    for i in range(len(numbers)):
        num = numbers[i]
        if num % 3 == 0:
            numbers[i] = "fizz"
        if num % 5 == 0:
            numbers[i] = "buzz"
        if num % 3 == 0 and num % 5 == 0:
            numbers[i] = "fizzbuzz"
    return numbers


# doctest.testmod(name="fizz_buzz", verbose=True)


def main():
    numbers = [100, 22, 14, 65, 97, 72]
    fizz_buzz(numbers)
    return numbers


print(main())


if __name__ == '__main__':
    doctest.testmod(name="fizz_buzz", verbose=True)
