# Asking for input from user
def main():
    a=input("Enter the expression: ")
    if a == "X" or a == "x":
        exit
         
    elif " " not in a:
        factorial_res=factorial(float(a))
        print("Factorial of",a,"is",factorial_res)
    
    else:
        x,y,z=a.split(" ")
        if y == "+":
            Sum(x,z)
        elif y == "-":
            Sub(x,z)
        elif y == "*":
            Multiply(x,z)
        elif y == "/":
            Divide(x,z)
        elif y == "**":
            Exponential(x,z)
        elif y == "//":
            Floor_Divide(x,z)
        elif y == "%":
            Modulus(x,z)
        else:
            print("Wrong operator given")

# Now will make a normal calculator

def Sum(x,z):
        print("Addition of",x,"and",z,"is",float(x) + float(z))

def Sub(x,z):

        print("Subtraction of",x,"and",z,"is",float(x) - float(z))

def Multiply(x,z):

        print("Multiplication of",x,"and",z,"is",float(x) * float(z))

def Divide(x,z):
    if z != 0:
        print("Division of",x,"and",z,"is",float(x) / float(z))
    else:
        print("Undefined")
        
        
def Modulus(x,z):
    if z != 0:
        print("Remainder of",x,"and",z,"is",float(x) % float(z))
    else:
        print("Undefined")

    
def Exponential(x,z):

        print("Exponential of",x,"and",z,"is",float(x) ** float(z))


def Floor_Divide(x,z):
    if z != 0:
        print("GIF of",x,"and",z,"is",float(x) // float(z))
    else:
        print("Undefined")

def factorial(x):
    if x < 0:
        exit

    else:   
        return 1 if x == 0 or x == 1 else x*factorial(x-1)
    
main()