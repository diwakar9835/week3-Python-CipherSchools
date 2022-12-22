# summary dictionary
# what is dictionary
# unordered collection of data

d = {'name' : 'harshit', 'age' :24}

# or 
d1 = dict(name = 'harshit', age=24)

# or

d2 = {
    'name' : 'harshit',
    'age' : 24,
    'fav_movies' : []
}


# how to access data from dictionary
# you cannot do like
# d[0] , because there is no order inside dictionary

# syntex 
# print(dictname[keyname]) 
print(d['name'])


# add data inside empty dict
empty_dict = {}
empty_dict['key1'] = 'value1'
empty_dict['key2'] = 'value2'
print(empty_dict)