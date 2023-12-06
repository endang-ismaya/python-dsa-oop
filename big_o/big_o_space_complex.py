"""
Auxiliary Space Complexity

The memory an algorithm needs to run
without counting the memory needed to store the input

When creating new data inside an algorithm
we need to think about the auxiliary memory utilization

"""

"""
the function will only keep i one in a time
it is not saving the old values

Time complexity -> O(n)
Space complexity -> O(1)
"""


def func_one(array):  # [0, 1, 2, 3, 4, 5]
    for i in array:
        print(i)


"""
Time complexity -> O(n)
Space complexity -> O(n)
"""


def func_two(array):
    result = []
    for i in array:
        result.append(i * 2)
    return result
