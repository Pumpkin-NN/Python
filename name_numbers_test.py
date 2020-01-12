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
    spell_number_list = [number_to_english(x) for x in n]
    
    def one_digit_number(n):
        return n
    def two_digit_number(t, n, List):
        if List[0] == 'One' and t == len(List) - 1:
            if List[1] == 'Zero':
                print("Ten")
            elif List[1] == 'One':
                print("Eleven")
            elif List[1] == 'Two':
                print("Twelve")
            elif List[1] == 'Three':
                print("Thirteen")
            elif List[1] == 'Five':
                print("Fifteen")
            elif List[1] == 'Eight':
                print("Eighteen")
            else:
                print(n+'teen')
        elif List[0] == 'Two' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Twenty")
            else:
                print("Twenty-"+n)
        elif List[0] == 'Three' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Thirty")
            else:
                print("Thirty-"+n)
        elif List[0] == 'Five' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Fifty")
            else:
                print("Fifty-"+n)
        elif List[0] == 'Eight' and t == len(List) - 1: 
            if List[1] == 'Zero':
                print("Eighty")
            else:
                print("Eighty-"+n)
        elif t == len(List) - 1 and List[0] != 'Zero':
            if List[1] == 'Zero':
                print(List[0]+"ty")
            else:
                print(List[0]+"ty"+"-"+n)
    def three_digit_number(t, n, List):
        if t == len(List) - 1 and List[1] == "Zero" and List[-1] == "Zero":
            print(List[0]+"-hundred")
        elif t == len(List) - 1 and List[1] == "Zero":
            print(List[0]+"-hundred"+" and " + one_digit_number(List[-1]))
        elif t == len(List) - 1:
            print(List[0]+"-hundred"+" and ")
            two_digit_number(t-1, n, List[1:])
    def four_digit_number(t, n, List):
        if t == len(List) - 1 and List[1] == "Zero" and List[2] == "Zero" and List[-1] == "Zero":
            print(List[0]+"-thousand")
        elif t == len(List) - 1 and List[1] == "Zero":
            if List[2] == "Zero":
                print(List[0]+"-thousand"+" and " + one_digit_number(List[-1]))
            else:
                print(List[0]+"-thousand"+" and ")
                two_digit_number(t-2, n, List[2:])
        elif t == len(List) - 1:
            print(List[0]+"-thousand"+" and ")
            three_digit_number(t-1, n, List[1:])
    def five_digit_number(t, n, List):
        List1 = List[:2]
        List2 = List[2:]
        print(List1, List2)
        if t == len(List) - 1:
            two_digit_number(t-3, List1[-1], List1)
            print("-thousand")
            if List2[0] == 'Zero' and List2[1] == 'Zero':
                print("and " + one_digit_number(List2[-1]))
            elif List2[0] == 'Zero':
                print("and ")
                two_digit_number(t-3, List2[-1], List2[1:])
            else:
                print("and ")
                three_digit_number(t-2, n, List2)
    def six_digit_number(t, n, List):
        List1 = List[:3]
        List2 = List[3:]
        print(List1, List2)
    
    
    
    
    
    
    
    
    
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






if __name__ == '__main__':
    n = '728990'
    spell_number(n)














