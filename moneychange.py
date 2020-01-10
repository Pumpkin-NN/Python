# Change Return Program
# - The user enters a cost and then the amount of money given.
#The program will figure out the change and the number of quarters, dimes, nickels, pennies needed for the change.

def remainder_check(r, n):
    count = 0
    while True:
        r = round((r - n),2)
        count = count + 1
        if r < n:
            break
    return count

def count_change(r):
    if r >= 0.25:
        count = remainder_check(r, 0.25)
        print(f'The quarter(s) is(are): {count}')

        r = round((r - 0.25 * count),2)
        if r >= 0.10:
            count = remainder_check(r, 0.10)
            print(f'The dime(s) is(are): {count}')

            r = round((r - 0.10 * count),2)
            if r >= 0.05:
                count = remainder_check(r, 0.05)
                print(f'The nickel(s) is(are): {count}')

                r = round((r - 0.05 * count),2)
                if r >= 0.01:
                    count = remainder_check(r, 0.01)
                    print(f'The penny(s) is(are): {count}')
            elif r >= 0.01:
                count = remainder_check(r, 0.01)
                print(f'The penny(s) is(are): {count}')

        elif r >= 0.05:
            count = remainder_check(r, 0.05)
            print(f'The nickel(s) is(are): {count}')

            r = round((r - 0.05 * count),2)
            if r >= 0.01:
                count = remainder_check(r, 0.01)
                print(f'The penny(s) is(are): {count}')

        else:
            if r >= 0.01:
                count = remainder_check(r, 0.01)
                print(f'The penny(s) is(are): {count}')


    elif r >= 0.10:
        count = remainder_check(r, 0.10)
        print(f'The dime(s) is(are): {count}')

        r = round((r - 0.10 * count),2)
        if r >= 0.05:
            count = remainder_check(r, 0.05)
            print(f'The nickel(s) is(are): {count}')

            r = round((r - 0.05 * count),2)
            if r >= 0.01:
                count = remainder_check(r, 0.01)
                print(f'The penny(s) is(are): {count}')
        else:
            if r >= 0.01:
                count = remainder_check(r, 0.01)
                print(f'The penny(s) is(are): {count}')



    elif r >= 0.05:
        count = remainder_check(r, 0.05)
        print(f'The nickel(s) is(are): {count}')

        r = round((r - 0.05 * count),2)
        if r >= 0.01:
            count = remainder_check(r, 0.01)
            print(f'The penny(s) is(are): {count}')


    else:
        if r >= 0.01:
            count = remainder_check(r, 0.01)
            print(f'The penny(s) is(are): {count}')



def change(c, m):
    ce = round(m-c, 2)
    print(f'The total change is ${ce}')
    if ce // 1 != 0:
        print(f'The dollar(s) is(are): {int(ce // 1)}')
        r = round((ce - (ce // 1)), 2)
        if r != 0:
            count_change(r)
    else:
        print(f'The change dollar is :{0}')
        r = ce
        if r != 0:
            count_change(r)




if __name__ == '__main__':
    cost = float(input("Please enter a cost:\n"))
    amount = float(input("Please enter the amount of money given:\n"))
    change(cost, amount)
