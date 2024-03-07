import pyfiglet
import random
import copy

# Display welcome Message
result = pyfiglet.figlet_format("Blackjack", font = "digital")
print(result)

# Initialize Deck
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 4
game_deck = copy.deepcopy(decks * one_deck)
print(game_deck)

# Shuffle Deck

# Deal Cards

# Calculate Hand Value

# Hit

# Stand

# Check Bust

# Determine Winner

# Display Hands

# Update Bankroll