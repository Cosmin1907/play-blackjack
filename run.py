import pyfiglet
import random
import copy


# Display welcome Message
result = pyfiglet.figlet_format("Blackjack", font = "digital")
print(result)

# Initialize Deck
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 1
game_deck = copy.deepcopy(decks * one_deck)
print(game_deck)

# General variables
records = [0, 0, 0]
player_score = 0
dealer_score = 0
player_hand = []
dealer_hand = []

# Deal Cards
def deal_cards(turn):
    card = random.choice(game_deck)
    turn.append(card)
    game_deck.remove(card)
    print(card)


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
    print(total)


# Hit

# Stand

# Check Bust

# Determine Winner
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

print(dealer_hand)
print(player_hand)

# Update Bankroll


total(dealer_hand)
total(player_hand)