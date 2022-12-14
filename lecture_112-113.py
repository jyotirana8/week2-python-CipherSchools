#tuples
#tuples are immutable
#no append, no insert, no pop, no remove
#methods
#count, inde3x
#slicing
#tuples are faster than lists

example=('one', 'two', 'three')
print(example[::2])

#more about tuples
mixed=(1,2,3,4.0)
for i in mixed:
    print(i)
    
#tuple for one element
nums=(1,)
print(type(nums))

#tuple withot parenthesis
guitars='yamaha','batonrouge','taylor'
print(type(guitars))

#tuple unpacking

fruits=('apple', 'orange', 'kiwi')
fruit1, fruit2, fruit3 = (fruits)
print(fruit1)

#list inside tuples

 