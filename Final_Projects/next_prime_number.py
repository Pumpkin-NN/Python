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
    if Fn+1 < Scale[0]:
        print("\n\tThe number is not in the scale!\n")
        return False
    
    if Flag == 'Y':
        
        for num in range(len(Scale)):
            
            # Check if it is the last item in the Scale
            if Scale[num] == Scale[-1] and Fn > Scale[-1]:
                print("There is no more prime numbers\n\n")
                return None
            
            if Scale[num] <= Fn:
                if Scale[num] == Fn:
                    if Scale[num] == Scale[-1]:
                        print("There is no more prime numbers\n\n")
                        return None
                    else:
                        NUM = Scale[num+1]
                        return NUM
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
    minimum, maximum = input("\n\nPlease type in the scale, for the mini to max(format: min-max): \n").split("-")
    minimum, maximum = int(minimum), int(maximum)
    scale = primeNumberScale(minimum, maximum)
    
    
    # Check for the "next number" condition.
    count = 0
    while True:
        if count == 0:
            while True:
                number = int(input("Please type a number in the scale: "))
                num = nextPrime('Y', scale, number)
                if num == False:
                    continue
                if num == None:
                    break
                else:
                    print(f'\n\t the next prime number is:{num}\n')
                    break
        if num == None:
            break
        
        else:
            # Check the typo
            while True:
                choose = input("Find the next prime number? (Y/N): ")
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
                print(f'\n\t the next prime number is:{num}\n')
        
        # choose == "N"      
        else:
            nextPrime(choose, scale, num)
            break
        count = count + 1
    
    