def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

user_input = "yes"

while user_input == "yes":

    a=int(input("enter your first number: "))
    b=int(input("enter your second number: "))

    operation=(input("which operation you want to perform(+,-,*,/) :"))

    if operation == "+" :
        print(add(a,b))
    elif operation == "-":
        print(sub(a,b))
    elif operation == "*":
        print(mul(a,b))
    elif operation == "/":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print(div(a, b))
    else:
        print("invalid operation.Use operations such as (+,-,*,/)")
    
    user_input=str(input("do you want to perform another calculation(yes/no) :"))