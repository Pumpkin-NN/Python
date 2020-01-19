
# Use the recursion to calculate the exponetiation
m = 1
def fastExpo(a, b):
    global m
    m *= a
    if b == 1:
        return m
    return fastExpo(a, b-1)



# Main function
if __name__ == '__main__':
    a, b = input("Please enter the base a and the exponent b (format: a^b): \n").split("^")
    a = int(a)
    b = int(b)
    
    result = fastExpo(a, b)
    print(result)