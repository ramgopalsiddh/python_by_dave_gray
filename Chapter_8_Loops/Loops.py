value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1

# while value <= 10:
#     value += 1
#     if value == 5:
#         continue
#     print(value)
# else:
#     print("value is now equal to " + str(value))


names = ["Dave", "Sara", "John"]
# for x in names:
#     print(x)

# # print each alphabet seprately
# for x in "Ram Gopal Siddh":
#     print(x)

# for x in names:
#     if x == "Sara":
#         break
#     print(x)

# for x in names:
#     if x == "Sara":
#         continue
#     print(x)

# print a range 
# for x in range(5):
#     print(x)

# # print a range between specific numbers
# for x in range(2,5):
#     print(x)

# print a range by a specific eteration in this example (5, 101, 5)
#  first 5 denote start from 5 and
#  2nd 101 define max limit and
#  no. 3rd 5 define the differnce between current and next number is 5
#   USE :- for print tables, print a specific eteration
for x in range(5, 101, 5):
    print(x)
else:
    print("Glade that\'s over!")


names = ["Dave", "Sara", "John"]
actions = ["codes", "eats", "sleeps"]

# outer loop perform 1st task then run inner loop till end then exit and run outer loop and then run inner loop till end and continous perform this task till complete run outer loop

# for name in names:
#     for action in actions:
#         print(name + " " + action + ".")

# if put action on outer loop then first perform 1st action with all name than 2nd action with all name and continoue.......
for action in actions:
    for name in names:
        print(name + " " + action + ".")

