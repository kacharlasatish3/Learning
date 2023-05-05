# Flow controls => loops
# for , while
# for  => iteration

bank_names = ['hdfc', 'sbi', 'icici', 'hsbc', 'kotak']
for item in bank_names:
    print(item)

users = [{"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
          "avatar": "https://reqres.in/img/faces/7-image.jpg"}
    , {"id": 8, "email": "lindsay.ferguson@reqres.in", "first_name": "Lindsay", "last_name": "Ferguson",
       "avatar": "https://reqres.in/img/faces/8-image.jpg"}
    , {"id": 9, "email": "tobias.funke@reqres.in", "first_name": "Tobias", "last_name": "Funke",
       "avatar": "https://reqres.in/img/faces/9-image.jpg"}
    , {"id": 10, "email": "byron.fields@reqres.in", "first_name": "Byron", "last_name": "Fields",
       "avatar": "https://reqres.in/img/faces/10-image.jpg"}
    , {"id": 11, "email": "george.edwards@reqres.in", "first_name": "George", "last_name": "Edwards",
       "avatar": "https://reqres.in/img/faces/11-image.jpg"}
    , {"id": 12, "email": "rachel.howell@reqres.in", "first_name": "Rachel", "last_name": "Howell",
       "avatar": "https://reqres.in/img/faces/12-image.jpg"}]

temp = users[0]
print(temp)
print(temp["first_name"])
print(users[0]["first_name"])
print(users[4]["email"])

print("//////")
data = [(3, 5), {"id": 232, "name": "chandra"}, [4, 5, 6], 'hdfc', 'sbi', 344]
print("/////////data//////")
for i in data:
    if type(i) is list or type(i) is tuple:
        for j in i:
            print(j)
    else:
        print(i)
print("//////end data /////")
print("//////users////////")
for item in users:
    print(item["first_name"])

print("////loop dictionary////")
user = {"id": 7, "email": "michael.lawson@reqres.in", "first_name": "Michael", "last_name": "Lawson",
        "avatar": "https://reqres.in/img/faces/7-image.jpg"}

for j in user.keys():
    print(user[j])

tupl1 = (2, 3, 4, 5)
for i in tupl1:
    print(i)

set1 = {1, 2, 4}
for i in set1:
    print(i)

str1 = "hello"
for i in str1:
    print(i)
x = 4555
for i in str(x):
    print(i)

print("////////range//////")

# range => to take the range of numbers , which contains start index,end index,step size
#
for i in range(0, 20, 2):
    print(i)

print("//////even numbers////")
# I want to print even numbers between 12 and 34
for i in range(12, 35):
    if i % 2 == 0:
        print(i)

# 0,len(l1)-1
# l1[0:5:]
l1 = ['python', 'java', 'c#', 'c', 'linux', 'windows', 'perl', 'spark', 'scala']
for i in range(0, len(l1), 2):
    print(l1[i])

l1 = [1, 2, 3, 4, 5, 6]
l2 = ['python', 'java', 'c#', 'c', 'linux', 'windows']
# dict1 ={1:"python",2:"java",3:"c#"}
dict1 = {}
for i in range(0, len(l1)):
    dict1[l1[i]] = l2[i]

print(dict1)

# while
# this will execute based on condition , if condition is true it will execute the code until condition fails
i = 0
while i < 10:
    print(i)
    i += 1

str1 = "hello"
print(str1[::-1])
output = ''
for i in str1:
    output = i + output

print(output)

# with while, I want to print first 20 even numbers
i = 0
count = 0
while count < 21:
    if i % 2 == 0:
        print(i)
        count += 1
    i += 1





#  reverse a number without converting to string by using while and floor division
x = 3456
# 6543
output = 0

while x > 0:
    temp = x % 10
    output = output * 10 + temp
    x = x // 10

print(output)


