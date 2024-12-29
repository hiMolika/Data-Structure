# using recursion wihtout loop
'''
def reverse_array(arr):
    def func(l,r):
        if l>=r:
            return
        temp = arr[l]
        arr[l] = arr[r]
        arr[r] = temp
        func(l+1,r-1)
    func(0,n-1)
    return arr

arr = [1,2,3,4,5]
n = len(arr)
print(reverse_array(arr))
'''

