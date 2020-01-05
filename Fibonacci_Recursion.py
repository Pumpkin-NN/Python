# Use the recursion
output = []
def fibonacci(a, b):
    # Stop Condition
    if a>55:
#         print(output)
        return output
    
    output.append(a)
    
    a, b = b, a+b
    
    # TODO Study the Recursion Concept
    # Recursion
    return fibonacci(a, b)

    
if __name__ == '__main__':
#     fibonacci(1, 1)
    fibonacci_list = fibonacci(1, 1)
    print(fibonacci_list)