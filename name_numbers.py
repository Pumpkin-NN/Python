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
        print(n)
    def two_digit_number(t, n):
        if spell_number_list[0] == 'One' and t == len(spell_number_list) - 1:
            if spell_number_list[-1] == 'Zero':
                print("Ten")
            elif spell_number_list[-1] == 'One':
                print("Eleven")
            elif spell_number_list[-1] == 'Two':
                print("Twelve")
            elif spell_number_list[-1] == 'Three':
                print("Thirteen")
            elif spell_number_list[-1] == 'Five':
                print("Fifteen")
            elif spell_number_list[-1] == 'Eight':
                print("Eighteen")
            else:
                print(n+'teen')
        elif spell_number_list[0] == 'Two' and t == len(spell_number_list) - 1: 
            if spell_number_list[-1] == 'Zero':
                print("Twenty")
            else:
                print("Twenty-"+n)
        elif spell_number_list[0] == 'Three' and t == len(spell_number_list) - 1: 
            if spell_number_list[-1] == 'Zero':
                print("Thirty")
            else:
                print("Thirty-"+n)
        elif spell_number_list[0] == 'Five' and t == len(spell_number_list) - 1: 
            if spell_number_list[-1] == 'Zero':
                print("Fifty")
            else:
                print("Fifty-"+n)
        elif spell_number_list[0] == 'Eight' and t == len(spell_number_list) - 1: 
            if spell_number_list[-1] == 'Zero':
                print("Eighty")
            else:
                print("Eighty-"+n)
        elif t == len(spell_number_list) - 1:
            if spell_number_list[-1] == 'Zero':
                print(spell_number_list[0]+"ty")
            else:
                print(spell_number_list[0]+"ty"+"-"+n)
    def three_digit_number(n):
        pass
    
    for k, i in enumerate(spell_number_list):
        if len(spell_number_list) == 1:
            one_digit_number(i)
        if len(spell_number_list) == 2:
            two_digit_number(k, i)
        if len(spell_number_list) == 3:
            pass








if __name__ == '__main__':
    n = '11'
    spell_number(n)














