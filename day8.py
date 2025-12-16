# Insertion Sort 
s=[7,2,3,60,1]
for i in range(1,len(s)):
    key=s[i]
    j=i-1
    while j>=0 and s[j]>key:
        s[j+1]=s[j]
        j-=1
    s[j+1]=key
print(s)
# single unique element in the duplicate elements in a list
# approach-1
# l=[2,3,3,4,7,1,4,1,2]
# for i in l:
#     if l.count(i)==1:
#         print(i)
#         break
# approach-2
# res={}
# for i in l:
#     if i not in res:
#         res[i]=1
#     else:
#         res[i]+=1
# print(res)
# approach-3
l=[2,3,3,4,7,1,4,1,2]
res=0
for i in l:
    res^=i
print(res)

