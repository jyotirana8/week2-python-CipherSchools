#function returning two values

def func(int1, int2):
    add=int1+int2
    mutltiply=int1*int2
    return add, mutltiply

add, multiply=func(2,3)
print(add)
print(multiply)

# something more about tuples, lists, str
nums=tuple(range(1,11))
print(nums)