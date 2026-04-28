# IS 4010 Final Project: Crane Game
## Purpose
This command-line interface application simulates a crane game. Players can play the crane game by choosing how far they would like to move the claw left or right in order to receive a prize. The crane game machine has a width of four spaces, so players can only move up to two spaces left and up to two spaces right. Players must win three prizes in a row to win the crane game. There are seventeen possible, randomly-generated prizes that can be won, each of which has been designed by an artist on the [ASCII Art Archive](https://www.asciiart.eu/) and compiled into a `.txt` file for easy parsing.

## Installation
There are no dependencies that need to be installed before running the crane game. Installing `pytest` using `pip install pytest` is optional, as `pytest` is only used for testing purposes.

## Usage
The crane game can be played on the command-line by running `python crane_game.py`. 

To move the claw left, press 'A'. To move the claw right, press 'D'. You can press either key as many times as you like and in any order, but, ultimately, the claw can move no more than two spaces in any direction. Any other input will be disregarded. The total amount of spaces moved will be displayed after input is received. Some examples of this output are:

**Input:** `AA`
**Output:** `You moved 2 spaces left.`

**Input:** `D`
**Output:** `You moved 1 spaces right.`

**Input:** `AD`
**Output:** `You did not move any spaces.`

To close the command-line application, press 'X'.

## Examples
### Losing the crane game

### Winning the crane game
