'''
Q18: Happy Numbers - A happy number is defined by the following process. 
Starting with any positive integer, replace the number by the sum of the squares of its digits, 
and repeat the process until the number equals 1 (where it will stay), 
or it loops endlessly in a cycle which does not include 1. 
Those numbers for which this process ends in 1 are happy numbers, 
while those that do not end in 1 are unhappy numbers. 
Display an example of your output here. Find first 8 happy numbers.
'''
import math
def find_happy_num():
    happy_num = []
    
    for i in range(1,200):
        i = str(i)
#         print(f'I am {i}')
        happy_number = int(i)
        temp = []
        while True:
            count = 0
            for index in range(len(i)):
                count = count + int(i[index]) ** 2
            num = count
#             print(num)
            temp.append(num)
            if temp[-1] == 1:
#                 print("This is a happy number")
                happy_num.append(happy_number)
                break
            else:
                # i has been CHANGED!
                i = str(num)
                if len(temp) > 30:
                    break
        if len(happy_num) == 8:
            return happy_num

if __name__ == '__main__':
    first_8_happy_num = find_happy_num()
    print(f'The first eight happy numbers are: {first_8_happy_num}')