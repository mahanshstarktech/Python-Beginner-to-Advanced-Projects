try:
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
        print(a/b)
    elif(op=='**' or op=='divide'):
        print(a**b)
    elif(op=='%' or op=='modulo'):
        print(a%b)
    else:
        print("Invalid Operation!")

except ValueError as ve:
    print(ve)
    print("Input numbers only")

except ZeroDivisionError as zde:
    print(zde)
    print("Can't divide by Zero")

