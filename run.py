import pyfiglet
import random
import copy

# Global variables
records = [0, 0, 0]
player_score = 0
dealer_score = 0
player_hand = []
dealer_hand = []
playerIn = True
dealerIn = True


# Display welcome Message
result = pyfiglet.figlet_format("   Blackjack   ", font = "digital")
print(result)

# Initialize Deck
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 1
game_deck = copy.deepcopy(decks * one_deck)
#print(game_deck)

# Deal Cards
def deal_cards(turn):
    card = random.choice(game_deck)
    turn.append(card)
    game_deck.remove(card)
    return card


# Calculate Hand Value
def total(turn):
    total = 0
    for card in turn:
        if card.isdigit():
            total += int(card)
        elif card in ['J', 'K', 'Q']:
            total += 10
        else:
            if total > 11:
                total += 1
            else:
                total += 11
    return total


# Display Hands
def show_hand():
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]

# Game loop
for _ in range(2):
    deal_cards(dealer_hand)
    deal_cards(player_hand)

while playerIn or dealerIn:
    print(f"Dealer hand: {show_hand()} and X")
    print(f"Your hand: {player_hand} for a total of {total(player_hand)}")

    if playerIn:
        stay_hit = input("\nPress the key\n1 to Stay\n2 to Hit\n")
        if stay_hit == '1':
            print("\nYou STAND")
            playerIn = False
        else:
            print("\nYou HIT")
            deal_cards(player_hand)
            if total(player_hand) >= 21:
                playerIn = False
                break # End player's turn immediately on bust or reaching 21

    # Check if the player is no longer in the game (either by standing or busting)
    if not playerIn:
        # Dealer must hit if total is less than 17, according to Blackjack rules
        while total(dealer_hand) < 17:
            print("\nDealer HITs")
            deal_cards(dealer_hand)
            # Check after each hit if the dealer busts; if so, break immediately
            if total(dealer_hand) >= 21:
                break
        # After dealer acts, if they haven't busted, they're done
        dealerIn = False


# Determine Winner
if total(player_hand) == 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)}")
    print("Blackjack!")
elif total(dealer_hand) == 21:
    print(f"\nDealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Blackjack!")
elif total(player_hand) == 21 and total(dealer_hand) == 21:
    print("Tye Game!")
elif total(player_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)}")
    print(f"\nDealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You bust! Dealer Wins!")
elif total(dealer_hand) > 21:
    print(f"\nYou have {player_hand} for a total of {total(player_hand)}")
    print(f"\nDealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer busts! You Win")
elif total(dealer_hand) > total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)}")
    print(f"\nDealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("Dealer Wins!")
elif total(dealer_hand) < total(player_hand):
    print(f"\nYou have {player_hand} for a total of {total(player_hand)}")
    print(f"\nDealer has {dealer_hand} for a total of {total(dealer_hand)}")
    print("You Win!")


# Update Bankroll
