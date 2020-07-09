import math
# Feel free to code your definitions here in order to separate your concerns.
num1 = 0
num2 = 0

def get_numbers():
    global num1, num2
    num1 = float(input("What is the first number? "))
    num2 = float(input("What is the second number? "))


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
def prime_number(n):
    ouput = [] 
    for i in range(n):
        output.append(i)
    holder = 2
    
    while (y) < x^(1/2): 

#nearest plane to you currently in the air
