user_info={
    'name' : 'Muskan',
    'age' : 24,
    'fav_colours' : ['red', 'orange'],
    'fav_fruits' : ['apple', 'kiwi'],
    }

# how to add data
user_info['fav_songs']=['song1', 'song2']
print(user_info)

# pop method
popped_item = user_info.pop('fav_fruits')
print(f"popped item is {popped_item}")
print(user_info)

# popitem method
popped_item=user_info.popitem()
print(user_info)
print(type(popped_item))
