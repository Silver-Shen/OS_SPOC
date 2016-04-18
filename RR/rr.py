import sys

def input_porc():
    print "please input proc list:"
    input=raw_input()
    input = input.split(' ')
    proc = []
    for i in input:
        if((int(i)) > 0):
            proc.append(int(i))
        
    print "please input time slice:"
    time=int(raw_input())
    return proc,time

def proc_run(proc,time):
    co = 0
    proc_num = len(proc)
    while(proc_num > 0):
        for i in range(0,len(proc)):
            if(proc[i] > time):
                proc[i] = proc[i] - time
                print proc[i]
            elif(proc[i] > 0):
                proc[i] = 0
                proc_num = proc_num - 1
                print proc[i]


if __name__ == "__main__":
    (proc,time) = input_porc()
    proc_run(proc,time)