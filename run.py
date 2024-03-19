import pyfiglet
import random
import copy
import os
import time
from colorama import just_fix_windows_console, Fore, Back, Style
just_fix_windows_console()


# Global variables
player_hand = []
dealer_hand = []
playerIn = True
dealerIn = True
bankroll = 1000
player_win = None
# Initialize Deck
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 1
game_deck = copy.deepcopy(decks * one_deck)


# Game Lobby
def enter_game():

    while True:
        result = pyfiglet.figlet_format("Welcome to Casino Royale", font="digital")
        colored_result = Back.GREEN + Fore.BLACK + Style.BRIGHT + result
        # Print the colored ASCII art
        print(colored_result)
        print("You are seated at a Blackjack table")
        play = input(f"\nEnter:\n1 to PLAY\n2 for Instructions\n")
        
        if play == '1':
            os.system('clear')
            main_game()
            return
        elif play == '2':
            os.system('clear')
            instructions()
            return
        else:
            os.system('clear')
            print(f"{play} is not a valid input please enter 1 or 2\n")
       

def instructions():
    print("\nHere are the rules:\n")
    print("1. Goal: Get cards that add up close to 21 without going over.")
    print("2. Card Values:")
    print("   - Number cards are worth their number.")
    print("   - Face cards (Jacks, Queens, Kings) are worth 10.")
    print("   - Aces can be 1 or 11.")
    print("3. Gameplay:")
    print("   - You get two cards to start.")
    print("   - You can 'hit' to get another card or 'stand' to keep your cards.")
    print("   - If your cards add up to more than 21, you lose ('bust').")
    print("   - The dealer also gets two cards and follows rules for hitting or standing. (Dealer stands on 17)")
    print("4. Winning:")
    print("   - If the dealer busts, you win automatically.")
    print("   - The one closest to 21 without going over wins.")
    print("   - If you get exactly 21, it's called a 'blackjack,' and you win")
    print("5. Tie Game:")
    print("   - If you and the dealer have the same total, it's a tie, and you get your bet back.")
    while True:
        play = input(f"\nEnter:\n1 to PLAY\n2 Go to game Lobby\n")
        if play in ('1', '2'):
            os.system('clear')
            if play == '1':
                main_game()
            else:
                enter_game()
                return 
        else: 
            os.system('clear')
            print(f"{play} is not a valid input please enter 1 or 2\n")
            


# Deal Cards
def deal_cards(turn):
    global game_deck, one_deck

    if not game_deck:
        print("No cards left in the deck! Reshuffling ...")
        time.sleep(1.5)
        game_deck = copy.deepcopy(decks * one_deck)
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
def main_game():
    global player_hand, dealer_hand, playerIn, dealerIn, bankroll

    player_hand = []
    dealer_hand = []

    for _ in range(2):
        deal_cards(dealer_hand)
        deal_cards(player_hand)

    cards_left = len(game_deck)

    print(f"\nDealer has: {show_hand()} and X")
    print(f"You have: {player_hand} for a total of {total(player_hand)}")
    print(f"Bankroll: ${bankroll}")
    print(f"Cards left to deal: {cards_left}")

    if total(player_hand) == 21:
        check_winner()
        return

    while playerIn or dealerIn:

        if playerIn:
            stay_hit = input("\nEnter:\n1 to STAND\n2 to HIT\n")
            if stay_hit == '1':
                os.system('clear')
                print(f"\nYou STAND on {total(player_hand)}")
                print(f"\nDealer has {dealer_hand} for a total of {total(dealer_hand)}")
                playerIn = False
            elif stay_hit == '2':
                print("\nYou HIT")
                deal_cards(player_hand)
                time.sleep(1)
                print(f"\nYou have {player_hand} for a total of {total(player_hand)}")
                if total(player_hand) >= 21:
                    playerIn = False
                    break
            else:
                os.system('clear')
                print(f"{stay_hit} is not a valid input please enter 1 or 2\n")
                print(f"\nDealer has: {show_hand()} and X")
                print(f"You have: {player_hand} for a total of {total(player_hand)}")
                print(f"Bankroll: ${bankroll}")

        # Check if the player is no longer in the game (either by standing or busting)
        if not playerIn:
            # Dealer must hit if total is less than 17, according to Blackjack rules
            while total(dealer_hand) < 17:
                print("\nDealer HITs")
                deal_cards(dealer_hand)
                time.sleep(1)
                print(f"\nDealer has {dealer_hand} for a total of {total(dealer_hand)}")
                time.sleep(1)
                # Check after each hit if the dealer busts; if so, break immediately
                if total(dealer_hand) >= 21:
                    break
            # After dealer acts, if they haven't busted, they're done
            dealerIn = False
    check_winner()
    

# Determine Winner
def check_winner():
    global player_hand, dealer_hand, player_win
    if total(player_hand) == 21:
        print("\nBlackjack! You Win!")
        player_win = True
    elif total(dealer_hand) == 21:
        print("\nBlackjack! Dealer Wins!")
        player_win = False
    elif total(player_hand) > 21:
        print("\nYou bust! Dealer Wins!")
        player_win = False
    elif total(dealer_hand) > 21:
        print("\nDealer busts! You Win")
        player_win = True
    elif total(dealer_hand) > total(player_hand):
        print("\nDealer Wins!")
        player_win = False
    elif total(dealer_hand) < total(player_hand):
        print("\nYou Win!")
        player_win = True
    elif total(player_hand) == total(dealer_hand):
        print("\nTie Game!")
    bet()
    reset_game()
    

# Reset Game
def reset_game():
    global player_hand, dealer_hand, playerIn, dealerIn, player_win
    while True: 
        deal = input("\nEnter:\n1 Deal\n2 Go to game Lobby\n")
        if deal == '1':
            player_hand = []
            dealer_hand = []
            playerIn = True
            dealerIn = True
            player_win = None
            os.system('clear')
            main_game()
            break
        elif deal == '2':
            os.system('clear')
            enter_game()
            break
        else:
            os.system('clear')
            print(f"{deal} is not a valid input please enter 1 or 2\n")

# Betting
def bet():
    global player_win, bankroll
    if player_win == True:
        bankroll += 100
        print("\nCongratulations! You won the bet.")
    elif player_win == False:
        bankroll -= 100
        print("\nYou lost the bet.")
    elif player_win == None:
        print("\nYour bet is returned.")
    print(f"Bankroll: ${bankroll}")


enter_game()

