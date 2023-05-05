# Create
names = ['python', 'java', 'c#', 'c', 'linux', 'windows', 'perl', 'spark', 'scala']

# Create,Read
# update
# updating based on index
names[1] = 'Advanced java'
names[5] = 'windows 11'
# positive index , negative index, slice
names[-6] = 'C1.23'
print(names)
# slicing
names[1:4] = ['Java ++','C#1',"C45.5",'informatica','oracle']
print(names)


print("////delete //////")
# delete
del names[7]
del names[2:5]
print(names)
names.clear()
print(names)
del names
# print(names)

print("////update list with new data///")
courses =['Bcom',"BSC","BA","MBA"]
# append => this is used to insert single record
# extend => this is used to insert sequence of records
courses.append("B.Tech")
print(courses)
courses.append(["BBA","M.Tech"])
print(courses)

# extend
courses.extend("CA")
print(courses)
courses.extend(["CA"])
print(courses)
courses.extend(["MSC",'BED',['HEC']])
print(courses)
courses.append("Bcom")
print(courses)

# insert on particular index
courses.insert(2,"Medicine")
print(courses)
print("//////delete without index//")
# for delete without index
courses.remove('Bcom')
print(courses)
temp = courses.pop()
print(courses)
print(temp)
courses.pop()
print(courses)
# what is the difference between pop and remove => remove will delete the first occurrence of item, but
# it will not return anything
#  pop => by default it will remove last item from the list, and it will return the item which is removed
temp = courses.pop(4)
print(courses)
print(temp)
