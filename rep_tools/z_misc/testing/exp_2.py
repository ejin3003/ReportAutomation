import timeit

"""
Sum the numbers from 0 to n-1 in different ways.
"""


def while_loop(n=100_000_000):
    i = 0
    s = 0
    while i < n:
        s += i
        i += 1
    return s


def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += i
    return s


def main():
    print('While Loop:\t\t', timeit.timeit(while_loop, number=1))
    print('For Loop:\t\t', timeit.timeit(for_loop, number=1))


if __name__ == '__main__':
    main()
