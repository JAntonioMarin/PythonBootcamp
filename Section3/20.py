my_list = [1,2,3]
my_list = ['STRING', 100, 23.2]
print(len(my_list))
my_list = ['one', 'two', 'three']
print(my_list[0])
another_list = ['four', 'five']
print(my_list+another_list)
my_list[0] = 'ONE ALL CAPS'
print(my_list)
my_list.append('six')
print(my_list)
my_list.pop()
print(my_list)
popped_item = my_list.pop()
print(popped_item)
my_list.pop(0)
print(my_list)

new_list = ['a', 'e', 'x', 'b', 'c']
num_list = [4,1,8,3]
print(new_list.sort())
print(num_list.sort())
new_list_sorted = new_list
num_list_sorted = num_list
print(new_list_sorted)
print(num_list_sorted)
num_list.reverse()
print(num_list)