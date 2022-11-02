#!/Users/rita/venvs/py3/bin/python3
import random


def find_fifth_largest_number(x):
    # print(x)
    if len(x) > 100:
        return "ERROR:  size should not be larger than 100"
    if len(x) < 5:
        return "ERROR:  size should be 5 or more"
    for i in x:
        if type(i) is not int:
            return "ERROR:  it contains not an integer value"
    print(x)
    # get rid of duplicates
    x_to_set = set(x)
    x_to_list = list(x_to_set)
    x_to_list.sort()
    print(x_to_list)
    return x_to_list[4]


if __name__ == '__main__':
    ax = [random.randint(-100, 100) for i in range(100)]
    print("Positive test case for size=100. The fifth largest number is:", find_fifth_largest_number(ax))
    # ax = [random.randint(-100, 100) for i in range(99)]
    # print("Positive test case for size=99. The fifth largest number is:", find_fifth_largest_number(ax))
    # ax = [random.randint(-100, 100) for i in range(101)]
    # print("Negative test case for size=101. ", find_fifth_largest_number(ax))
    # ax = [random.randint(-100, 100) for i in range(4)]
    # print("Negative test case for size=4. ", find_fifth_largest_number(ax))
    # ax = [random.randint(-100, 100) for i in range(0)]
    # print("Negative test case for size=0. ", find_fifth_largest_number(ax))
    # ax = [random.randint(-100, 100) for i in range(4)]
    # ax.append(random.uniform(-100, 100))
    # print("Negative test case for not integer values. ", find_fifth_largest_number(ax))
    # ax = [random.uniform(-100, 100) for i in range(101)]
    # print("Negative test case for not integer values and size=101. ", find_fifth_largest_number(ax))
