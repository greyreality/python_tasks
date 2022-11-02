from maybe_on_interview.hexlet import solution2


def test_find():
    tree = [13, 10, 28, 6, 11, 21, 33]

    # assert solution.find([], 13) is None
    assert solution2.find(tree, 25) is None
    assert solution2.find(tree, 13) == 0
    assert solution2.find(tree, 28) == 2
    assert solution2.find(tree, 33) == 6

test_find()