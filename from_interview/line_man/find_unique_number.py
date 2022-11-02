#!/Users/rita/venvs/py3/bin/python3
import random


def find_unique_numbers(x):
    print("List:", x)
    print("List length:", len(x))
    unique = set(x)
    print("Unique:", unique)
    print("Unique amount:", len(unique))
    return unique


if __name__ == '__main__':
    ax = [random.randint(-100, 100) for i in range(10)]
    ax.append(ax[2])
    ax.append(ax[6])
    print("Unique numbers are:", find_unique_numbers(ax))
