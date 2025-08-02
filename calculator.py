a=int(input("enter first operand : "))
operator=input("enter the operator : ")
b=int(input("enter second operand : "))
if operator == "+":
    print("result:", a+b)
elif operator=="-":
    print("result:", a-b)
elif operator=="*":
    print("result:", a*b)
elif operator=="/":
    print("result:", a/b)
else :
    print("invalid operator")