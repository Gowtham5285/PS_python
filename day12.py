# Two-sum
# Approach-1
# def two_sum(l,tar):
#     seen =set()
#     for i in l:
#         if (tar-i) in seen:
#             return True
#         seen.add(i)
#     return False
    
# l=list(map(int,input("Enter the list:").split()))
# tar=int(input("Enter the target value:"))
# print(two_sum(l,tar))
# Approach-2
# l=[3,7,1,2,5]
# t=6
# l.sort()
# i=0
# j=len(l)-1
# while i<j:
#     if l[i]+l[j]==t:
#         print(True)
#         break
#     elif l[i]+l[j]>t:
#         j-=1
#     else:
#         i+=1
# else:
#     print(False)

# Binary Search
# l=[1,4,6,7,9,11]
# tar=11
# i,j=0,len(l)-1
# m=i+j//2
# while 0<= m <=len(l)-1:
#     m=i+j//2
#     if l[m]==tar:
#         print(True)
#         break
#     elif l[m]>tar:
#         j=m-1
#     else:
#         i=m+1

l=[1,4,6,7,9,11]
tar=5
i,j=0,len(l)-1
while i<=j:
    mid=(i+j)//2
    if l[mid]==tar:
        print(mid)
        break
    elif l[mid]>tar and l[mid-1]<tar:
        print(mid)
        break
    elif l[mid]<tar and l[mid+1]>tar:
        print(mid+1)
        break
    else:
        if l[mid]>tar:
            j=mid-1
        else:
            i=mid+1
    
