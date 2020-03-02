def myfunc(a, b):
    return sum((a, b)) * 0.05


print(myfunc(40, 60))


def myfunc2(a, b, c=0, d=0):
    return sum((a, b, c, d)) * 0.05


print(myfunc2(40, 60, 100, 100))


def myfunc3(*args):
    return sum(args) * 0.05

print(myfunc3(40,60))
print(myfunc3(50,60,46,35,37,38,36,35,34))

def myfunc4(*args):
    for item in args:
        print(item)

print(myfunc4(50,60,46,35,37,38,36,35,34))

def myfunc5(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc5(fruit='apple', veggie= 'lettuce')

def myfunc6(*args, **kwargs):
    print ('I would like {} {}'.format(args[0],kwargs['food']))

myfunc6(10,20,30, fruit='orange', food='eggs', animal='dog')