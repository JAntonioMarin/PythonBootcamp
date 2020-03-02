def myfunc(*args):
    mylist = []
    for item in args:
        if(item % 2 == 0):
            mylist.append(item)
    return mylist

print(myfunc(1,2,3,4,5,6,7,8,9,10))