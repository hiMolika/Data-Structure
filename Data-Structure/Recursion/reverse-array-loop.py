# reverse an array using loop
def func(arr):
    n = len(arr)
    for i in range(n//2): # iterate only upto the middle of the array
        temp = arr[i]
        arr[i] = arr[n-i-1]
        arr[n-i-1] = temp
    return arr

arr = [1,2,3,4,5,6,7,8,9,10]
print(func(arr))