import math
# Feel free to code your definitions here in order to separate your concerns.
num1 = 0
num2 = 0

def get_numbers():
    global num1, num2
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))
def singleinput():
    global num1
    num1 = int((input('single input here plox')))

def add():
    global num1, num2
    get_numbers()
    sum = num1 + num2
    print(str(num1) + " + " + str(num2) + " = " + str(sum))


def subtract():
    global num1, num2
    get_numbers()
    sum = num1 - num2
    return(str(num1) + " - "+ str(num2) + " = " + str(sum))

def multiply():
    global num1, num2
    get_numbers()
    sum = num1 * num2
    return(str(num1) + " * "+ str(num2) + " = " + str(sum))

def divide():
    global num1, num2
    get_numbers()
    if(num1 == 0 or num2 == 0):
        return("No singularities please thank you")
    sum = num1 / num2
    return(str(num1) + " / "+ str(num2) + " = " + str(sum))

def simple():
    runthis = input('input math normally, for ex 4 + 4')
    return(eval(runthis))

#average
#remainder 
#distance between points
#power
#convert between decimal fraction 
#convert hex binary and decimal
#quadratic formula
#all prime numbers from 0  to n
def prime_number():
    global num1
    singleinput()
    n = num1
    output = [] 
    for i in range(n):
        output.append(True)   
    for i in range(2, math.floor(n**(1/2))):
        if(output[i]):
            otherhold = 0
            while(((i **2 ) + (i * otherhold))< n):
                j = i**2
                j = j + i * otherhold
                output[j] = False
                otherhold += 1
    realoutput = []
    for idx, i in enumerate(output):
        if(i):
            realoutput.append(idx)
    return(realoutput)


    
    


#nearest plane to you currently in the air
