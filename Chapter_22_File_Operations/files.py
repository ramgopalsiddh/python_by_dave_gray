import os
# r = Read
# a = Append
# w = Write
# x = Create

# Read - error if it doesn't exist

f = open("names.txt")
# read full file
#print(f.read())

# read first 8 characters
# print(f.read(8))

# read first line of file
# print(f.readline())

# when print 2 time get next line not print a single line 2 time(but have a blank line between these)
# print(f.readline())
# print(f.readline())

# print by use loop line by line 
for line in f:
    print(line)

f.close()


try:
    f = open("name_list.txt")
    print(f.read())
except:
    print("The file you want read doesn't exist")
finally:
    f.close()



# Append - create the file if it doesn't exist 

f = open("names.txt", "a")
f.write("Ramniwash\n")
f.close()

f = open("names.txt")
print(f.read())
f.close()

# Write (overwrite)

f = open("context.txt", "w")
f.write("I delete all of the context.")
f.close()

f = open("context.txt")
print(f.read())
f.close()


# Two way to create a new file

# Opens a file for writing , create the file if it does not exist
f = open("name_list.txt", "w")
f.close()

# Creates the specified file, but return an error if the file exists
if not os.path.exists("ramgopal.txt"):
    f = open("ramgopal.txt", "x")
    f.close()

# Delete a file

# avoide an error if it doesn't exist
if os.path.exists("ramgopal.txt"):
    os.remove("ramgopal.txt")
else:
    print("The file you wish to delete does not exist.")


# copy open file content to another file
with open("more_names.txt") as f:
    content = f.read()


with open("names.txt", "w") as f:
    f.write(content)