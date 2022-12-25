print('''
+ ADD
- SUBTRACT
* MULTIPLY
/ DIVIDE
''')

num1=int(input("Enter the value 1:-"))
num2=int(input("Enter the value 2:-"))
opr=input("Enter the operator .. +,-,*,/ :-")

if opr=="+":
    print(num1+num2)
if opr=="-":
    print(num1-num2)
if opr=="*":
    print(num1*num2)
if opr=="/":
    print(num1/num2)
if opr!="+" and opr!="-" and opr!="*" and opr!="/":
    print("Invalid")