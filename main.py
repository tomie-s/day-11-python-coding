from replit import clear
import random
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  return random.choice(cards)

def calculate_score(cards):
    if len(cards) == 2 and sum(cards) == 21:#Hint 7
        return 0
    if 11 in cards and sum(cards) > 21:#Hint 8
        cards.remove(11)
        cards.append(1)
        #return sum(cards)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        print("It's a draw")
    elif c_score == 0:
        print("Computer has a blackjack. You lose")
    elif u_score == 0:
        print("You have a blackjack. You win")
    elif u_score > 21:
        print("You went over. You lose")
    elif c_score > 21:
        print("Computer went over. You win")
    elif u_score > c_score:
        print("You win")
    else:
        print("You lose")

def play_blackjack():
    print(logo)
    
    user_cards = []
    computer_cards = []
    
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    user_playing = True #Hint 11
    
    while user_playing:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
    
        print(f"Your cards are: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")
        
        if user_score == 0 or computer_score == 0 or user_score > 21:
            user_playing = False #Hint 11
        else:
            continue_game = input("Do you want to draw another card? Type 'y' or 'n': ")#Hint 10
            if continue_game == "y":
                user_cards.append(deal_card())
            else:
                user_playing = False #Hint 11
    
    
    while computer_score < 17 and computer_score != 0:#Hint 12
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"Yours final hand: {user_cards}, final score: {user_score} \nComputer's final hand: {computer_cards}, final score: {computer_score}")
    
    compare(user_score, computer_score)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_blackjack()  
