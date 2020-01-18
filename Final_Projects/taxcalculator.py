# Tax Calculator
# Asks the user to enter a cost and either a country or state tax.
# It then returns the tax plus the total cost with tax.

def tax_calculator(c, t):
    return c * t + c

if __name__ == "__main__":
    cost = int(input("Please enter a cost: \n"))
    tax = float(input("Please enter a tax rate (Format: 0.xx): \n"))
    tax = round(tax, 2)
    
    total = tax_calculator(cost, tax)
    print(f'The total is: {total}')