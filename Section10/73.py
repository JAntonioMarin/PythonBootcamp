# pip3 install pylint
# pylint 73.py

# a = 1
# b = 1
# print(a)
# print(B)

# ************* Module 73
# 73.py:7:0: C0304: Final newline missing (missing-final-newline)
# 73.py:1:0: C0103: Module name "73" doesn't conform to snake_case naming style (invalid-name)
# 73.py:1:0: C0114: Missing module docstring (missing-module-docstring)
# 73.py:4:0: C0103: Constant name "a" doesn't conform to UPPER_CASE naming style (invalid-name)
# 73.py:5:0: C0103: Constant name "b" doesn't conform to UPPER_CASE naming style (invalid-name)
# 73.py:7:6: E0602: Undefined variable 'B' (undefined-variable)
#
# -------------------------------------
# Your code has been rated at -15.00/10
'''
A Very Simple Script
'''


def myfunc():
    '''
    A simple function
    :return:
    '''
    first = 1
    second = 2
    print(first)
    print(second)


myfunc()
