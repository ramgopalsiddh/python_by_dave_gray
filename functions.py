def hello_world():
    print("Hello World!")

hello_world()

def sum(num1, num2):
    print(num1 + num2)

sum(2, 3)
sum(7, 3)
sum(20, 3)

# validate given input in function is in proper data type
def sum(num1=0, num2=0):
    if(type(num1) is not int or type(num2) is not int):
        return "📢 please enter only integer type input ❗"
    return num1 + num2

total = sum(17, 3)
print(total)

def multiple_items(*args):
    print(args)
    print(type(args))

multiple_items("Dave", "John", "Sara")

def multi_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

multi_named_items(first="Dave",last="Gray")