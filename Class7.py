# set
# it removes duplicate elements, and it will not maintain order
set1 ={23,3,4,4,46,8,84,8,9}
l1=[23,3,4,4,46,8,84]
print(type(set1))
print(set1)
print(l1)
# CRUD
# Create
set1 = {23,3,4,4,46,8,84,8}
# Read
# Indexing and slicing will not work because set will not maintain the order data
for i in set1:
    print(i)

# update
# we can not update existing data, but we can add new data
set1.add(90)
print(set1)
set1.update([26,10,14])
print(set1)

# delete
set1.remove(10)
print(set1)
temp = set1.pop()
print(set1)

print("//////////mathematical methods///")
# intersection ,union ,difference ,difference update
# intersection => it gives common elements between two sets
s1 = {1,2,5,6,3,8}
s2 = {4,5,6}
s3 = s1.intersection(s2)
print(s3)
l1= [1,2,5,6,3,8]
l2 =[4,5,6]
s5 = set(l1)
s6 = set(l2)
s4  = s5.intersection(s6)
print(s4)

# union
s1 = {1,2,5,6,3,8}
s2 = {4,5,6,7}
s3 = s1.union(s2)
print(s3)
print("/////difference////")
# difference
s3 = s1.difference(s2)
print(s3)
s4 = s2.difference(s1)
print(s4)
print("////////difference update//")
# difference update
print(s1)
print(s2)
s2.difference_update(s1)
print(s2)

# premitive datatypes => string,int,float,bool
# sequence datatypes => list,tuple,dict,set