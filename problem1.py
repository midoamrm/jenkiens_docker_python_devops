n=int(input())
l=[]
countlist=[]
num_of_problem=0

for i in range(0,n):
    l.append(input())
    #print(l[i])

for k in range(0,n):
    count=0
    if l[k][0]=="1":
        count=count+1
    if l[k][2]=="1":
        count=count+1
    if l[k][4]=="1":
        count=count+1
    countlist.append(count)    
for j in range(0,n):
    temp=int(countlist[j])
    if temp>=2:
        num_of_problem=num_of_problem+1
print( num_of_problem)
