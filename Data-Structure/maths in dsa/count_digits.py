num=int(input("enter:"))
print ("number: ",num)
count=0
while (num>0):
    last_digit=num%10 # remainder
    count= count+1
    num = num//10 #quotient
print(count)



