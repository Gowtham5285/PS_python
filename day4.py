def freq(a):
    count=1
    maxcount=0
    for i in range(1,len(a)):
        if a[i]==a[i-1]:
            if(a[i]=="1"):
                count+=1         
        else:

            if(maxcount<count):
                maxcount=count 
            count=1
    if(maxcount<count):
        maxcount=count
    return maxcount
print(freq("0001111101111001"))

# bubble sort - O(n**2)
# selection sort - O(n**2)
# insertion sort - O(n**2)
# quick sort - O(nlogn)
# merge sort - O(nlogn)
