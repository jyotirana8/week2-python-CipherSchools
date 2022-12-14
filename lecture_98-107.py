#problem 1
# def square_list(l):
#     square=[]
#     for i in l:
#         square.append(i**2)
#     return square

# numbers=list(range(1,11))
# print(square_list(numbers))

#problem 2

# def reverse_list(l):
#     return l[::-1]


# def reverse_list(l):
#     r_list=[]
#     for i in range(len(l)):
#         popped_item=l.pop()
#         r_list.append(popped_item)
#     return r_list


# numbers=[1,2,3,4]
# print(reverse_list(numbers))

#problem 3

# def reverse_elements(l):
#     elements=[]
#     for i in l:
#         elements.append(i[::-1])
#     return elements

# words=['abc', 'tuv', 'xyz']
# print(reverse_elements(words))
     
# problem 4

def filter_odd_even(l): 
    odd_nums=[]
    even_nums=[]
    for i in l:
        if i%2==0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    output=[odd_nums, even_nums]
    return output

nums=[1, 2, 3, 4, 5, 6]
print(filter_odd_even(nums))

#problem 5

def common_finder(l1, l2):
    output=[]
    for i in l1:
        if i in l2:
            output.append(i)
    return output
print(common_finder([1,2,5,8], [1,2,7,6]))
    
    