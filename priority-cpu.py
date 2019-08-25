#NON-PREEMPTIVE PRIORITY SCHEDULING 
n=int(input("Enter number of processes: "))
p=[ ]
bt=[ ]
at=[ ]
wt=[ ]
tat=[ ]
priority=[ ]
for i in range(n):
        p.append(i+1)
        temp=int(input("Enter burst time: "))
        temp2=int(input("Enter arrivial time: "))
        temp3=int(input("Enter priority : "))
    
        bt.append(temp)
        at.append(temp2)
        priority.append(temp3)
    
for i in range(n-1):                    #sorting according to priority
        for j in range(n-1-i):
                if priority[j]>priority[j+1]:
                        temp=priority[j]
                        priority[j]=priority[j+1]
                        priority[j+1]=temp

                        temp=bt[j]
                        bt[j]=bt[j+1]
                        bt[j+1]=temp

                        temp=at[j]
                        at[j]=at[j+1]
                        at[j+1]=temp

                        temp=p[j]
                        p[j]=p[j+1]
                        p[j+1]=temp
        
for i in range(n):           #calculating waiting time
    temp3=0
    for j in range(i):
        temp3+=bt[j]-at[j]

    wt.append(temp3)

for i in range(n):           #calculating turnaround time
    temp4=0
    temp4+=wt[i]+bt[i]
    tat.append(temp4)

print("process sending order: ")           #process sending order
for i in p:
    print("p",i)

#print(wt)
#print(tat)
avg_wt=sum(wt)/n
print("average waiting time: ",avg_wt)            #printing results

avg_tat=sum(tat)/n
print("average turn around  time: ",avg_tat)




        
    

    
        
    
