def largestElement(a):
    max=float("-inf")
    for i in a:
        if max<i:
            max=i
    return max
a=[4,7,1,9]
larg=largestElement(a)
print(larg)