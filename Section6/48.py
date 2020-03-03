def spy_game(nums):
    code = [0,0,7]
    pointer = 0
    for num in nums:
        if pointer == 3:
            return True
        if num == code[pointer] and pointer < 3:
            pointer += 1
    return pointer > 2

# Check
print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,4,5,0]))


def count_primes(num):
    list_primes = [2]
    count = 3
    while count <= num:
        for i in list_primes:
            if count % i == 0:
                count += 2
                break
        else:
            list_primes.append(count)
            count += 2
    print(list_primes)
    return len(list_primes)


# Check
print(count_primes(100))