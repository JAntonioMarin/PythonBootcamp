def myfunc(any_string):
    pos = 0
    return_string = ''
    for item in any_string:
        if((pos+1)%2 == 0):
            return_string = return_string + any_string[pos].upper()
        else:
            return_string = return_string + any_string[pos].lower()
        pos += 1
    return return_string


print(myfunc('Estos es aoisdjasdAD asd ASd as'))