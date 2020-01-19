# Next Prime Number
# Have the program find prime numbers until the user chooses to stop asking for the next one.


import math

def primeNumberScale(min, max):
    prime_list = []
    for num in range(min, max):
        if min == 0:
            num = num + 1
        for j in range(1, num):
            if math.gcd(j, num) != 1:
                break
            if j == num-1:
                prime_list.append(num)
    return prime_list


def nextPrime(Flag, Scale, Fn):
    if Flag == 'Y':
        
        for num in range(len(Scale)):
            
            # Check if it is the last item in the Scale
            if Scale[num] == Scale[-1]:
                print("There is no more prime numbers\n\n")
                return None
            
            if Scale[num] <= Fn:
                if Scale[num] == Fn:
                    return Scale[num+1]
                else:
                    continue
                
            else:
                NUM = Scale[num] 
                return NUM
    else:
        print("End of the search")
        return None

    return nextPrime(Flag, Scale, NUM)


if __name__ == '__main__':
    # Define the scale
    minimum, maximum = input("Please type in the scale, for the mini to max(format: min-max): \n").split("-")
    minimum, maximum = int(minimum), int(maximum)
    scale = primeNumberScale(minimum, maximum)
    
    
    # Check for the "next number" condition.
    count = 0
    while True:
        if count == 0:
            number = int(input("Please type a number in the scale: \n"))
            num = nextPrime('Y', scale, number)
            print(f'\t the next prime number is:{num}')
            
        # Check the typo
        while True:
            choose = input("Find the next prime number?(Y/N)\n")
            if choose == 'Y' or choose == 'N':
                break
            else:
                print("Please type in 'Y' or 'N'\n")
        
        # choose == "Y"
        if choose == "Y":
            num = nextPrime(choose, scale, num)
            if num == None:
                break
            else:
                print(f'\t the next prime number is:{num}')
        
        # choose == "N"      
        else:
            nextPrime(choose, scale, num)
            break
        count = count + 1
    
    