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
        
    return count

if __name__ == '__main__':
    Man = HumanPlayer(MONEY)
    Rot = ComputerDealer(MONEY)

    cards_Man = []
    cards_Rot = []
    
    Round = 1
    hold = 0
    while True: 
        # The start of the game
        if len(cards_Man) == 0 and len(cards_Rot) == 0:
            cards_Man.append(Man.hit())
            cards_Man.append(Man.hit())

            cards_Rot.append(Rot.hit())
            cards_Rot.append(Rot.hit())
            print(cards_Man,cards_Rot)
        # Check for the sum of the current cards from each beginning
        if sum_cards(cards_Man) > 21:
            print("Human BUST!")
            break
        if sum_cards(cards_Rot) > 21:
            print("Rot BUST!")
            break
        
        print("The {} Round Begin!".format(Round))
        
        # Ask for the human player
        while True:
            next_move = input("Do u want to 'hit' or 'hold'?\n")
            if next_move == 'hit':
                cards_Man.append(Man.hit())
                print("The human cards are: {}".format(cards_Man))
                break
            elif next_move == 'hold':
                hold = hold + 1
                break
            else:
                print("Please Type in 'hit' or 'hold'")
             
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
