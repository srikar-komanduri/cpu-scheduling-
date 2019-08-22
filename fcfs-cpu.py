#FIRST COME FIRST SERVE -SCHEDULING 
n=int(input("Enter number of processes: "))
p=[ ]
bt=[ ]
at=[ ]
wt=[ ]
tat=[ ]

for i in range(n):
        p.append(i+1)
        temp=int(input("Enter burst time: "))
        temp2=int(input("Enter arrivial time: "))
    
        bt.append(temp)
        at.append(temp2)
        
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


avg_wt=sum(wt)/n
print("average waiting time: ",avg_wt)            #printing results

avg_tat=sum(tat)/n
print("average turn around  time: ",avg_tat)




        
    

    
        
    
