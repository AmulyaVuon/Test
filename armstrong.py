x=raw_input("enter the number")
order=len(str(x))
num=int(x,10)
print(num)
s=0
while(num>0):
    t=num%10
    s+=t**order
    num=num/10
#print("s=",s)
#print("num=",num)
#print("x=",x)
if(s==int(x)):
    print("the number",x,"is armstrong")
else:
    print("not the armstrong number")


# Program to check Armstrong numbers in certain interval

#lower = 100
#upper = 2000

# To take input from the user
"""lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))

for num in range(lower, upper + 1):

   # order of number
   order = len(str(num))
    
   # initialize sum
   sum = 0

   # find the sum of the cube of each digit
   temp = num
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)"""
