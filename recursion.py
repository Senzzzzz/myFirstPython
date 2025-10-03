def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(linear_search(numbers, 5))


def binary_search(list, target):
    first = 0
    last = len(list) - 1
    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] > target:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return None


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        print(n)
        return n * factorial(n - 1)


def sum_n(n):
    if n == 0:
        return 0
    else:
        return n + sum_n(n - 1)


def n_to_one(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n_to_one(n - 1)


def reverse_string(string):
    if len(string) <= 1:
        return string
    else:
        print(string[1:])
        print(string[0])
        return reverse_string(string[1:]) + string[0]


def palindrome_checker(word):
    if len(word) <= 1:
        return True
    else:
        first = word[0]
        last = word[-1]

        if first != last:
            return False
    print(word)
    return palindrome_checker(word[1:-1])


print(palindrome_checker("racecar"))


def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        last = n % 10    # gets the LAST DIGIT
        last2 = n // 10  # gets the REMAINING NUMBER after removing last digit

        print(f"last: {last} last2:{last2}")
        return last + sum_of_digits(last2)


def num_of_digits(n):
    if n == 0:
        return 0
    else:
        last = n // 10  # 12345, 1234, 123, 12, 1
        print(last)
        return 1 + num_of_digits(last)
