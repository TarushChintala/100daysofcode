# import random
#
# def blackjack():
#
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
#     player = []
#
#     dealer = []
#
#     def hit(hand):
#         hand.append(random.choice(cards))
#         print("\nDrawing card...")
#
#     def ace(hand):
#         if 11 in hand and sum(hand) > 21:
#             hand[hand.index(11)] = 1
#
#     def display(p1, comp):
#         print(f"\nDealer's hand is {comp}")
#         print(f"Your hand is {p1}\n")
#
#     hit(player)
#     hit(player)
#
#     hit(dealer)
#
#     proceed = True
#     while proceed:
#         if sum(player) >= 21:
#             proceed = False
#         else:
#             display(player,dealer)
#             choice = input("Hit? or Stand?\n").lower()
#             if choice == "hit":
#                 hit(player)
#                 ace(player)
#             else:
#                 proceed = False
#
#     game = True
#
#     if sum(player) == 21:
#         display(player,dealer)
#         print("Blackjack! Player wins!")
#         game = False
#     elif sum(player) > 21:
#         display(player,dealer)
#         print("Bust! Player Loses!")
#         game = False
#
#     if game:
#
#         display(player,dealer)
#
#         while sum(dealer) < 17:
#             hit(dealer)
#             ace(dealer)
#             display(player,dealer)
#
#         if sum(dealer) == 21:
#             display(player,dealer)
#             print("Blackjack! Dealer wins!")
#             game = False
#         elif sum(dealer) > 21:
#             display(player,dealer)
#             print("Bust! Dealer Loses!")
#             game = False
#
#     if game:
#         player_diff = 21 - sum(player)
#         dealer_diff = 21 - sum(dealer)
#         if player_diff < dealer_diff:
#             print("Player wins")
#         elif dealer_diff < player_diff:
#             print("Dealer wins")
#         else:
#             print("Its a Draw")
#
# play = True
#
# while play:
#     start = input("Would you like to play a game of blackjack? y for yes, n for no\n")
#     if start == "n":
#         play = False
#     else:
#         blackjack()



import random
from art import logo


def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def score(card_list):
    if 11 in card_list and sum(card_list) > 21:
        card_list[card_list.index(11)] = 1

    return sum(card_list)

def compare(p_score,d_score):
    if p_score == d_score:
        return "Its a draw"
    elif d_score == 21:
        return "Dealer has a blackjack! You Lose"
    elif p_score == 21:
        return "Blackjack! You Win"
    elif p_score > 21:
        return "Bust! You Lose"
    elif d_score > 21:
        return "Dealer goes over! You Win"
    elif p_score > d_score:
        return "You Win!"
    elif d_score > p_score:
        return "You Lose!"


def blackjack():
    player_cards = []
    player_score = -1
    dealer_cards = []
    dealer_score = -1

    for i in range(0,2):
        player_cards.append(deal())
        dealer_cards.append(deal())

    game = True
    while game:

        player_score = score(player_cards)
        dealer_score = score(dealer_cards)

        print(f"Your cards are {player_cards} and your score is {player_score}")
        print(f"The dealer's known card is {dealer_cards[0]}")

        if player_score == 21 or dealer_score == 21 or player_score > 21:
            game = False
        elif input("Hit or Stand?\n").lower() == "hit":
            player_cards.append(deal())
            player_score = score(player_cards)
        else:
            game = False

    while dealer_score !=21 and dealer_score < 17:
        dealer_cards.append(deal())
        dealer_score = score(dealer_cards)

    print(f"Your cards are {player_cards} and your score is {player_score}")
    print(f"The dealer's cards are {dealer_cards} and dealer's score is {dealer_score}\n")
    print(compare(player_score,dealer_score))

while input("Would you like to play a game of blackjack? y for yes n for no\n").lower() == "y":
    print("\n" * 20)
    print(logo)
    blackjack()