val = input("Please enter a number: ")

try:
    v = int(val)
except:
    v = -1

if(v != -1):
    print("This is a true number")
else:
    print("Please enter a real number again")
