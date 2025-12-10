# a = [1, 3, 2, 3, 6]

# xor_sum = 0
# for num in a:
#     xor_sum ^= num

# print(xor_sum)

# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
    
#     pivot = arr[-1]
#     left = [x for x in arr[:-1] if x <= pivot]
#     right = [x for x in arr[:-1] if x > pivot]

#     return quick_sort(left) + [pivot] + quick_sort(right)


# arr = [4, 2, 7, 3, 1]
# print(quick_sort(arr))

# nearest Prime
def prime(n):
    for i in range(2,n):
       if n%i==0:
           return False
    return True
           
n=int(input("Enter a number:"))
l=n-1
h=n+1
if prime(n)==True:
    print(n)
else:
    while True:
        if prime(l):
            print(l)
            break
        if prime(h):
            print(h)
            break
        l-=1
        h+=1
        
