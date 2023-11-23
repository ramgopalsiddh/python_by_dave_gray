# Dictionaries

band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Page")

print(band)
print(band2)
print(type(band))
print(len(band))

#Access items 
print(band["vocals"])
print(band.get("guitar"))

#list all keys
print(band.keys())

#list all values
print(band.values())

# list of key/vaues pairs as tuples
print(band.items())

#verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change values
band["vocals"] = "Coverdale"
band.update({"bass": "JPJ"})

print(band)

# Remove iteam
print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem())  #tuple
print(band)

# Delete and clear

band["drums"] = "Bonham"
# delete specific iteam from Dictionaries
del band["drums"]
print(band)

# clear all data of Dictionaries only {} show in print
band2.clear()
print(band2)

# Delete entire Dictionaries if try to print show errer(name 'band2' is not defined.)
del band2


# Copy Dictionaries

# Bad way to create copy

# band2 = band
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good Copy!")
print(band3)

# Neasted Dictionaries

member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])


# Sets

nums = {1, 2, 3, 4}

nums2 = set((1,2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# No duplicate allowed
nums = {1, 2, 2, 3}
print(nums)

# True is a dupe of 1, false is a dupe of zero
# if True/False has before number then take boolen input and 
# if number come before boolen then number taken as input

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# Check if a value is in a set
print(2 in nums)

# But you cannot refer to an element in the set with an index position or a key

# Add a new element to a set
nums.add(8)
print(nums)

# Add element from one set to another
morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries, too.

# Merge two sets to create a new set 
one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

# keep only the Duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

# keep everything except the Duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)