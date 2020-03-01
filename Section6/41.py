def name_of_function():
    """
    Docstring explains funtion, this function only print Hello
    :return:
    """
    print("Hello")


def name_of_function2(name):
    """
    Docstring explains function, this function only print Hello
    :return:
    """
    print("Hello" + name)


def add_function(num1, num2):
    return num1 + num2


def name_function():
    '''
    DOCSTRING: Information about the function
    INPUT: no input
    OUTPUT: HELLO
    :return:
    '''
    print("Hello")


name_function()


# print(help(name_function))

def say_hello(name='NAME'):
    print('Hello ' + name)


say_hello()
say_hello('Juan')

result = say_hello('Zach')


def say_hello2(name='NAME'):
    return ('Hello ' + name)


result = say_hello2('Zach2')
print(result)


def add(n1, n2):
    return n1 + n2


result = add(20, 30)
print(result)

def dog_check(mystring):
    if 'dog' in mystring:
        return True
    else:
        return False

print(dog_check('My dog ran away'))
print(dog_check('My cat ran away'))

def dog_check2(mystring):
    return 'dog' in mystring.lower()

print(dog_check2('My dog ran away'))
print(dog_check2('My cat ran away'))

# PIGLATIN 'ay'

def pig_latin(word):
    first_letter = word[0]
    # check if vowel
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

print(pig_latin('apple'))
print(pig_latin('word'))