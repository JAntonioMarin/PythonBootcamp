x = 0

while x < 5:
    print(f'Tehe current value x is {x}')
    x += 1

x = [1, 2, 3]

for item in x:
    # pass is for work in progress
    pass

print('En of my script')

mystring = 'Sammy'

for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

for letter in mystring:
    if letter == 'a':
        break
    print(letter)

x = 0
while x < 5:
    if x == 2:
        break
    print(x)
    x += 1
