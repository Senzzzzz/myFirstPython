from queue import Queue, Empty
# State the problem clearly. Identify the input & output formats.
# Come up with some example inputs & outputs. Try to cover all edge cases.
# Come up with a correct solution for the problem. State it in plain English.
# Implement the solution and test it using example inputs. Fix bugs, if any.
# Analyze the algorithm's complexity and identify inefficiencies, if any.
# Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# find midpoint, discord irrelevant numbers, check if midpoint is target number
# if not then midpoint becomes first of index
