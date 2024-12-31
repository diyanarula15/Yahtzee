# Yahtzee Game 

A Python implementation of the scoring logic for the classic dice game **Yahtzee**. This program calculates scores for various Yahtzee categories based on the dice rolls provided as input.

## Features
- Calculate scores for all Yahtzee categories:
  - **Upper Section**: Aces, Twos, Threes, Fours, Fives, Sixes
  - **Lower Section**: 
    - Three of a Kind
    - Four of a Kind
    - Full House
    - Small Straight
    - Large Straight
    - Yahtzee
    - Chance
- Output scores for each category in a simple and clear format.

## How It Works
The program accepts a list of five dice rolls as input, evaluates the scores for all Yahtzee categories, and prints the results.

### Scoring Categories
1. **Aces, Twos, Threes, Fours, Fives, Sixes**: Sum of all dice matching the given number.
2. **Three of a Kind**: Sum of all dice if at least three have the same value.
3. **Four of a Kind**: Sum of all dice if at least four have the same value.
4. **Full House**: 25 points if there are three of one number and two of another.
5. **Small Straight**: 30 points for any sequence of four consecutive numbers.
6. **Large Straight**: 40 points for a sequence of five consecutive numbers.
7. **Yahtzee**: 50 points for five of the same number.
8. **Chance**: Sum of all dice values.

## Prerequisites
- Python 3.9 or higher.

## Installation
1. Clone this repository or download the source code.
2. Ensure Python is installed on your system.

## Usage
Run the program using the command line. Provide exactly 5 integers (representing dice rolls) as arguments.
Input:
python3 yahtzee.py 1 2 3 4 5
