"""
Adventure Game - Text-Based Interactive Quest
===============================================
A text-based adventure game built with Python and GitHub Copilot.

This module implements an interactive command-line adventure game where players
navigate through various locations, make strategic decisions, and attempt to find
a legendary treasure. The game uses functions, conditionals, and loops to create
an engaging, replayable experience.

Author: Created with GitHub Copilot assistance
Date: 2024
Purpose: Practice Python fundamentals (variables, functions, conditionals, loops)
"""

# Global variables to track game state
player_name = ""
game_active = True


def display_intro():
    """
    Display the game introduction and welcome message.
    
    This function prints an ASCII-art style banner and explains the objective
    of the adventure game to the player.
    
    Returns:
        None
    """
    print("\n" + "="*60)
    print("     WELCOME TO THE LEGENDARY TREASURE QUEST")
    print("="*60)
    print("\nYou stand at the edge of an ancient, mysterious land.")
    print("Legends speak of a legendary treasure hidden somewhere")
    print("in the depths of forgotten locations.")
    print("\nYour mission: Navigate through challenges, make wise choices,")
    print("and find the treasure to complete your quest!")
    print("\nBut beware! Not all paths lead to glory...")
    print("-"*60 + "\n")


def get_player_name():
    """
    Prompt the player for their name and validate input.
    
    This function asks the player to enter their name, validates that it's not empty,
    and returns the validated name for use throughout the game.
    
    Returns:
        str: The player's name
    """
    while True:
        name = input("What is your name, brave adventurer? ").strip()
        if name:
            return name
        else:
            print("Please enter a valid name to continue your adventure.\n")


def start_game():
    """
    Initialize and start the adventure game.
    
    This is the main entry point of the game. It displays the introduction,
    gets the player's name, and presents the initial choice between exploring
    a dark forest or entering a mysterious cave.
    
    The function uses a loop to allow the player to make their initial choice
    and routes them to the appropriate game path.
    
    Returns:
        None
    """
    global player_name, game_active
    
    display_intro()
    player_name = get_player_name()
    
    print(f"\nWelcome, {player_name}!")
    print(f"Your legend begins now...\n")
    
    # Initial choice presentation
    while True:
        print("You arrive at a crossroads. Two paths lie before you:")
        print("-" * 40)
        print("Path 1: A DARK FOREST")
        print("   A dense forest with ancient trees and mysterious sounds.")
        print("\nPath 2: A MYSTERIOUS CAVE")
        print("   A dark cave entrance glowing with strange ethereal light.")
        print("-" * 40)
        
        choice = input(f"\n{player_name}, which path do you choose? (1 or 2): ").strip()
        
        if choice == "1":
            forest_path()
            break
        elif choice == "2":
            cave_path()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")


def forest_path():
    """
    Handle the forest exploration sequence.
    
    This function presents the player with the forest scenario and offers
    two choices: following a river or climbing a tree. Each choice leads to
    a different outcome that affects the player's progress toward the treasure.
    
    Returns:
        None
    """
    global player_name, game_active
    
    print("\n" + "="*60)
    print("YOU ENTER THE DARK FOREST")
    print("="*60)
    print("\nAs you step into the forest, ancient trees loom overhead,")
    print("their gnarled branches creating a canopy of shadow.")
    print("The sound of running water echoes in the distance...")
    print("\nSuddenly, you hear a rustling sound and see a fork in the path.\n")
    
    while True:
        print("Choice 1: Follow the sound of the RIVER")
        print("   You spot what appears to be a river with strange markings on its banks.")
        print("\nChoice 2: Climb the TALLEST TREE to get a better view")
        print("   A massive oak tree stands before you, its branches sturdy and accessible.")
        
        choice = input(f"\n{player_name}, what do you do? (1 or 2): ").strip()
        
        if choice == "1":
            follow_river()
            break
        elif choice == "2":
            climb_tree()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")


def follow_river():
    """
    Handle the river exploration sequence (forest path - choice 1).
    
    The player follows the river and discovers an ancient stone map that
    points them toward the treasure location, leading them to victory.
    
    Returns:
        None
    """
    global player_name, game_active
    
    print("\n" + "-"*60)
    print("Following the River...")
    print("-"*60)
    print("\nYou carefully make your way along the river bank.")
    print("The water sparkles with an otherworldly glow.")
    print("\nAs you walk further, you discover an ancient stone archway")
    print("carved with mysterious symbols. Beneath it lies a weathered map!")
    print("\nYou examine the map closely:")
    print("  - It shows the location of the legendary treasure")
    print("  - There's a clear path marked with glowing runes")
    print("  - Your heart races with excitement!\n")
    
    # Ask if they want to follow the map
    while True:
        choice = input(f"{player_name}, do you follow the map to the treasure? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            win_game()
            game_active = False
            break
        elif choice in ["no", "n"]:
            print("\nYou hesitate and turn back, missing the opportunity of a lifetime.")
            lose_game()
            game_active = False
            break
        else:
            print("Please enter 'yes' or 'no'.\n")


def climb_tree():
    """
    Handle the tree climbing sequence (forest path - choice 2).
    
    The player climbs the tree but encounters a dangerous situation with
    aggressive creatures, leading to a loss scenario.
    
    Returns:
        None
    """
    global player_name, game_active
    
    print("\n" + "-"*60)
    print("Climbing the Tallest Tree...")
    print("-"*60)
    print("\nYou begin your ascent up the mighty oak tree.")
    print("The bark is rough beneath your hands, but you climb higher and higher.")
    print("\nAbout halfway up, you hear a low growl...")
    print("Suddenly, a family of TERRITORIAL EAGLES attacks!")
    print("\nYou lose your grip and tumble down...")
    print(f"Oh no, {player_name}! You've been defeated by nature's guardians!\n")
    
    lose_game()
    game_active = False


def cave_path():
    """
    Handle the cave exploration sequence.
    
    This function presents the cave scenario and offers two choices: lighting
    a torch or proceeding in the dark. Each choice leads to different outcomes
    that determine the player's success or failure.
    
    Returns:
        None
    """
    global player_name, game_active
    
    print("\n" + "="*60)
    print("YOU ENTER THE MYSTERIOUS CAVE")
    print("="*60)
    print("\nYou step into the cave and the sunlight quickly fades behind you.")
    print("The air is cool and damp. Strange symbols glow faintly on the walls.")
    print("The darkness seems almost alive, pressing against your senses.")
    print("\nOn the ground, you notice an old torch and a flint striker.\n")
    
    while True:
        print("Choice 1: Light the TORCH")
        print("   You could use the torch to see clearly, but it might alert any creatures within.")
        print("\nChoice 2: Proceed in the DARK")
        print("   Moving without light is risky, but you might remain undetected.")
        
        choice = input(f"\n{player_name}, what do you do? (1 or 2): ").strip()
        
        if choice == "1":
            light_torch()
            break
        elif choice == "2":
            proceed_dark()
            break
        else:
            print("Invalid choice. Please enter 1 or 2.\n")


def light_torch():
    """
    Handle the torch lighting sequence (cave path - choice 1).
    
    The player lights the torch and discovers a path deeper into the cave,
    but encounters a guardian that they must negotiate with, leading to a win.
    
    Returns:
        None
    """
    global player_name, game_active
    
    print("\n" + "-"*60)
    print("Lighting the Torch...")
    print("-"*60)
    print("\nYou strike the flint and the torch ignites with bright flames!")
    print("The cave is suddenly illuminated, revealing stunning crystal formations.")
    print("\nYou notice a GUARDIAN SPIRIT blocking the deeper passage.")
    print("It glows with an ethereal blue light and speaks to you:")
    print("\n  'Mortal, you have shown courage by facing the darkness with light.'")
    print("  'Few have earned the right to seek the treasure.'")
    print("  'You may pass, brave one!'\n")
    
    print("The guardian steps aside, revealing a passage deeper into the cave.")
    print("Following the path, you discover a GOLDEN CHEST!")
    print(f"Inside lies the legendary treasure, {player_name}!\n")
    
    win_game()
    game_active = False


def proceed_dark():
    """
    Handle the dark progression sequence (cave path - choice 2).
    
    The player attempts to navigate in the dark but gets lost and encounters
    an obstacle that ends the adventure unsuccessfully.
    
    Returns:
        None
    """
    global player_name, game_active
    
    print("\n" + "-"*60)
    print("Proceeding in Darkness...")
    print("-"*60)
    print("\nYou cautiously move forward, your hands outstretched.")
    print("You can hear water dripping and feel the walls getting narrower.")
    print("\nSuddenly, the ground beneath you gives way!")
    print("You fall into a hidden chasm and find yourself trapped.")
    print(f"\nUnfortunately, {player_name}, your adventure ends here.")
    print("Better luck next time...\n")
    
    lose_game()
    game_active = False


def win_game():
    """
    Display the victory message and congratulate the player.
    
    This function is called when the player successfully finds the treasure.
    It displays a celebratory message and invites the player to play again.
    
    Returns:
        None
    """
    print("="*60)
    print("🎉 CONGRATULATIONS! YOU FOUND THE TREASURE! 🎉")
    print("="*60)
    print(f"\n{player_name}, you have successfully completed your quest!")
    print("You have become a legend in the ancient land.")
    print("Your name will be remembered for generations to come!")
    print("\nThe treasure is now yours, and your adventure is complete.\n")


def lose_game():
    """
    Display the defeat message and sympathize with the player.
    
    This function is called when the player fails to complete the quest.
    It explains the outcome and offers the opportunity to try again.
    
    Returns:
        None
    """
    print("="*60)
    print("❌ QUEST FAILED ❌")
    print("="*60)
    print(f"\n{player_name}, your adventure has come to an end.")
    print("The treasure remains hidden, waiting for another brave soul.")
    print("But fear not! You can try again and learn from your mistakes.\n")


def play_again():
    """
    Ask the player if they want to play another round.
    
    This function prompts the player to decide whether to restart the game
    or exit the program. It handles input validation and returns the decision.
    
    Returns:
        bool: True if the player wants to play again, False otherwise
    """
    while True:
        choice = input("Would you like to play again? (yes/no): ").strip().lower()
        if choice in ["yes", "y"]:
            return True
        elif choice in ["no", "n"]:
            return False
        else:
            print("Please enter 'yes' or 'no'.\n")


def main():
    """
    Main game loop that controls overall game flow.
    
    This is the entry point of the program. It manages the game loop,
    allowing the player to play multiple times until they decide to quit.
    It also displays a farewell message when the game ends.
    
    Returns:
        None
    """
    global game_active
    
    # Continue running the game until the player decides to quit
    while True:
        game_active = True
        start_game()
        
        # Ask if the player wants to continue
        if not play_again():
            break
    
    print("\n" + "="*60)
    print("Thank you for playing the Adventure Game!")
    print("Farewell, brave adventurer!")
    print("="*60 + "\n")


# Entry point of the script
if __name__ == "__main__":
    main()
