# Number Names
# Show how to spell out a number in English. 
# You can use a preexisting implementation or roll your own, 
# but you should support inputs up to at least one million 
# (or the maximum value of your language's default bounded integer type, if that's less). 
# Optional: Support for inputs other than positive integers 
# (like zero, negative integers, and floating-point numbers).

def number_to_english(num):
    if num == '0':
        return "Zero"
    if num == '1':
        return "One"
    if num == '2':
        return "Two"
    if num == '3':
        return "Three"
    if num == '4':
        return "Four"
    if num == '5':
        return "Five"
    if num == '6':
        return "Six"
    if num == '7':
        return "Seven"
    if num == '8':
        return "Eight"
    if num == '9':
        return "Nine"

def spell_number(n):
    # Create a spell_number list use the list comprehension
    spell_number_list = [number_to_english(x) for x in n]
    
    # Spell out number names less than ten million
    def one_digit_number(n):
        return n
    def two_digit_number(t, n, List):
        if List[0] == 'One' and t == len(List) - 1:
            if List[1] == 'Zero':
                print("Ten", end = " ")
            elif List[1] == 'One':
                print("Eleven", end = " ")
            elif List[1] == 'Two':
                print("Twelve", end = " ")
            elif List[1] == 'Three':
                print("Thirteen", end = " ")
            elif List[1] == 'Five':
                print("Fifteen", end = " ")
            elif List[1] == 'Eight':
                print("Eighteen", end = " ")
            else:
                print(n+'teen', end = " ")
        elif List[0] == 'Two' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Twenty", end = " ")
            else:
                print("Twenty-"+n, end = " ")
        elif List[0] == 'Three' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Thirty", end = " ")
            else:
                print("Thirty-"+n, end = " ")
        elif List[0] == 'Five' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Fifty", end = " ")
            else:
                print("Fifty-"+n, end = " ")
        elif List[0] == 'Eight' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Eighty", end = " ")
            else:
                print("Eighty-"+n, end = " ")
        elif t == len(List) - 1 and List[0] != 'Zero':
            if List[1] == 'Zero':
                print(List[0]+"ty", end = " ")
            else:
                print(List[0]+"ty"+"-"+n, end = " ")
    def three_digit_number(t, n, List):
        if t == len(List) - 1 and List[1] == "Zero" and List[-1] == "Zero":
            print(List[0]+"-hundred", end = " ")
        elif t == len(List) - 1 and List[1] == "Zero":
            print(List[0]+"-hundred"+" and " + one_digit_number(List[-1]), end = " ")
        elif t == len(List) - 1:
            print(List[0]+"-hundred"+" and", end = " ")
            two_digit_number(t-1, n, List[1:])
    def four_digit_number(t, n, List):
        if t == len(List) - 1 and List[1] == "Zero" and List[2] == "Zero" and List[-1] == "Zero":
            print(List[0]+"-thousand", end = " ")
        elif t == len(List) - 1 and List[1] == "Zero":
            if List[2] == "Zero":
                print(List[0]+"-thousand"+" and " + one_digit_number(List[-1]), end = " ")
            else:
                print(List[0]+"-thousand"+" and", end = " ")
                two_digit_number(t-2, n, List[2:])
        elif t == len(List) - 1:
            print(List[0]+"-thousand"+" and", end = " ")
            three_digit_number(t-1, n, List[1:])
    def five_digit_number(t, n, List):
        List1 = List[:2]
        List2 = List[2:]
        if t == len(List) - 1:
            two_digit_number(t-3, List1[-1], List1)
            print("-thousand", end = " ")
            if List2[0] == 'Zero' and List2[1] == 'Zero':
                print("and" + one_digit_number(List2[-1]), end = " ")
            elif List2[0] == 'Zero':
                print("and", end = " ")
                two_digit_number(t-3, List2[-1], List2[1:])
            else:
                print("and", end = " ")
                three_digit_number(t-2, n, List2)
    def six_digit_number(t, n, List):
        List1 = List[:3]
        List2 = List[3:]
        if t == len(List) - 1:
            three_digit_number(t-3, List1[-1], List1)
            print("-thousand", end = " ")
            if List2[0] == 'Zero' and List2[1] == 'Zero':
                if List2[-1] == 'Zero':
                    print("", end = " ")
                else:
                    print("and " + one_digit_number(List2[-1]), end = " ")
            elif List2[0] == 'Zero':
                print("and", end = " ")
                two_digit_number(t-4, List2[-1], List2[1:])
            else:
                print("and", end = " ")
                three_digit_number(t-3, n, List2)
    def seven_digit_number(t, n, List):
        List1 = List[:1]
        List2 = List[1:]
        if t == len(List) - 1:
            print(one_digit_number(List1[0])+"-million", end = " ")
            if List2[0] == 'Zero' and List2[1] == 'Zero' and List2[2] == 'Zero' and List2[3] == 'Zero' and List2[4] == 'Zero' and List2[5] == 'Zero':
                print("", end = " ")
            elif List2[0] == 'Zero' and List2[1] == 'Zero' and List2[2] == 'Zero' and List2[3] == 'Zero' and List2[4] == 'Zero':
                print("and " + one_digit_number(List2[-1]), end = " ")
            elif List2[0] == 'Zero' and List2[1] == 'Zero' and List2[2] == 'Zero' and List2[3] == 'Zero':
                print("and", end = " ")
                two_digit_number(t-5, n, List2[4:])
            elif List2[0] == 'Zero' and List2[1] == 'Zero' and List2[2] == 'Zero':
                print("and", end = " ")
                three_digit_number(t-4, n, List2[3:])
            elif List2[0] == 'Zero' and List2[1] == 'Zero':
                print("and", end = " ")
                four_digit_number(t-3, n, List2[2:])
            elif List2[0] == 'Zero':
                print("and", end = " ")
                five_digit_number(t-2, n, List2[1:])
            else:
                print("and", end = " ")
                six_digit_number(t-1, n, List2)     
            
    # Spell out number names more than ten million      
    def eight_digit_number(t, n, List):
        pass 
    def nine_digit_number(t, n, List):
        pass 
    def ten_digit_number(t, n, List):
        pass   
    def eleven_digit_number(t, n, List):
        pass
    
    for k, i in enumerate(spell_number_list):
        if len(spell_number_list) == 1:
            print(one_digit_number(i))
        if len(spell_number_list) == 2:
            two_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 3:
            three_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 4:
            four_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 5:
            five_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 6:
            six_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 7:
            seven_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 8:
            eight_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 9:
            nine_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 10:
            ten_digit_number(k, i, spell_number_list)
        if len(spell_number_list) == 11:
            eleven_digit_number(k, i, spell_number_list)

if __name__ == '__main__':
    # n less than ten million
    n = '9999999'
    print("Formatted Result: ")
    spell_number(n)
    print("")














