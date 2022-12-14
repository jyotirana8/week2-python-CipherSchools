# in keyword and iterations in dictionary
user_info={
    'name' : 'Muskan',
    'age' : 24,
    'fav_colours' : ['red', 'orange'],
    'fav_fruits' : ['apple', 'kiwi'],
    }
# check if key exist in dictionary 

if 'address' in user_info:
    print('present')
else:
    print('not present')
    
# check if avlue exist in dictionary

if 'Muskan' in user_info.values():
    print('present')
else:
    print('not present')
    
# loops in dictionaries

for i in user_info:
    print(i)
    
for i in user_info.values():
    print(i)
    
# values method

user_info_values=user_info.values()
print(user_info_values)
print(type(user_info_values))

# items method

user_items = user_info.items()
print(user_items)
print(type(user_items))
