name = 'chandra'
# print(type(name))
id = 2334
address = 'BLR'
# sequence data types => nothing but collection of different data types
# list
# tuple
# set
# dict


# list => it is collection of different data types of data
l1 = ['chandra', 3555, 'AP', 56.56, True]
print(type(l1))
l1 = [name, id, address, 56.56, True]
# CRUD operations
# Create , Read ,Update ,delete
# create => creating data initially in list
l1 = ['chandra', 34345, address, 56.56, True]

# Read
print(l1)
# how to read individual data from list
# data will read based on indexing from list, index will start with 0
print(l1[0])
print(l1[2])
print(l1[4])
# print(l1[5]) =>list index out of range

names = ['python', 'java', 'c#', 'c', 'linux', 'windows', 'perl', 'spark', 'scala']

# length of list => len(names)
print("length of names ", len(names))
print(names[4])
print(names[6])
print(names[5])

# I need 3rd data from names from last
temp = len(names) - 3
print(names[temp])

# positive indexing  => it will start with 0 and total length-1
# negative indexing => it will start with -1 from end of list it will start
print("////////////")
print("negative indexing --", names[-1])
print(names[-4])
temp = len(names)
print(temp)
print(names[-temp])

print("///// Slicing ////////")
# start index => start point
# end index  => end point => this will consider provided end index-1
names = ['python', 'java', 'c#', 'c', 'linux', 'windows', 'perl', 'spark', 'scala']

print("slicing ", names[0:3])
print(names[2:6])
print(names[4:7])

# step size
print("////////step size/////////")
print(names[0:5])
print("with step size 2:", names[0:5:2])
print("with step size 3:", names[0:5:3])
# names [startindex : endindex(consider -1) : step size]
print(names[2:7:4])

# default settings of slice
print("////default//")
print(names[2:])
print(names[2::2])
print(names[::2])

# slicing with negative index
print("//////negative slicing////")
print(names[1:5])
print(names[-8:-4:2])


# step size with negative value
print("////negative step size/////")
print(names[1:5])
print(names[5:1:-1])
print(names[6:0:-1])
print(names[6:0:-2])