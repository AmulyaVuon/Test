x=int(raw_input("enter the number"))
fact=1
if(x<0):
    print("can't find")
elif(x==0):
    print("factorial of 0 is 1")
else:
    for i in range(2,x+1):
        fact=fact*i
    print("factorial of",x,"is",fact)
        
    
