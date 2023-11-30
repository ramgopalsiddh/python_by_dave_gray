squared = lambda num : num * num

print(squared(2))

addTwo = lambda num : num + 2

print(addTwo(12))


# pass more then 1 parameter in lambda
sum_total = lambda a, b : a + b

print(sum_total(2,3))

########################################################################

# use lambda in function bilder
def funcBuilder(x):
    return lambda num : num + x

# 10 is assign to x
addTen = funcBuilder(10)
addTwenty = funcBuilder(20)

# 7 is assign as num 
print(addTen(7))
print(addTwenty(7))

##################################################################

# Higher Order Functions

numbers = [3, 7, 12, 18, 20, 21]

squared_nums = map(lambda num : num * num, numbers)

print(list(squared_nums))

##################################

# Filter method 

odd_nums = filter(lambda num : num % 2 != 0, numbers )

print(list(odd_nums))

##################################################################

from functools import reduce


numbers = [1, 2, 3, 4, 5, 1]

# acc = accumulator or subtotal
# curr = current item
total = reduce(lambda acc, curr: acc + curr, numbers, 10)

print(total)

# use in built sum function for subtotal
print(sum(numbers, 10))

# count total  length of given names 
names = ['ram gopal siddh', 'suraj', 'shive', 'rahul']

char_count = reduce(lambda acc, curr: acc + len(curr), names, 0)

print(char_count)