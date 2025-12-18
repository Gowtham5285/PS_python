# Reverse of a string with its word count
s=" iam from hyd  "
l=s.split()
for i in range(len(l)):
    l[i]=l[i][::-1]
res=" ".join(l)
i,j=0,len(s)-1
l_c,t_c=0,0
while i<len(s):
    if s[i]!=" ":
        break
    else:
        l_c+=1
        i+=1
while j>=0:
    if s[i]!=" ":
        break
    else:
        t_c+=1
        j-=1
res=" "*l_c+res+" "*t_c
print(res)
# Trailing zeroes in the factorial
n=20
fact=1
c=0
for i in range(2,n+1):
    fact=fact*i
factstr=str(fact)
for i in range(len(factstr)-1,-1,-1):
    if factstr[i]!="0":
        break
    else:
        c+=1
print(c)