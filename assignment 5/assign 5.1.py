l=[1,2,3]
newlist=[]
for i in range(len(l)):
    x=l[0:i]+l[i+1:]
    print(x)
    if x not in newlist:
        newlist.append(x)
print(newlist)