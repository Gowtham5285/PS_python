# Strong number
# def factorial(n):
#     fact=1
#     if n==0 or n==1:
#         return 1
#     else:
#         for i in range(2,n+1):
#             fact*=i
#     return fact
# number=int(input("enter the number:"))
# rem=0
# sum=0
# temp=number
# while number>0:
#     rem=number%10
#     sum+=factorial(rem)
#     number= number//10
# print(sum)
# if sum==temp:
#     print("Strong Number")
# else:
#     print("Not a strong number")

#anagram
# a="listen"
# b="silent"
# count=0
# if len(a)==len(b):
#     for i in a:
#         if i in b:
#             count+=1
#         else:
#             break
# if count==len(b):
#     print("Anagram")
# else:
#     print("Not an Anagram")


# Biggest two among three numbers with sum given in WIPRO
a=int(input("Enter number1:"))
b=int(input("enter number2:"))
c=int(input("Enter number3:"))
# if a>=b and a>=c:
#     first=a
#     if b>=c:
#         second=b
#     else:
#         second=c
# elif a<=b and b>=c:
#     first=b
#     if a>=c:
#         second=a
#     else:
#         second=c
# else:
#     first=c
#     if a>=b:
#         second=a
#     else:
#         second=b
# sum=first+second
# print(sum)

res=a+b+c
if a<=b and a<=c:
    print(res-a)
elif b<=a and b<=c:
    print(res-b)
else:
    print(res-c)