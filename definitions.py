import math
# Feel free to code your definitions here in order to separate your concerns.

nums = []

def get_numbers(n = 2):
    global nums
    for i in range(n):
        nums.append(float(input("What is the " + str(i + 1) +" number?")))
    

    
def singleinput():
    global nums
    nums.append((float(input('single input here plox'))))

def add():
    global nums
    get_numbers()
    sum = nums[0] + nums[1]
    print(str(nums[0]) + " + " + str(nums[1]) + " = " + str(sum))


def subtract():
    global nums
    get_numbers()
    sum = nums[0] - nums[1]
    return(str(nums[0]) + " - "+ str(nums[1]) + " = " + str(sum))

def multiply():
    global nums
    get_numbers()
    sum = nums[0] * nums[1]
    return(str(nums[0]) + " * "+ str(nums[1]) + " = " + str(sum))

def divide():
    global nums
    get_numbers()
    if(nums[0] == 0 or nums[1] == 0):
        return("No singularities please thank you")
    sum = nums[0] / nums[1]
    return(str(nums[0]) + " / "+ str(nums[1]) + " = " + str(sum))

def simple():
    runthis = input('input math normally, for ex 4 + 4')
    return(eval(runthis))


#distance between points
def twopoint():
    global nums
    print('enter x1 then y1 then x2 then y2')
    get_numbers(4)
    sum = math.sqrt(((nums[2] - nums[0] ) ** 2 ) + ((nums[3] - nums[1] ) **2 )
        )
    return(sum)

#all prime numbers from 0  to n
def prime_number():
    global nums
    singleinput()
    n = int(nums[0])
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
