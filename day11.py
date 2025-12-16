# n=5
# # Approach-1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or j==1 or j==n or i==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# # Approach-2
# for i in range(1,n+1):
#     if i==1 or i==n :
#         print("* "*n)
#     else:
#         print("* "+"  "*(n-2)+"*")

# n=5
# # Approach -1 
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if i==1 or j==1 or i==n or j==i:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# #Approach -2 
# for i in range(1,n+1):
#     if  i==n or i==1:
#         print("* "*i)
#     else:
#         print("* "+"  "*(i-2)+"*")

n=5
# Approach -1 
for i in range(1,n+1):
    print("  "*(n-i),end=" ")
    for j in range(1,i+1):
        if i==1 or i==n or j==1 or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
# Approach -2
for i in range(1,n+1):
    v="  "*(n-i)
    if i==n or i==1:
        print(v+"* "*i)
    else:
        print(v+"* "+"  "*(i-2)+"*")