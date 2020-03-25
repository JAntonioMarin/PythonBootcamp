# Problem 1

print(bin(1024))
print(hex(1024))

# Problem 2

print(round(2.23222, 2))

# Problem 3

s = 'hello how are you Mary, are you feeling okay?'

print('All charaters are lower?')
print(s.islower())

# Problem 4

s = 'toiwjtoiwoijtoiwjotwotjweoivfoijfwejroiw'

print(s.count('w'))

# Problem 5

set1 = {2, 3, 1, 5, 6, 8}
set2 = {3, 1, 7, 5, 6, 8}

print(set1.difference(set2))

# Problem 6

print(set1.union(set2))

# Problem 7

d = {'0': 0, '1': 1, '2': 8, '3': 27, '4': 64}
d2 = {x: x ** 3 for x in range(5)}
print(d)
print(d2)

# Problem 8

l = [1, 2, 3, 4]
l.reverse()
print(l)

# Problem 9

l = [3, 4, 2, 5, 1]
l.sort()
print(l)
