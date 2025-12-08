#input:iam a good student
# o/p:-tne d utsd oogamai
# approach-1
# s="iam a good student"
# s2=""
# count=[]
# for i in range(len(s)):
#     if s[i]==" ":
#         count.append(i)
#     else:
#         s2=s[i]+s2
    
# print(s2)
# sl=list(s2)
# for i in count:
#     sl.insert(i, " ")
# res="".join(sl)
# print(res)
# approach-2
# s="iam a good student"
# ss=s.replace(" ","")
# ss=ss[::-1]
# res=""
# i=0
# j=0
# while i<len(s):
#     if s[i]!=" ":
#         res+=ss[j]
#         i+=1
#         j+=1
#     else:
#         res+=" "
#         i+=1
# print(res)

# selection sort
l=[2,5,1,4,6]
for i in range(0,len(l)-1):
    m=i
    for j in range(i+1,len(l)):
        if l[j]<l[m]:
            m=j
    l[i],l[m]=l[m],l[i]
print(l)
