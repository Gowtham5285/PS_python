#palindrome 
a="ram"
rev=""
# for i in range(len(a)-1,-1,-1):
#     rev=a[i]+ rev
# print(rev)
# if a==rev:
#     print("Palindrome")
i=0
j=len(a)-1
flag=0
while i<j:
    if a[i]==a[j]:
        i+=1
        j-=1
    else:
        flag=1
        break
if flag==1:
    print("False")
else:
    print("True")