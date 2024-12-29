# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
def reverse(x):
    is_neg=x<0
    x=abs(x)
    rev_no=0
    while(x>0):
        last_digit = x%10
        x = x//10
        rev_no = rev_no*10+last_digit

        # checking for range given
        if rev_no > 2**31-1:
            return 0
    
    return rev_no*-1 if is_neg else rev_no

n=-123
print(reverse(n))