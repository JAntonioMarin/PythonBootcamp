def has_33(nums):
    for num in range(0, len(nums) - 1):
        if (nums[num] == 3 and nums[num + 1] == 3):
            return True
    return False


# Check
print(has_33([1, 3, 3]))
print(has_33([1, 3, 1, 3]))
print(has_33([3, 1, 3]))


def paper_doll(text):
    result = ''
    for c in text:
        result = result + c * 3
    return result


# Check
print(paper_doll('Hello'))
print(paper_doll('Mississippi'))


def blackjack(a, b, c):
    sum_var = sum([a, b, c])
    if (sum_var <= 21):
        return sum_var
    elif (11 in [a, b, c] and sum_var - 10 <= 21):
        return sum_var - 10
    else:
        return 'BUST'


# Check
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))


def summer_69(arr):
    total = 0
    switch_69 = True
    for num in arr:
        if num != 6 and switch_69:
            total += num
        elif (not switch_69) and num == 9:
            switch_69 = True
        else:
            switch_69 = False
    return total


# Check
print(summer_69([1, 3, 5]))
print(summer_69([4, 5, 6, 7, 8, 9]))
print(summer_69([2, 1, 6, 9, 11]))
