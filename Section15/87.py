from collections import Counter

list = [1,1,1,1,12,2,2,2,2,3,4,4,5,6,6,6]

print(Counter(list))

string ='asdihsdiuhsiughsdbadkjn'

print(Counter(string))

string_word = 'How many times does each word show up in this sentence word word shoe up up'

words = string_word.split()
c = Counter(words)

print(c)

print(c.most_common(3))

