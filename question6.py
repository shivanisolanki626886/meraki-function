def add(num1,num2):
    print(num1+num2)
    return
def sub(num1,num2):
    print(num1-num2)
    return
def multiple(num1,num2):
    print(num1*num2)
    return
def divide(num1,num2):
    print(num1/num2)
    return
print("add")
print("sub")
print("mul")
print("divide")
num1=int(input("enter first value"))
num2=int(input("enter second value"))
choice=int(input("enter your choice.1/2/3/4"))
if choice==1:
    add(num1,num2)
elif choice==2:
    sub(num1,num2)
elif choice==3:
    multiple(num1,num2)
elif choice==4:
    divide(num1,num2)
else:
    print("wrong choice")
add(25,20)
sub(90,23)
multiple(50,60)
divide(80,120)









