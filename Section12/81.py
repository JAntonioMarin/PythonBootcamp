def func():
    return 1


print(func())


def hello():
    return "Hello!"


print(hello())
print(hello)

greet = hello
print(greet())


# del hello

# print(hello())
#
# Traceback (most recent call last):
#   File "81.py", line 18, in <module>
#     print(hello())
# NameError: name 'hello' is not defined

def hello2(name='Josele'):
    print("The hello() function has been executed!")

    def greet():
        return '\t This is the greet() func inside hello!'

    def welcome():
        return "\t This is welcome() inside hello"

    if name == 'Jose':
        return greet
    else:
        return welcome

    # print(greet())
    # print(welcome())
    # print("This is the end of hello function!")


my_new_func = hello2('Jose')

print(my_new_func())


# hello2()
# welcome()
# NameError: name 'welcome' is not defined

def cool():
    def super_cool():
        return "I am very cool!"

    return super_cool


some_func = cool()
some_func()


def jelou():
    return "Hi Jose!"


def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())


other(jelou)


def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function")
        original_func()
        print("Some extra code, after the original function!")
    return wrap_func

def func_need_decorator():
    print("I want to be decorated!!")

decorated_func = new_decorator(func_need_decorator)

decorated_func()

@new_decorator
def func_need_decorator2():
    print("I want to be decorated!!")

func_need_decorator2()