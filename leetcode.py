import string
import json
from queue import Queue, Empty
import math
# State the problem clearly. Identify the input & output formats.
# Come up with some example inputs & outputs. Try to cover all edge cases.
# Come up with a correct solution for the problem. State it in plain English.
# Implement the solution and test it using example inputs. Fix bugs, if any.
# Analyze the algorithm's complexity and identify inefficiencies, if any.
# Apply the right technique to overcome the inefficiency. Repeat steps 3 to 6.


# 2. Two sum - Easy
# Check if first index and the following indexs matches the target
# If not then first index increments by 1

def two_sum(nums, target):
    for first_index in range(len(nums)):
        for second_index in range(first_index + 1, len(nums)):
            # check if nums[first_index] + nums[second_index] == target
            if nums[first_index] + nums[second_index] == target:
                print(nums[first_index], nums[second_index])
                return first_index, second_index


nums = [2, 7, 11, 15, 1, 8]
target = 9
# print(two_sum(nums, target))

# 9. Palindrome number - Easy
# Initial thoughts: check if first and last numbers are the same


def palinedrome_number(x):
    if x < 0:
        return False
    length = math.floor(math.log10(abs(x))) + 1 if x != 0 else 1
    if length == 1 or length == 0:
        return True
    else:
        first = x // 10 ** (length - 1)
        last = x % 10

        if first != last:
            return False

    x = x // 10
    print(x)
    x = x % (10 ** (length - 2))
    print(x)
    length = math.floor(math.log10(x)) + 1 if x != 0 else 1

    if length <= 1:
        return True
    return palinedrome_number(x)

# Reverse the number and check if the reversed number is equal to x


def reverse(x):
    if x == 0:
        return True
    if x < 0:
        return False

    reversed_number = 0
    num = x

    while x != 0:
        last = x % 10  # Get last digit 3, 2, 1
        reversed_number = reversed_number * 10 + last  # Shift 3, then 2. then 1
        x = x // 10  # Removes last digit 123, 12, 1

    return num == reversed_number


# 13. Roman to Integer - Easy
# Initial thoughts: store numerals in a dictionary, check if each indivual character matches that of characters in the dictionary, then check 2 by 2 characters to account for outliers

numerals_table = {
    "M": 1000,
    "CM": 900,
    "D": 500,
    "CD": 400,
    "C": 100,
    "XC": 90,
    "L": 50,
    "XL": 40,
    "X": 10,
    "IX": 9,
    "V": 5,
    "IV": 4,
    "I": 1
}


def numerals_to_integer(numeral):
    i = 0
    total = 0
    # check 2 by 2 characters in input
    while i < len(numeral):
        if numeral[i:i+2] in numerals_table:
            total += numerals_table[numeral[i:i+2]]
            i += 2
        # check individual characters in input
        else:
            total += numerals_table[numeral[i].capitalize()]
            i += 1
    print(i)
    return total


# 27. Remove Element - Easy

def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):  # gets you the index and the value
        # if the value at index i is not equal to val, then we keep it
        # and increment k, which is the index of the next position to fill
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

# nums = [3, 2, 2, 3]
# val = 3

# 26. Remove Duplicates from Sorted Array - Easy


def remove_duplicates(nums):
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[k - 1]:
            print(f"nums[i]: {nums[i]}, nums[k]: {nums[k]}")
            nums[k] = nums[i]
            k += 1
    return k


# this code is saying if nums[i] is not equal to the previous number, then we keep it
# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# nums2 = [5, 2, 2, 4, 5, 3, 3]
# nums3 = [1, 2, 1, 2, 3, 4, 3, 5, 4, 6, 2, 1]
# print(remove_duplicates(nums3))

# 28. Find the Index of the First Occurrence in a String - Easy
##
haystack = "sadbutsad"
needle = "sad"


def find_first_occurrence(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1


# 88. Merge Sorted Array - Easy

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


def merge_sorted_array(nums1, m, nums2, n):

    # nums1[:] = sorted(nums1[:m] + nums2[:n]) faster and less code
    # Replace all elements inside nums1 with the elements from nums1 and nums2
    nums1[:] = nums1[:m] + nums2[:n]
    i = 0
    while i < len(nums1) - 1:
        if nums1[i] > nums1[i + 1]:
            nums1[i], nums1[i + 1] = nums1[i + 1], nums1[i]
            i = 0  # reset index to start
        else:
            i += 1  # move to next index
    return nums1


# 1768. Merge Strings Alternately - Easy

word1 = "abc"
word2 = "pqr"


def merge_strings_alternately(word1, word2):
    merged = []
    for i in range(max(len(word1), len(word2))):
        if i < len(word1):
            merged.append(word1[i])
        if i < len(word2):
            merged.append(word2[i])
    return "".join(merged)

# 1071. Greatest Common Divisor of Strings
# check if str1 + str2 is equal to str2 + str1
# if they are equal, then find the gcd of the lengths of str1 and str2
# else return an empty string


str1 = "ABCBCBC"
str2 = "BC"


def gcd_of_strings(str1, str2):
    if str1 + str2 == str2 + str1:
        gcd = math.gcd(len(str1), len(str2))
        return str1[:gcd]
    else:
        return ""

# print(gcd_of_strings(str1, str2))

# 1431. Kids With the Greatest Number of Candies - Easy


candies = [4, 2, 1, 1, 2]
extraCandies = 1


def kids_with_greatest_candies(candies, extraCandies):
    max_candies = max(candies)
    for n in range(len(candies)):
        if candies[n] + extraCandies >= max_candies:
            candies[n] = True
        else:
            candies[n] = False
    return candies


# print(kids_with_greatest_candies(candies, extraCandies))

# 605. Can Place Flowers - Easy
# Check left and right numbers to see if its empty, if it is plant

def can_place_flowers(flowerbed, n):
    if len(flowerbed) <= 1:
        return (n <= 1 and flowerbed[0] == 0) or (n == 0)

    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        n -= 1

    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
            flowerbed[i] = 1
            n -= 1

    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        n -= 1
    print(flowerbed)
    return n <= 0


flowerbed = [1]
n = 1

# print(can_place_flowers(flowerbed, n))

# 345. Reverse Vowels of a String - Easy


def reverse_vowels_in_string(s):
    i = 0
    k = len(s) - 1
    s = list(s)
    vowels = ["a", "e", "i", "o", "u"]
    while i < k:
        if s[i].lower() not in vowels:
            i += 1
        elif s[k].lower() not in vowels:
            k -= 1
        else:
            first = s[i]
            second = s[k]
            s[i] = second
            s[k] = first
            i += 1
            k -= 1
    return "".join(s)


str1 = "IceCreAm"  # I, e, e, A reversed = A, e, e, I

# print(reverse_vowels_in_string(str1))


# 151. Reverse Words in a String - Medium

words = "the sky is blue"


def reversed_words(s):
    words = s.split()
    new_words = []
    for i in range(len(words)):
        reversed = words.pop()
        new_words.append(reversed)
    return " ".join(new_words)


# print(reversed_words(words))

# 238. Product of Array Except Self - Medium
# ignoring each number in the loop, we want to multiply all the other numbers except i.
nums = [1, 2, 3, 4]


def productExceptSelf(nums):
    left_list = []
    n = 1
    for i in range(len(nums)):
        left_list.append(n)  # 1, 1, 2, 6
        n *= nums[i]

    right_list = []
    n2 = 1
    for j in reversed(range(len(nums))):
        right_list.append(n2)
        n2 *= nums[j]

    result = []
    right_list = right_list[::-1]  # 24, 12, 8, 6
    for k in range(len(nums)):
        result.append(left_list[k] * right_list[k])
    return result


# print(productExceptSelf(nums))


# 283. Move Zeroes - Easy

nums = [0, 1, 0, 3, 12]

position = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[position] = nums[i]
        position += 1
nums[position:] = [0] * (len(nums) - position)

# print(nums)


# 392. Is Subsequence - Easy

str1 = "axc"  # s
str2 = "ahbgdc"  # t


def is_subsequence(s, t):
    i = 0
    for char in range(len(t)):
        if i < len(s) and t[char] == s[i]:
            i += 1
    if s == "":
        return True
    if i == len(s):
        return True
    else:
        return False


# print(is_subsequence(str1, str2))

# 11. Container With Most Water - Medium

# area = biggest index - smallest index * lowest height  e.g 8 - 1 * 7 = 49

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def max_area(height):
    left = 0
    right = len(height) - 1
    result = []
    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = h * width
        result.append(area)
        print(area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max(result)


# print(max_area(height))

# 1679. Max Number of K-Sum Pairs - Medium

nums = [1, 2, 3, 4]
k = 5
nums.sort()

i = 0
j = len(nums) - 1

count = 0

while i < j:
    if nums[i] + nums[j] == k:
        count += 1
        i += 1
        j -= 1
    if nums[i] + nums[j] < k:
        i += 1
    elif nums[i] + nums[j] > k:
        j -= 1

# print(count)


# 643. Maximum Average Subarray I - Easy

nums = [1, 12, -5, -6, 50, 3]
k = 4


def find_max_average(nums, k):
    first_sum = sum(nums[:k])
    final_sum = first_sum
    for i in range(k, len(nums)):
        first_sum += nums[i] - nums[i-k]
        final_sum = max(first_sum, final_sum)

    return final_sum / k


# print(find_max_average(nums, k))


# 334. Increasing Triplet Subsequence - Mediu

nums = [20, 100, 10, 12, 5, 13]
nums2 = [1, 2, 3, 4, 5]
nums3 = [2, 4, -2, -3]
nums4 = [1, 2, 2147483647]
nums5 = [5, 1, 6]


def increasing_triple(nums):
    first = float("Inf")
    second = float("inf")
    for n in range(len(nums)):
        if nums[n] < first:
            first = nums[n]
        elif nums[n] > first and nums[n] < second:
            second = nums[n]
        if nums[n] > second:
            return True
    return False


print(increasing_triple(nums))
