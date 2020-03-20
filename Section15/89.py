from _collections import OrderedDict

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
d['e'] = 5

print(d)

for k, v in d.items():
    print(k, v)

dict = OrderedDict()
dict['a'] = 1
dict['d'] = 4
dict['e'] = 5
dict['b'] = 2
dict['c'] = 3

for k, v in dict.items():
    print(k, v)

if d == dict:
    print('Equals')
else:
    print('Different')

dict2 = OrderedDict()
dict2['a'] = 1
dict2['d'] = 4
dict2['b'] = 2
dict2['e'] = 5
dict2['c'] = 3

if dict2 == dict:
    print('Equals')
else:
    print('Different')
