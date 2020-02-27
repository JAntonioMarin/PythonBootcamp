myfile = open('myfile.txt')
print(myfile.read())
print(myfile.read())  # Only can read one time
myfile.close()
myfile = open('myfile.txt')
content = myfile.readlines()
print(content)
myfile.close()

with open('myfile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)
my_new_file.close()

with open('myfile.txt', mode='r') as myfile: # w:write a:append r+: reading and writing w+: writing and reading overwriting or creates a new file
    contents = myfile.read()

print(contents)

# with open('myfile.txt', mode='a') as f:
#     f.write('TEST NEW APPEND LINE')

# with open('new_create_file.txt', mode='w') as f:
#     f.write('I CREATED THIS FILE!')

