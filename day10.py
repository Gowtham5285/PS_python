a=[(1,23),(2,4),(0,49),(11,0),(-1,-1)]
res=[]
for i in a:
    res.append(i[1])
res.sort()
ll=[]
for i in res:
    for j in a:
        if i==j[1]:
            ll.append(j)
print(ll)

print(sorted(a,key=lambda i:i[1]))

