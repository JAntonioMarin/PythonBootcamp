def vol(rad):
    return (4.0 / 3) * 3.14 * (rad ** 3)


# Check
print(vol(2))


def ran_check(num, low, high):
    if num in range(low, high):
        print(f'Number {num} is in the range {low}-{high}')
    else:
        print(f'Number {num} is outside the range {low}-{high}')


# Check
ran_check(5, 2, 7)


def ran_bool(num, low, high):
    return num in range(low, high)


# Check
print(ran_bool(3, 1, 10))


def up_low(s):
    count_upper = 0
    count_lower = 0
    print(f'Sample String: {s}')
    for char in s:
        if char.isupper():
            count_upper += 1
        elif char.islower():
            count_lower += 1
    print(f'No. of Upper case characters: {count_upper}')
    print(f'No. of Lower case characters: {count_lower}')


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
# Check
up_low(s)


def unique_list(lst):
    list_unique = []
    for i in lst:
        if i not in list_unique:
            list_unique.append(i)
    return list_unique


# Check
print(unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5]))


def multiply(numbers):
    total = numbers[0]
    for i in numbers:
        total *= i
    return total

# Check
print(multiply([1, 2, 3, -4]))


def palindrome(s):
    return s == s[::-1]


# Check
print(palindrome('helleh'))

import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    ispan = set(alphabet)
    return ispan <= set(str1.lower())


# Check
print(ispangram("The quick brown fox jumps over the lazy dog"))
