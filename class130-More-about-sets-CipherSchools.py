# in keyword in sets and for loop

s = {'a','b','c'}

# in keyword to check if items is present or not in set
if 'a' in s:
    print("present")
else:
    print("not present")

# for loop
for item in s:
    print(item)

l = [1,2,3,3]
print(set(l))

# set maths

s1 = {1,2,3,4}
s2 = {3,4,5,6}

# union
# intersection

union_set = s1 | s2
print(union_set)

# intersection
print(s1 & s2)