# min and max functions

numbers=[3, 45, 22]
print(min(numbers))
print(max(numbers))

def greatest_diff(l):
    return max(l) - min(l)

print(greatest_diff(numbers))

# exercise 
def sublist_counter(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

mixed=[1,2,3, [1,2], [3,4]]
print(sublist_counter(mixed))    

