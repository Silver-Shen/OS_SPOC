import sys

def mean(list):
    sum = 0.0
    for i in list:
        sum = sum + i
    return sum/len(list)

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
    print "ARG policy RR"
    co = 0
    proc_num = len(proc)
    print "ARG jobs %d"%(proc_num)
    total = 0
    
    print "Here is the job list, with the run time of each job: "
    
    for i in range(0,proc_num):
        print "Job %d ( length = %d )"%(i,proc[i])
    
    print "** Solutions **"
    total_cost = []
    response = []
    temp_proc = []
    for i in range(0,len(proc)):
        total_cost.append(-1)
        response.append(-1)
        temp_proc.append(proc[i])
    while(proc_num > 0):
        for i in range(0,len(proc)):
            if(response[i] == -1):
                response[i] = total
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
                total_cost[i] = total
                
    print "Final statistics:"
    for i in range(0,len(proc)):
        print "Job   %d -- Response: %.2f  Turnaround %.2f  Wait %.2f"%(i,response[i],total_cost[i],total_cost[i]-temp_proc[i])
    print "Average -- Response: %.2f  Turnaround %.2f  Wait %.2f"%(mean(response),mean(total_cost),mean(total_cost)-mean(temp_proc))


if __name__ == "__main__":
    (proc,time) = input_porc()
    proc_run(proc,time)