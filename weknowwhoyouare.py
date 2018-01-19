import numpy as np
from progress.bar import Bar

delay = 10
students = set()
left = [[], []]
right = [[], []]
server = set()


def count_students():
    with open("left.txt", 'r') as f:
        for line in f.readlines():
            words = line.lower().split()
            left.append(words[0])
            students.add(words[0])
    print("count of students> ", len(students))
    # print(students)


def count_server():
    with open("right.txt", 'r') as f:
        for line in f.readlines():
            words = line.lower().split()
            right.append(words[2])
            server.add(words[2])
    print("count of server> ", len(server))
    # print(server)


def top5servers():
    if len(server) == 0:
        count_server()
    servercount = []
    listofserver = list(server)
    bar = Bar('Processing', max=len(server))
    for i in (range(0, len(server))):
        bar.next()
        servercount.append([listofserver[i], right.count(listofserver[i])])
        servercount.sort(reverse=True, key=takeSecond)

    bar.finish()
    print(servercount[:5], "\n")


def takeSecond(elem):
    return elem[1]


# count_server()
# top5servers()
count_students()
print("done")
