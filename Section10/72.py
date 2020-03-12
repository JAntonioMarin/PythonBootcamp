
try:
    for i in ['a','b','c']:
        print(i**2)
except TypeError:
    print("Type error!!")




try:
    x = 5
    y = 0
    z = x/y
except ZeroDivisionError:
    print("ZeroDivisionError!!")
finally:
    print("All Done!")



def ask():
    while True:
        try:
            number = int(input("Input an integer: "))
        except:
            print("An error occurred! Please try again!")
            continue
        else:
            break
    square = number ** 2
    print(f"Thank you, your number squared is:  {square}")

ask()




