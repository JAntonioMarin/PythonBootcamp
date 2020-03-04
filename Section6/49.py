def square(num):
    return num ** 2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)


def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]


names = ['Andy', 'Eve', 'Sally']

print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


mynums = [1, 2, 3, 4, 5, 6]

print(list(filter(check_even, mynums)))


def square(num):
    return num ** 2


print(square(3))

# lambda num: num ** 2
print(list(map(lambda num: num ** 2, mynums)))

print(list(filter(lambda num: num % 2 == 0, mynums)))

print(list(map(lambda name: name[::-1], names)))
