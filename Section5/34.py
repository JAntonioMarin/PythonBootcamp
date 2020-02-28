mylist = [1,2,3,4,5,6,7,8,9,10]

for num in mylist:
    print(num)

for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number {num}')

list_num = 0;
for num in mylist:
    list_num = list_num + num
print(list_num)

mystring = 'Hello World'
for letter in mystring:
    print(letter)

mystring = 'Pepe'
for _ in mystring:
    print('letter!')

mylist = [(1,2), (3,4), (5,6), (7,8)]
print(len(mylist))
for item in mylist:
    print(item)

mylist = [(1,2), (3,4), (5,6), (7,8)]
print(len(mylist))
for (a,b) in mylist:
    print(a)
    print(b)

mylist = [(1,2,3), (4,5,6), (7,8,9)]
for a,b,c in mylist:
    print(b)

d = {'k1':1, 'k2':2, 'k3':3}
for key,value in d.items():
    print(value)

for value in d.values():
    print(value)

