a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
op = input("Enter operator: ")

if(op=='+' or op=='add'):
    print(a+b)
elif(op=='-' or op=='sub'):
    print(a-b)
elif(op=='*' or op=='multiply'):
    print(a*b)
elif(op=='/' or op=='divide'):
    if(b==0):
        print("Error division by zero")
    else:
        print(a/b)
elif(op=='**' or op=='divide'):
    print(a**b)
elif(op=='%' or op=='modulo'):
    print(a%b)
else:
    print("Invalid Operation!")



