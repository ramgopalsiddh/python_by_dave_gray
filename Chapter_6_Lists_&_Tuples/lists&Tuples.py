# Create lists
users = ['Dave', 'John', 'Sara']

data = ['Dave', 42, True]

emptylist = []

# find list's data existence 
print("Dave" in users, "Dave" in data, "Dave" in emptylist)

# Indexing 
print(users[0])
print(users[-2])

print(users.index('Sara'))

# print lists data useing indexing
print(users[0:2])
print(users[1:])
print(users[-3:-1])

# identify Lenghth of lists
print("data's length:",len(data), ", users length:",len(users), ", empty list length:",len(emptylist))
print(len(data))

# Add data in lists
users.append('Elsa')
print(users)

users += ['Jason']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# Add a predefine list in list
# comment this because lists get multiple data type data
# users.extend(data)  
# print(users)

users.insert(0, 'Bob')
print(users)

# This insert value in list
users[2:2] = ['Eddie', 'Alex']
print(users)

#This replace(remove exestening vaiue from list) value in list 
users[1:3] = ['Robert', 'JPJ']
print(users)



# Delete data from list

users.remove('Bob')
print(users)

# pop print and remove list iteam from list 
print(users.pop())
print(users)

# del Delete iteam useing indexing 
del users[0]
print(users)

# Delete complete list in this don't existing list and lists data  
# comment this because after delection and when try to print show errer in code 
# del data
# print(data)

# Clear delete lists all data but empty list still existing
data.clear()
print(data)

# put [] when replace only one data, without [] add every alphabet print seprate
# Add a lower case word in list 
users[1:2] = ['dave']

# Sort list 
users.sort()
print(users)

# Sorting data, give priority to lower case
users.sort(key=str.lower)
print(users)

nums = [4, 42, 78, 1, 5]
# In this only list's indexing reverse, list don't shorting in reverse order
nums.reverse()
print(nums)

# Sort list in reverse order
nums.sort(reverse=True)
print(nums)

# sorting 
print(sorted(nums, reverse=True))

# Create lists copy from 3 different ways
numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(" ")

print(numscopy)
print(mynums)
# sort copy of list
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1, "Neil", True])
print(mylist)



# Tuples
# 1. Tuples can't edited 
mytuple = tuple(('Dave', 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

# Edit tuples by use list
newlist = list(mytuple)
newlist.append('Neil')
newtuple = tuple(newlist)
print(newtuple)

(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

# Counting occurrences of number 2 inside anothertuple
print(anothertuple.count(2))