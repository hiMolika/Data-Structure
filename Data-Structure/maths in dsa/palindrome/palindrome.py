def ispalindrome(x):
    dup=x
    rev_no=0
    while(x>0):
        last_dig=x%10
        x=x//10
        rev_no=rev_no*10+last_dig
    if rev_no==dup:
        return True
    else:
        return False

x=121
print(ispalindrome(x))