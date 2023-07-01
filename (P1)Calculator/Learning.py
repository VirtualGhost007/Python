# Asking for input from user
a=int(input('Enter first number: '))
b=int(input('Enter second number: '))

# Now will make a normal calculator
def Sum(a,b):
    Ans1=a+b
    print('Sum of',a,'and',b,'is',Ans1)
def Sub(a,b):
    Ans2=a-b
    print('Subtraction of',a,'and',b,'is',Ans2)
def Multiply(a,b):
    Ans3=a*b
    print('Multiply of',a,'and',b,'is',Ans3)
def Divide(a,b):
    if (a==1):
        if (b==0):
            Ans4='Undefined'
            print('Division of',a,'and',b,'is',Ans4)
    else:
        Ans4=a/b
        print('Division of',a,'and',b,'is',Ans4)
        
def Modulus(a,b):
    if (a==1):
        if (b==0):
            Ans5='Undefined'
            print('Modulus of',a,'and',b,'is',Ans5)
    else:
        Ans5=a%b
        print('Modulus of',a,'and',b,'is',Ans5)
    
def Exponential(a,b):
    Ans6=a**b
    print('Exponential of',a,'and',b,'is',Ans6)
def Floor_Divide(a,b):
    if (a==1):
        if(b==0):
            Ans7='Undefined'
            print('Floor division of',a,'and',b,'is',Ans7)
    else:
        Ans7=a//b
        print('Floor division of',a,'and',b,'is',Ans7)


# Result output
print('Available operators are Add/add/Sub/sub/Multiply/multiply/Divide/divide/Modulus/modulus/Exponential/exponential/Floor division/floor division/floor/Floor')
c=input('Enter the operation to be performed: ')

def Operator(c):
    if  (c=='Add'):
        Sum(a,b)
    elif(c=='add'):
        Sum(a,b)
    elif(c=='Sub'):
        Sub(a,b)
    elif(c=='sub'):
        Sub(a,b)
    elif(c=='Multiply'):
        Multiply(a,b)
    elif(c=='multiply'):
        Multiply(a,b)
    elif(c=='Divide'):
        Divide(a,b)
    elif(c=='divide'):
        Divide(a,b)
    elif(c=='Modulus'):
        Modulus(a,b)
    elif(c=='modulus'):
        Modulus(a,b)
    elif(c=='Exponential'):
        Exponential(a,b)
    elif(c=='exponential'):
        Exponential(a,b)
    elif(c=='Floor divide'):
        Floor_Divide(a,b)
    elif(c=='floor divide'):
        Floor_Divide(a,b)
    elif(c=='Floor'):
        Floor_Divide(a,b)
    elif(c=='floor'):
        Floor_Divide(a,b)

Operator(c)