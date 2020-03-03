def old_macdonald(name):
    first_part = name[:3]
    second_half = name[3:]
    return first_part.capitalize() + second_half.capitalize()


# Check
print(old_macdonald('macdonald'))


def master_yoda(text):
    list_to_reverse = text.split(' ')
    list_to_reverse.reverse()
    return ' '.join(list_to_reverse)


# Check
print(master_yoda('I am home'))
print(master_yoda('We are ready'))


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


# Check
print(almost_there(104))
print(almost_there(150))
print(almost_there(209))
