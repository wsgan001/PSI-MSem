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
            domain = words[2]
            # reald = (domain[len(domain) - 2] + "." + domain[len(domain) - 1])
            right.append(domain)
            server.add(domain)
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
    bar.finish()
    servercount.sort(reverse=True, key=takeSecond)
    for t in servercount[:5]:
        print(t, "\n")


def takeSecond(elem):
    return elem[1]


def getMueller():
    julia = list()
    with open("left.txt", 'r') as f:
        bar = Bar('GET MÜLLLER!', max=1191923)
        for line in f.readlines():
            bar.next()
            words = line.lower().split()
            # left.append
            # data_id.append(words[0])
            # data_t.append(datetime.datetime.strptime(words[1][1:-7].replace("t", " "), "%Y-%m-%d %H:%M:%S"))
            for j in range(4, 9):

                start_t = datetime.datetime.strptime("2009-05-0" + str(j) + " 20:14:30", "%Y-%m-%d %H:%M:%S")
                end_t = datetime.datetime.strptime("2009-05-0" + str(j) + " 20:15:30", "%Y-%m-%d %H:%M:%S")
                if (start_t <= datetime.datetime.strptime(words[1][1:-7].replace("t", " "), "%Y-%m-%d %H:%M:%S") <= end_t):
                    mueller.append(words[0])
        bar.finish()
        muellercount = []
        setmueller = set(mueller)
        listmueller = list(setmueller)
        for i in (range(0, len(listmueller))):
            if (mueller.count(listmueller[i]) > 10):
                muellercount.append([listmueller[i], mueller.count(listmueller[i])])
        muellercount.sort(reverse=True, key=takeSecond)
        for t in muellercount:
            print(t)


def getJulia():
    julias = list()
    matchlist = ["2009-05-02 17:00:05", "2009-05-02 22:00:16", "2009-05-03 19:00:05", "2009-05-03 19:00:05", "2009-05-03 22:00:23", "2009-05-04 17:00:03", "2009-05-04 22:00:52", "2009-05-05 17:00:02", "2009-05-05 21:59:52", "2009-05-06 18:00:04", "2009-05-06 19:00:03", "2009-05-06 21:59:46", "2009-05-07 21:00:05", "2009-05-07 22:00:04", "2009-05-07 22:00:04", "2009-05-07 22:00:31", "2009-05-08 21:59:47"]
    checkdate = list()
    for i in range(0, len(matchlist)):
        matchlist[i] = datetime.datetime.strptime(matchlist[i], "%Y-%m-%d %H:%M:%S")
        for j in range(2, 9):
            start_t = datetime.datetime.strptime("2009-05-0" + str(j) + " 21:59:30", "%Y-%m-%d %H:%M:%S")
            end_t = datetime.datetime.strptime("2009-05-0" + str(j) + " 22:00:35", "%Y-%m-%d %H:%M:%S")
            if (start_t <= matchlist[i] <= end_t):
                checkdate.append(matchlist[i] - datetime.timedelta(seconds=5))
    with open("left.txt", 'r') as f:
        bar = Bar('WHO THE FUCK SURFES ON WWW.TV-MOVIE.DE!', max=1191923)
        for line in f.readlines():
            bar.next()
            words = line.lower().split()
            time = datetime.datetime.strptime(words[1][1:-7].replace("t", " "), "%Y-%m-%d %H:%M:%S")
            for k in range(0, len(checkdate)):
                if (checkdate[k] <= time <= checkdate[k] + datetime.timedelta(seconds=5)):
                    julias.append(words[0])
        bar.finish()
        # print(len(julias))
        count = []
        j_set = set(julias)
        j_list = list(j_set)
        for i in (range(0, len(j_list))):
            count.append([j_list[i], julias.count(j_list[i])])
        count.sort(reverse=True, key=takeSecond)
        for t in count:
            print(t)


# top5servers()
# getMueller()
getJulia()
print("done")
