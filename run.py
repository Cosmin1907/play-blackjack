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
bankroll = 10000
player_win = None
# Initialize Deck source: https://youtu.be/e3YkdOXhFpQ?si=sQLN16kWOC1zlaon
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
one_deck = 4 * cards
decks = 6
game_deck = copy.deepcopy(decks * one_deck)


# Game Lobby
def enter_game():
    """
    Initiate player's entry into Blackjack game.

    Display welcome message and game rules, allowing
    user to start game or view instructions.
    """
    while True:
        # Pyfiglet and colorama libraries create desired text output.
        result = pyfiglet.figlet_format("Welcome to Casino Royale",
                                        font="digital")
        colored_result = Back.GREEN + Fore.BLACK + Style.BRIGHT + result
        # Print the colored ASCII art
        print(colored_result)
        print("You are seated at a Blackjack table.")
        print("You will be credited with $10,000. Your standard bet is $100.")
        print("The game will be played with six decks of cards.")
        print("\nGood luck!")
        play = input(f"\nENTER:\n1 TO PLAY\n2 FOR GAME RULES\n")
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
    """
    Display Blackjack rules and options.

    Prompts the player to start game or return to lobby.
    """
    print("\nWelcome to the rules:\n")
    print("1. Goal: Get cards that add up close to 21 without going over")
    print("2. Card Values:")
    print("   - Number cards are worth their number")
    print("   - Face cards (Jacks, Queens, Kings) are worth 10")
    print("   - Aces can be 1 or 11. \
AA on first hand will be 12 for best odds")
    print("3. Gameplay:")
    print("   - You get two cards to start.")
    print("   - You can 'hit' to get another card or \
'stand' to keep your cards")
    print("   - If your cards add up to more than 21, you lose ('bust')")
    print("   - The dealer also gets two cards hits till 17 and stands on 17")
    print("4. Winning:")
    print("   - If the dealer busts, you win automatically")
    print("   - The one closest to 21 without going over wins")
    print("   - If you get exactly 21, it's called a 'blackjack', \
and you win 1.5 your bet")
    print("5. Tie Game:")
    print("   - If you and the dealer tie ('push'), you get your bet back")
    while True:
        play = input(f"\nENTER:\n1 TO PLAY\n2 GO TO GAME LOBBY\n")
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


# Deal Cards adapted for the game needs
# Source: https://youtu.be/mpL0Y01v6tY?si=GiW_qSq1gvqj7F58
def deal_cards(turn):
    """
    Deal a card to the player's hand.

    Parameters
    ----------
    turn : list
        The player's hand.

    Returns
    -------
    str
        The card that was dealt.
    """
    global game_deck, one_deck

    if not game_deck:
        print("No cards left in the deck! Reshuffling ...")
        time.sleep(1.5)
        game_deck = copy.deepcopy(decks * one_deck)
    card = random.choice(game_deck)
    turn.append(card)
    game_deck.remove(card)
    return card


# Calculate Hand Value, modified for game needs
# Source: https://youtu.be/mpL0Y01v6tY?si=GiW_qSq1gvqj7F58
def total(turn):
    """
    Calculate the total value of the player's hand.

    Parameters
    ----------
    turn : list
        The player's hand.

    Returns
    -------
    int
        The total value of the player's hand.
    """
    total = 0
    num_aces = 0
    for card in turn:
        if card.isdigit():
            total += int(card)
        elif card in ['J', 'K', 'Q']:
            total += 10
        elif card == 'A':
            num_aces += 1
            if total > 11:
                total += 1
            else:
                total += 11
        if num_aces == 2 and total > 21:
            total -= 10
    return total


# Display Hands
# Source: https://youtu.be/mpL0Y01v6tY?si=GiW_qSq1gvqj7F58
def show_hand():
    """
    Display the dealer's hand.

    Returns
    -------
    If the dealer has two cards, returns the first card.
    If the dealer has more than two cards, returns the first two cards.
    """
    if len(dealer_hand) == 2:
        return dealer_hand[0]
    elif len(dealer_hand) > 2:
        return dealer_hand[0], dealer_hand[1]


# Game loop, some sections of the code were borrowed
# Source: https://youtu.be/mpL0Y01v6tY?si=GiW_qSq1gvqj7F58
def main_game():
    """
    Run the main game logic.

    Actions:
    - Initialize the player's and dealer's hands with two cards each.
    - Display the dealer's visible card and the player's hand.
    - Prompt the player to hit or stand.
    - Implement the hitting mechanism for the dealer.
    - Check for a winner after the initial hand deal
    and after the player and dealer play.
    """
    global player_hand, dealer_hand, playerIn, dealerIn, bankroll

    player_hand = []
    dealer_hand = []
    playerIn = True
    dealerIn = True
    player_win = None

    for _ in range(2):
        deal_cards(dealer_hand)
        deal_cards(player_hand)

    cards_left = len(game_deck)

    print(f"\nDealer has: {show_hand()} and X")
    print(f"You have: {player_hand} for a total of {total(player_hand)}")
    print(f"Bankroll: ${bankroll}")
    print(f"Cards left to deal: {cards_left}")

    # check if the player has 21 on the first hand
    if total(player_hand) == 21:
        print("Roo Check winner")
        check_winner()
        print("Roo Check Winner End")
        return

    while playerIn or dealerIn:

        if playerIn:
            stay_hit = input("\nENTER:\n1 TO STAND\n2 TO HIT\n")
            if stay_hit == '1':
                os.system('clear')
                print(f"\nYou STAND on {total(player_hand)}")
                print(f"\nDealer has {dealer_hand} for a total \
of {total(dealer_hand)}")
                playerIn = False
            elif stay_hit == '2':
                print("\nYou HIT")
                deal_cards(player_hand)
                time.sleep(1)
                print(f"\nYou have {player_hand} for a total \
of {total(player_hand)}")
                if total(player_hand) >= 21:
                    playerIn = False
                    break
            else:
                os.system('clear')
                print(f"{stay_hit} is not a valid input please enter 1 or 2\n")
                print(f"\nDealer has: {show_hand()} and X")
                print(f"You have: {player_hand} for a total \
of {total(player_hand)}")
                print(f"Bankroll: ${bankroll}")

        # Check if the player is no longer in the game
        if not playerIn:
            # Dealer must hit if total is less than 17
            while total(dealer_hand) < 17:
                print("\nDealer HITs")
                deal_cards(dealer_hand)
                time.sleep(1)
                print(f"\nDealer has {dealer_hand} for a total \
of {total(dealer_hand)}")
                time.sleep(1)
                # Check after each hit if the dealer busts
                if total(dealer_hand) >= 21:
                    break
            # After dealer acts, if they haven't busted, they're done
            dealerIn = False

    check_winner()


# Determine Winner
# Source: https://youtu.be/mpL0Y01v6tY?si=GiW_qSq1gvqj7F58
def check_winner():
    """
    Checks for a winner and updates player status.
    """
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
    reset_game()
    bet()


# Reset Game
def reset_game():
    """
    Resets the game state or returns to the game lobby based on user input.
    """
    global player_hand, dealer_hand, playerIn, dealerIn, player_win
    while True:
        deal = input("\nENTER:\n1 DEAL\n2 GO TO GAME LOBBY\n")
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
    """
    Manages the player's bet and updates the bankroll.
    """
    global player_win, bankroll
    if player_win is True:
        if total(player_hand) == 21:
            bankroll += 150
        else:
            bankroll += 100
        print("\nCongratulations! You won the bet.")
    elif player_win is False:
        bankroll -= 100
        print("\nYou lost the bet.")
        if bankroll < 100:
            print("You are out of money, you are credited with another 10000$")
            bankroll = 10000
    elif player_win is None:
        print("\nYour bet is returned.")
    print(f"Bankroll: ${bankroll}")


enter_game()
