"""
BlackJack en Python
ASRBD 211 - Julien - Henri - Sammy
"""

#Random import module 
import random
from random import shuffle
import os
#Dictionary 
dict_Values = {'2♠': 2, '3♠': 3, '4♠': 4, '5♠': 5, '6♠': 6, '7♠': 7, '8♠': 8, '9♠': 9, '10♠': 10, 'J♠': 10, 'Q♠': 10, 'K♠': 10, '1♠': 11,
               '2♥': 2, '3♥': 3, '4♥': 4, '5♥': 5, '6♥': 6, '7♥': 7, '8♥': 8, '9♥': 9, '10♥': 10, 'J♥': 10, 'Q♥': 10, 'K♥': 10, '1♥': 11,
               '2♦': 2, '3♦': 3, '4♦': 4, '5♦': 5, '6♦': 6, '7♦': 7, '8♦': 8, '9♦': 9, '10♦': 10, 'J♦': 10, 'Q♦': 10, 'K♦': 10, '1♦': 11,
               '2♣': 2, '3♣': 3, '4♣': 4, '5♣': 5, '6♣': 6, '7♣': 7, '8♣': 8, '9♣': 9, '10♣': 10, 'J♣': 10, 'Q♣': 10, 'K♣': 10, '1♣': 11}

#This function creates the entire deck of 52 cards
def deckCreation():
    card_Types = ['♠','♥','♦','♣']
    card_Numbers = ['1','2','3','4','5','6','7','8','9','10','J','Q','K']
    deck = []

    for i in card_Types:
        for j in card_Numbers:
            deck.append(j+i)
    return deck

#This function draw 2 card
def drawCards():
    hand = [gameDeck.pop()]
    return hand

def playAgain():
    while True:
        choice = input("Do you want to play again ? (Y or N)")
        if choice.upper() == "Y":
            play = True
            os.system('clear')
            break
        elif choice.upper() == "N":
            play = False
            break
        else:
            print("Error please do choice again")
    return play


play = True

while play == True:
    #Preview of the generated deck 
    gameDeck = deckCreation()

    #Shuffle deck
    shuffle(gameDeck)

    #Draw cards to players
    player_hand = []
    dealer_hand = []
    player_hand += drawCards()
    dealer_hand += drawCards()
    player_hand += drawCards()
    dealer_hand += drawCards()

    #Calcule score
    playerScore = dict_Values[player_hand[0]] + dict_Values[player_hand[1]]
    dealerScore = dict_Values[dealer_hand[0]] + dict_Values[dealer_hand[1]]

    #Display board
    print("Dealer's hand : "+dealer_hand[0]+" + Returned card")
    print("Dealer's score : "+str(dict_Values[dealer_hand[0]]))
    print("Player's hand : "+player_hand[0]+" + "+player_hand[1])
    print("Player's score : "+str(playerScore))

    #Condition for test blackjack situationH
    if playerScore == 21:
        if dealerScore == 21:
            print("Blackjack for all players. Equality !")
            play = playAgain()
        else:
            print("Blackjack for you. You win !")
            play = playAgain()
    else:
        while True:
            choice = input("Enter H to Hit or S to Stand : ")
            if choice.upper() == 'H':
                player_hand += drawCards()
                playerScore += dict_Values[player_hand[-1]]
                print("You pick "+player_hand[-1])
                print("Your score is "+str(playerScore))
                if playerScore > 21:
                    print("You made "+str(playerScore)+" you lose")
                    play = playAgain()
                    break
                elif playerScore == 21:
                    while dealerScore < playerScore:
                        dealer_hand += drawCards()
                        dealerScore += dict_Values[dealer_hand[-1]]
                        print("Dealers pick "+str(dealer_hand[-1])+" this score is "+str(dealerScore))
                        if dealerScore > 21:
                            print("You win")
                            play = playAgain()
                            break
                        elif dealerScore > playerScore:
                            print("You lose")
                            play = playAgain()
                            break
            elif choice.upper() == 'S':
                print("Dealer's hand : "+str(dealer_hand[0])+" + "+str(dealer_hand[1]))
                while dealerScore <= playerScore:
                    dealer_hand += drawCards()
                    dealerScore += dict_Values[dealer_hand[-1]]
                    print("Dealers pick "+str(dealer_hand[-1])+" this score is "+str(dealerScore))
                if dealerScore > 21:
                    print("You win")
                    play = playAgain()
                    break
                elif dealerScore > playerScore:
                    print("You lose")
                    play = playAgain()
                    break
            else:
                print("Error please do choice again")