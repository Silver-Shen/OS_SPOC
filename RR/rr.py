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
    total = 0
    while(proc_num > 0):
        for i in range(0,len(proc)):
            if(proc[i] > time):
                total = total + time
                proc[i] = proc[i] - time
                print "[ time   %-2d ] Run job   %d for %.2f secs"%(co,i,time)
                co  = co + 1
            elif(proc[i] > 0):
                total = total + proc[i]
                print "[ time   %-2d ] Run job   %d for %.2f secs ( DONE at %.2f )"%(co,i,time,total)
                proc[i] = 0
                proc_num = proc_num - 1
                co  = co + 1


if __name__ == "__main__":
    (proc,time) = input_porc()
    proc_run(proc,time)