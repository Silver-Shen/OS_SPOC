def input(filename):
    fd = file(filename)
    list = fd.readlines()
    t = int(list[0][0:-1])
    order = list[1][0:-1]
    init = list[2][0:-1]
    print "access order = " + order
    print "window = " + str(t)
    print "init state = " + init
    return (t,order,init)
    
def make():
    (t,order,init) = input('test.txt')
    page = {}
    temp_page = {}
    for i in init:
        page[i] = 0
    loss = 0
    delta = 1
    for i in order :
        if(i in page):
            delta = delta + 1
            temp_page[i] = 0
            print "hit " + i
        else:
            print "miss = " + i + " delta = " + str(delta)
            if(delta > t):
                temp_page[i] = 0
                page = temp_page
                temp_page = {}
                temp_page[i] = 0
                delta = 1
            else:
                page[i] = 0
                temp_page = {}
                temp_page[i] = 0
                delta = 1
                