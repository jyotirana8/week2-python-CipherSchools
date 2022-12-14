# fromkeys
d = dict.fromkeys(['name', 'age', 'height'], 'unknown')
print(d)

d=dict.fromkeys(range(1,11), 'unknown')
print(d)

# get method
d={'name' : 'unknown', 'age' : 'unknown'}
# print(d['names'])
print(d.get('names'))

# clear method
# d.clear()
# print(d)

# copy method

d1=d.copy()
print(d1)

