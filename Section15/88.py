from collections import defaultdict

# d = {'k1': 1}
#
# print(d['k1'])

dicti = defaultdict(object)
dicti['one']

for item in dicti:
    print(item)

out = defaultdict(lambda: 0)
out['one']

for item in out:
    print(item)

out['two'] = 2

print(out)