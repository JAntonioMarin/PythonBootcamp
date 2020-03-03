def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


# Check
print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 5))

def animal_crackers(text):
    list = text.split(' ')
    return list[0][0].lower() == list[1][0].lower()

# Check
print(animal_crackers('Levelheaded Llama'))
print(animal_crackers('Crazy Kangaroo'))


def makes_twenty(n1,n2):
    return n1 == 20 or n2 == 20 or n1 + n2 == 20

# Check
print(makes_twenty(20,10))
print(makes_twenty(12,8))
print(makes_twenty(2,3))

