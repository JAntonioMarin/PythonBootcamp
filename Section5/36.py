from random import shuffle
from random import randint

mylist = [1, 2, 3]

for num in range(0, 11, 2):
    print(num)

print(list(range(0, 11, 2)))

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

index_count = 0
word = 'abcde'
for letter in word:
    print(word[index_count])
    index_count += 1

word = 'abcde'
for index, letter in enumerate(word):
    print(index)
    print(letter)

mylist1 = [1,2,3]
mylist2= ['a','b','c']
mylist3 = [100,200,300]

for item in zip(mylist1, mylist2, mylist3):
    print(item)

print(list(zip(mylist1, mylist2)))

print('x' in ['x','y','z'])

print('mykey' in {'mykey':345})

mylist = [10,20,30,40,100]
print(min(mylist))
print(max(mylist))

mylist = [1,2,3,4,5,6,7,8,9,10]
shuffle(mylist)
print(mylist)

print(randint(0,100))

# num = input('Enter a number here: ')
# print(num)

# result = input('What is your name: ')
# print(f'Welcome {result}')

# num = int(input('Enter a number here: '))
# print(type(num))