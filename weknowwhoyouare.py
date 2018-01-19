import numpy as np

delay = 10
students = set()
left = [[],[]]
#students.append([])
right = [[],[]]
server = set()
#server.append([])



def count_students():
    with open("left.txt", 'r') as f:
        i = 0
        for line in f.readlines():
            words = line.lower().split()
            left.append(words[0])
            students.add(words[0])           
    print(len(students))
    #print(students)

def count_server():
    with open("right.txt", 'r') as f:
        for line in f.readlines():
            words = line.lower().split()
            right.append(words[2])
            server.add(words[2])
    print(len(server))
    #print(server)

def top5servers():
    servercount = [[]]
    listofserver = list(server)
    for i in range(0, len(server)):
        servercount.append([listofserver[i],right.count(listofserver[i])])
    print(servercount)
    
count_server()
count_students()
top5servers()
print("done")
