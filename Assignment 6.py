n=int(input())
l=list(map(int,input().split()))
l2=[]
while l!=[]:
    l.sort()
    l1=[]
    i=0
    while i<len(l):
        for j in range(i+1,len(l)):
            if l[i]<l[j] and l[i] not in l1:
                l1.append(l[i])
                l.remove(l[i])
                i=0
                break
        else:
            i+=1
    l2.append(max(l))
    l.remove(max(l))
print(len(l2))
    
