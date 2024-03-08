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

# Hit

# Stand

# Check Bust

# Determine Winner

# Display Hands

# Game loop

# Update Bankroll

deal_cards(player_hand)
deal_cards(dealer_hand)
print(game_deck)
