x = 25

def printer():
    x = 50
    return x

print(x)
print(printer())

yeah = lambda num:num**2
print(yeah(6))

#GLOBAL
name = 'THIS IS A GLOBAL STRING'

def greet():
    #ENCLOSING
    name = 'Sammy'

    def hello():
        name = 'IM A LOCAL' #LOCAL
        print('Hello '+name)

    hello()

greet()

x = 50
def func(x):
    print(f'X is {x}')

    # LOCAL REASSIGN;EMT
    x = 200
    print(f'I JUST LOCALLY CHANGED X TO {x}')

func(x)
print(x)

def func2():
    global x # no recommended
    print(f'X is {x}')

    # LOCAL REASSIGN;EMT
    x = 200
    print(f'I JUST CHANGED GLOBAL X TO NEW VALUE')

func2()
print(x)
