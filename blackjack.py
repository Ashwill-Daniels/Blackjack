"""This is a blackjack card game. The user tries to get close to 21 
 without going bust while also going up against the dealer/computer.
 """

import random

user_score = []

# A card deck used to randomly pick from.
card_deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, "Ace"]

# The first card of the user.
user_score.append(random.choice(card_deck))

if "Ace" in user_score:
    user_score[0] = 11

# Holds the computer's cards.
dealer_score = []

# Build the computer's hand.
dealer_score.append(random.choice(card_deck))

# Make an appropriate decision for the computer. 
if "Ace" in dealer_score:
    dealer_score[0] = 11

dealer_score.append(random.choice(card_deck))

# Make an appropriate decision for the computer.
if "Ace" in dealer_score:
    dealer_score[1] = 1

print("Welcome to the Python Blackjack game!")

while True:
    

    user_input = (input(f"""Your hand: {user_score}
Will you 'hit' or 'stand'? """)).lower()
    
    # Add another card to the user's hand.
    if user_input =='hit':
        user_score.append(random.choice(card_deck))
        if "Ace" in user_score:
            while True:
                try:
                    user_choice = int(input("You drew an ace. Will you play \
it as a 1 or 11? "))
                    if user_choice == 1 or user_choice == 11:
                        if user_choice == 1:
                            user_score[-1] = 1

                        elif user_choice == 11:
                            user_score[-1] = 11

                        break
                    
                    else:
                        print("Please enter either '1' or '11'.")
                
                except ValueError:
                    print("Please enter either '1' or '11'.")

        elif sum(user_score) == 21:
            print("Blackjack! Your score is 21, you win!")
            break
        
        elif sum(user_score) > 21:
            print(f"Bust! Your final score is {sum(user_score)}")
            break

    # Compare the scores after the user finishes playing.   
    elif user_input == 'stand':
        if sum(user_score) > sum(dealer_score):
            print("Victory! You beat the dealer!")
            print(f"""Your final score is: {sum(user_score)}
The dealer's final score: {sum(dealer_score)}""")
            
        elif sum(user_score) < sum(dealer_score):
            print("Defeat! You were beaten by the dealer!")
            print(f"""Your final score is: {sum(user_score)}
The dealer's final score: {sum(dealer_score)}""")
            
        elif sum(user_score) == sum(dealer_score):
            print("A tie! Your final score and the dealer's score is the \
same!")
            print(f"""Your final score is: {sum(user_score)}
The dealer's final score: {sum(dealer_score)}""")
            
        break

    else:
        print("Please enter 'hit' or 'stand'.")