

name = "Dave"
count = 1


def another():
    color = "blue"
    global count
    count += 4
    print(count)

    def greeting(name):
        print(color)
        print(name)

    greeting("Dave")

another()