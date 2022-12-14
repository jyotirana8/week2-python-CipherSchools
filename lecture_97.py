# generate lists with range functions

# numbers=list(range(1,11))
# print(numbers)

#pop method

# numbers=list(range(0,11))
# numbers.pop()
# print(numbers)
# print(numbers.pop())

#index method

numbers=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
# print(numbers.index(1, 3))
# print(numbers.index(1, 3, 6))

def negative_list(l):
    negative=[]
    for i in l:
        negative.append(-i)
    return negative

print(negative_list(numbers))
    