# Sum of the list using recursion
def sum_list(l, summ, i, n):
    if i == n:
        return summ
    return sum_list(l, summ + l[i], i + 1, n)

l = [39, 10, 2, 3, 4]
n = len(l)
i = 0
summ = 0

print(sum_list(l, summ, i, n))



# fibonaaci number finding using recursion
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
n=6
print(fib(n))
