import numpy as np
from progress.bar import Bar
import sys
import datetime
import time

delay = 10
students = set()
left = [[], []]
right = [[], []]
server = set()
mueller = list()
data_t = list()
data_id = list()


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


def getMueller():
    with open("left.txt", 'r') as f:
        for line in f.readlines():
            words = line.lower().split()
            # left.append
            data_id.append(words[0])
            data_t.append(datetime.datetime.strptime(words[1][1:-7].replace("t", " "), "%Y-%m-%d %H:%M:%S"))
        print("done appending left")
        for i in range(0, len(data_t)):
            # if (data_t[i] > start_t and data_t[i] < end_t):
            for j in range(4, 9):
                start_t = datetime.datetime.strptime("2009-05-0" + str(j) + " 20:14:30", "%Y-%m-%d %H:%M:%S")
                end_t = datetime.datetime.strptime("2009-05-0" + str(j) + " 20:15:30", "%Y-%m-%d %H:%M:%S")
                if (start_t <= data_t[i] <= end_t):
                    print(start_t)
                    print(end_t)
                    print(data_t[i])
                    print(data_id[i], data_t[i])
                    mueller.append(data_id[i])


def top5ip():
    if len(mueller) == 0:
        getMueller()
    muellercount = []
    setmueller = set(mueller)
    listmueller = list(setmueller)
    for i in (range(0, len(listmueller))):
        muellercount.append([listmueller[i], mueller.count(listmueller[i])])
        muellercount.sort(reverse=True, key=takeSecond)
    print(muellercount, "\n")


# count_server()
# top5servers()
getMueller()
# d = datetime.datetime.strptime("01:15:41", "%H:%M:%S")
# print(d)
top5ip()
print("done")
