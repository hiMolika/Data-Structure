def gcd_fun(x,y): # x = 5 , y = 10
    while (y!=0):
        x,y = y,x%y
    return x     

x=5
y=10
print(gcd_fun(x,y))