def input(filename):
    fd = file(filename)
    list = fd.readlines()
    t = int(list[0][0:-1])
    order = list[1][0:-1]
    return (t,order)
    
def make():
    (t,order) = input('test.txt')
    page = {}
    temp_page = {}
    loss = 0
    delta = 1
    for i in order :
        if(i in page):
            delta = delta + 1
            temp_page[i] = 0
        else:
            print "loss = " + i + " delta = " + str(delta)
            if(delta > t):
                temp_page[i] = 0
                page = temp_page
                temp_page = {}
                temp_page[i] = 0
                delta = 1
                print "replace"
            else:
                page[i] = 0
                temp_page = {}
                temp_page[i] = 0
                delta = 1
                print "add"
                