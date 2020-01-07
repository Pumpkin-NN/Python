# Prime Factorization
# 1. Have the user enter a number
# 2. Find all Prime Factors (if there are any) and display them

# Use Recursion

import math
def prime_num(n):
    prime_numbers = []
    for i in range(1, n+1):
        for j in range(2,i):
            if (i % j) == 0:
                break
        else:
            prime_numbers.append(i) 
    return prime_numbers


'''
Prime Factorization function
Input: int n
       list pn
Output: list prime_factor
'''
prime_factor = []
def prime_fac(n,pn):
    if n == 1:
        prime_factor.append(1)
        print("\n\nThe prime factors are: {}".format(prime_factor))
        return prime_factor
    else:
        for i in pn[1:]:
            if n % i == 0:
                prime_factor.append(i)
                r = n // i
                return prime_fac(r,pn)

'''
Main Fuction
'''    
if __name__ == '__main__':
    n = int(input("Please enter an arbitrary number: \n"))
    pn = prime_num(n)
    print("\n\nThe numbers are: {}".format(pn))
    pf = prime_fac(n,pn)
    print(pf)


'''
# Learnt some cool techs from the GFG web
import math
start = 1
end = 23

for val in range(start, end + 1): 
    if val > 1: 
        for n in range(2, val):
            # if (val % n) == 0:
            if math.gcd(val, n) != 1:
                break
        # Writing Style?
        else:
            print(val) 
'''
