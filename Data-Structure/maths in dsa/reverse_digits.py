num=int(input("Enter the number: "))
print("number before reversing:",num)
rev_no=0
while(num>0):
    last_digit=num%10
    num=num//10 # quotient
    rev_no=(rev_no*10)+last_digit
print("number after reversing: ",rev_no)