# Find the largest of three numbers.
a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
if(a>=b and a>=c):
    print("larger first numbe is",a)

elif(b>=a and b>=c):
    print("larger second number is",b)

else:
    print("larger number is third is ",c)
