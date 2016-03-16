import os
def getMem():
    fd = open('mem.txt')
    memory = fd.readlines()
    mainMem = []
    diskMem = []
    for i in range(0, 128):
        line = memory[i].split(' ')
        #print line
        page = []
        for j in range(2, len(line)):
            if line[j] != '\n':
                page.append(int(line[j],16))
        mainMem.append(page)
        #print page
    for i in range(128, 256):
        line = memory[i].split(' ')
        #print line
        page = []
        for j in range(2, len(line)):
            if line[j] != '\n':
                page.append(int(line[j],16))
        diskMem.append(page)
        #print page
    return mainMem, diskMem

