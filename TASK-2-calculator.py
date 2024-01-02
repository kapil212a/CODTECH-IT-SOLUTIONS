def add (x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def division(x,y):
    if y !=0:
        return x/y
    else:
        return "not divide by zero"
    
    
def calculator():
    print("simple calculator")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")

    a=input("enter(1.For addition/2.For substract/3.For Multiply/4.Divide):")

    if a in ("1","2","3","4"):
        n1=float(input("Enter first number: "))
        n2=float(input("Enter second number:"))

        if a=='1':
            print(f"{n1}+{n2} = {add(n1,n2)}")
        elif a=='2':
            print(f"{n1}-{n2} = {subtract(n1),n2}")
        elif a=='3':
            print(f"{n1}*{n2} = {multiply(n1,n2)}")
        elif a=='4':
            print(f"{n1}/{n2} = {division(n1,n2)}")
        
        else:
            print("Not valid input.please enter a valid number")

    else:
        print("Not valid input.please enter a valid number")

if __name__ == "__main__":
    calculator()
        

        