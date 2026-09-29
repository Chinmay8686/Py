#Armstrong No
num = int(input("Enter NUmber :"))
p = len(str(num))
sum=0
n=num
while(num>0):
    sum+=(num%10)**p #power
    num//=10
if (n==sum):
    print("Number is Armstrong")
 