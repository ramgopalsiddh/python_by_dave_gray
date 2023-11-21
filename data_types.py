import math

# literal assignment 
first = "Ram Gopal"
last = "Siddh "

print(type(first))
print(type(first) == str)
print(isinstance(first, str))



#Constructor function
pizza = str("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))

#concatenation 
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

#Casting a number to a string 
decade = str(2023)
print(type(decade))
print(decade)

statement = "I complete my B.tech in " + decade + "s."
print(statement)

#Multiple Lines
multiline = '''
Hey, how are you ?                                  

I just done my work.       
                            All good
'''
print(multiline)

#Escaping special characters (\ = closeing, \t = tab, \n = new line, \\ = print single \)
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

#String method
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)


print("Length before add spaces:-", len(multiline))
multiline += "                                           "
multiline = "                                     " + multiline
print("Length After add spaces:-", len(multiline))

print("-------------------------------------------------------------------------------------------------")

print("Length After remove all spaces :-", len(multiline.strip()))   # remove all spaces
print("Length After remove left spaces :-", len(multiline.lstrip()))   # remove left spaces
print( "Length After remove right spaces :-", len(multiline.rstrip()))   # remove right spaces

print("--------------------------------------------------------------------------------------------------------")

#Build a menu
title = "menu".upper()
print(title.center(25, "="))
print("Coffee".ljust(20, ".") + "₹199".rjust(4))
print("Muffin".ljust(20, ".") + "₹249".rjust(4))
print("Cheesecake".ljust(20, ".") + "₹299".rjust(4))
print("Tea".ljust(20, ".") + "₹99".rjust(4))

print(" ")

#String index values
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])


#Some methods return boolean data
print(first.startswith("R"))
print(first.endswith("L"))


# Boolean data type

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric data type 

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

#float type
CGPA = 7.81
x = float(2.66)
print(type(CGPA))

#complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(CGPA))
print(abs(CGPA * -1))

print(round(CGPA))

print(round(CGPA, 1))


print(math.pi)
print(math.sqrt(64))
print(math.ceil(CGPA))
print(math.floor(CGPA))


# casting a string to a number
zipcode = "331403"
zip_value = int(zipcode)
print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("sardarshar")