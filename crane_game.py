import pytest
import random
import sys

reset = "\033[0m" # Resets the colors used on the command line

# Used for each animal prize in the Prizes.txt file
class Animal:
    def __init__(self, name = None, sound = None, artist = None, color = "", appearance = ""):
        self.name = name
        self.sound = sound
        self.artist = artist
        self.color = color
        self.appearance = appearance

# Reads the animal prizes from the Prizes.txt file and adds them to the prizes array
def read_prize_data(prize_data):

    line_number = 0
    lines = prize_data.splitlines()

    prizes = []
    current_animal = Animal()
    while line_number < len(lines):
        line = lines[line_number]

        if "Animal: " in line:
            current_animal.name = line.split("Animal: ", 1)[1]
        elif "Sound: " in line:
            current_animal.sound = line.split("Sound: ", 1)[1]
        elif "Artist: " in line:
            current_animal.artist = line.split("Artist: ", 1)[1]
        elif "Color: " in line:
            current_animal.color = line.split("Color: ", 1)[1]
        elif line != "":
            current_animal.appearance += (line + "\n")
        elif line == "":
            current_animal.appearance = current_animal.appearance[:-1] # Removing the extra newline character
            prizes.append(current_animal)
            current_animal = Animal()

        line_number += 1

    return prizes

# Returns the location of the claw based on the sum of user inputs
def get_claw_location(user_input):

    moves_left = user_input.count('a')
    moves_right = user_input.count('d')
    claw_location = moves_right - moves_left

    # Makes sure the claw cannot go outside the bounds of the machine
    if claw_location > 2:
        claw_location = 2

    if claw_location < -2:
        claw_location = -2

    return claw_location

# Gets a random prize from the prizes array based on the amount of total prizes
def get_random_prize(prizes):
    random_prize = random.randrange(0, len(prizes))
    return prizes[random_prize]

# Increases the amount of prizes the player has won
def increase_count(prizes_won):
    prizes_won += 1
    return prizes_won

# Resets the amount of prizes the player has won
def reset_count(prizes_won):
    return 0

# Main function
if __name__ == "__main__":

    file = open("Prizes.txt")
    prize_data = file.read()
    prizes = read_prize_data(prize_data)
    file.close()

    prizes_won = 0

    print("Ready to play the crane game?")
    print("You win the crane game when you've received three prizes in a row.\n")
    print("Press \'A\' to move the claw left. Press \'D\' to move the claw right. Enter no more than four characters. Any other input will be disregarded.")
    print("To close the crane game, press X.")

    user_input = input("")
    while user_input.lower() != 'x':

        claw_location = get_claw_location(user_input.lower())

        # Determining where the user moved the claw to
        if claw_location < 0:
            print(f"\nYou moved {abs(claw_location)} spaces left.")
        elif claw_location > 0:
            print(f"\nYou moved {claw_location} spaces right.")
        else:
            print("\nYou did not move any spaces.")

        random_number = random.randrange(-2, 3) # There is a 20% chance of winning the crane game (-2, -1, 0, 1, 2)
        
        if random_number == claw_location:

            # If the player got a prize
            animal = get_random_prize(prizes)
            prizes_won = increase_count(prizes_won)

            print("Congrats! You won the " + animal.name + ". " + animal.sound + "\n")
            print(f"\033[{animal.color}m{animal.appearance}{reset}")
            print(f"\033[38;2;30;30;30mDesigned by: {animal.artist}{reset}\n")
            print(f"This is prize number {prizes_won} out of 3. Just {(3 - prizes_won)} more!");

            # If the player won the entire crane game
            if prizes_won == 3:
                print(f"\n\033[38;2;255;0;0mC\033[38;2;255;170;0mO\033[38;2;255;251;0mN\033[38;2;0;255;38mG\033[38;2;0;255;179mR\033[38;2;0;183;255mA\033[38;2;0;27;255mT\033[38;2;111;0;255mU\033[38;2;251;0;255mL\033[38;2;255;0;140mA\033[38;2;255;0;0mT\033[38;2;255;170;0mI\033[38;2;255;251;0mO\033[38;2;0;255;38mN\033[38;2;0;255;179mS\033[38;2;0;183;255m!{reset}")
                print(f"\033[38;2;255;251;0mYou've finally won the crane game! Great job!{reset}")
                prizes_won = reset_count(prizes_won)

        else:

            # If the player did not get a prize
            print("No prize this time! :(")
            prizes_won = reset_count(prizes_won)
            print("Your prize count has been reset to 0.")

        print("Want to play again? Press \'A\' to move the claw left. Press \'D\' to move the claw right. Enter no more than four characters. Any other input will be disregarded.")
        print("To close the crane game, press X.")
        user_input = input("")

    print("\nThanks for playing the crane game! Goodbye!")
    sys.exit()