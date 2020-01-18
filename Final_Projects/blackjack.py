import random

MONEY = 200

#Create a DESK
DESK = [2,2,2,2,
        3,3,3,3,
        4,4,4,4,
        5,5,5,5,
        6,6,6,6,
        7,7,7,7,
        8,8,8,8,
        9,9,9,9,
        10,10,10,10,
        'JACK','JACK','JACK','JACK',
        'QUENE','QUENE','QUENE','QUENE',
        'KING','KING','KING','KING',
        'A','A','A','A']

class HumanPlayer():
    def __init__(self, money):
        self.money = money
    def hit(self):
        return random.choice(DESK)


class ComputerDealer():
    def __init__(self, money):
        self.money = money
    def hit(self):
        return random.choice(DESK)

def sum_cards(cards):
    count_list = []
    for i in cards:
        if i == 'A' and i != cards[-1]:
            hold = cards[-1]
            cards[-1] = i
            i = hold
        count_list.append(i)
        
    count = 0
    for j in count_list:
        if j == 'JACK':
            j = 10
        if j == 'QUENE':
            j = 10
        if j == 'KING':
            j = 10
        if j == 'A':
            if count <= 10:
                j = 11
            else:
                j = 1
        count = count + j
        
    '''
    # Another way to get the same result
    count = 0
    for j in count_list:
        if j == 'JACK':
            count = count + 10
        elif j == 'QUEEN':
            count = count + 10
        elif j == 'KING':
            count = count + 10
        elif j == 'A':
            if count <= 10:
                count = count + 11
            else:
                count = count + 1
        else:
            count = count + j
    return count
    '''
        
    return count

if __name__ == '__main__':
    Man = HumanPlayer(MONEY)
    Rot = ComputerDealer(MONEY)

    while True:
        cards_Man = []
        cards_Rot = []
        
        Round = 1
        hold = 0
        
        answer = input("Do you want to start a new game(Y/N)?\n")
        if answer == "N":
            break
        elif answer == "Y":
            while True: 
                print("\n\n*************************************************")
                print("The {} Round Begin!".format(Round))
                # The start of the game
                if len(cards_Man) == 0 and len(cards_Rot) == 0:
                    cards_Man.append(Man.hit())
                    cards_Man.append(Man.hit())
                    
                    cards_Rot.append(Rot.hit())
                    cards_Rot.append(Rot.hit())
                    print("\n\nThe first two cards for Man: \n{}".format(cards_Man))
                    print("The first two cards for Rot: \n{}".format(cards_Rot))
                # Check for the sum of the current cards from each beginning
                if sum_cards(cards_Man) > 21:
                    print("Human BUST!")
                    break
                if sum_cards(cards_Rot) > 21:
                    print("Rot BUST!")
                    break
                
                # Ask for the human player
                while True:
                    next_move = input("Do u want to 'HIT' or 'HOLD'?\n")
                    if next_move == 'HIT':
                        cards_Man.append(Man.hit())
                        print("The human cards are: {}".format(cards_Man))
                        break
                    elif next_move == 'HOLD':
                        hold = hold + 1
                        break
                    else:
                        print("Please Type in 'HIT' or 'HOLD'")
                    
                if sum_cards(cards_Man) > 21:
                    print("Human BUST!")
                    break

                if sum_cards(cards_Rot) < 18:
                    cards_Rot.append(Rot.hit())
                    print("The rot cards are: {}".format(cards_Rot))
                elif sum_cards(cards_Rot) > 21:
                    print("Rot BUST!")
                    break
                else:
                    hold = hold + 1

                if hold >= 3:
                    print("This Round ends.")
                    break
                
                Round = Round + 1

            if sum_cards(cards_Rot) > 21:
                print("Human wins!")
                Man.money = Man.money + Rot.money/2
                Rot.money = Rot.money - Rot.money/2
                print("The Man now have ${}".format(Man.money))
            elif sum_cards(cards_Man) > 21:
                print("Rot wins!")
                Rot.money = Rot.money + Man.money/2
                Man.money = Man.money - Man.money/2
                print("The Rot now have ${}".format(Rot.money))
            else:
                if sum_cards(cards_Rot) > sum_cards(cards_Man):
                    print("Rot wins!")
                    Rot.money = Rot.money + Man.money/2
                    Man.money = Man.money - Man.money/2
                    print("The Rot now have ${}".format(Rot.money))
                elif sum_cards(cards_Rot) < sum_cards(cards_Man):
                    print("Human wins!")
                    Man.money = Man.money + Rot.money/2
                    Rot.money = Rot.money - Rot.money/2
                    print("The Man now have ${}".format(Man.money))
                else:
                    print("Tied!")
        else:
            print("Please Type in 'Y' or 'N'\n\n")