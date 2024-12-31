from collections import Counter
import sys

YAHTZEE_PTS = 50
SMALL_STRAIGHT_PTS, LARGE_STRAIGHT_PTS = 30, 40
SMALL_STRAIGHT_LEN, LARGE_STRAIGHT_LEN = 4, 5
STRAIGHT_PTS = {SMALL_STRAIGHT_LEN: SMALL_STRAIGHT_PTS, 
                LARGE_STRAIGHT_LEN: LARGE_STRAIGHT_PTS}
FULL_HOUSE_FREQS = [3, 2]
FULL_HOUSE_PTS = 25


def _upper_house(dice: list[int], number: int) -> int:
    return sum(i for i in dice if i == number)

def aces(dice: list[int]) -> int:
    return _upper_house(dice, 1)

def twos(dice: list[int]) -> int:
    return _upper_house(dice, 2)

def threes(dice: list[int]) -> int:
    return _upper_house(dice, 3)

def fours(dice: list[int]) -> int:
    return _upper_house(dice, 4)

def fives(dice: list[int]) -> int:
    return _upper_house(dice, 5)

def sixes(dice: list[int]) -> int:
    return _upper_house(dice, 6)


def _n_of_a_kind(dice: list[int], n: int) -> int:
    dice_freqs = Counter(dice).most_common()
    val, max_count = dice_freqs[0]
    return sum(dice) if max_count >= n else 0

def three_of_a_kind(dice: list[int]) -> int:
    return _n_of_a_kind(dice, 3)

def four_of_a_kind(dice: list[int]) -> int:
    return _n_of_a_kind(dice, 4)


def yahtzee(dice: list[int]) -> int:
    return YAHTZEE_PTS if dice == [dice[0]] * len(dice) else 0


def _is_sublist_of(smaller: list[any], larger: list[any]) -> bool:
    return all(item in larger for item in smaller)

def _straight(dice: list[int], length: int) -> int:
    dice = sorted(dice)
    diffs = [b - a for a, b in zip(dice, dice[1:])]
    straight_diffs = [1] * (length - 1)
    has_straight = _is_sublist_of(straight_diffs, diffs)
    if not has_straight:
        return 0
    else:
        return STRAIGHT_PTS[length]

def small_straight(dice: list[int]) -> int:
    return _straight(dice, SMALL_STRAIGHT_LEN)

def large_straight(dice: list[int]) -> int:
    return _straight(dice, LARGE_STRAIGHT_LEN)


def full_house(dice: list[int]) -> int:
    top_two_freqs = [freq for val, freq in Counter(dice).most_common(2)]
    return FULL_HOUSE_PTS if top_two_freqs == FULL_HOUSE_FREQS else 0


def chance(dice: list[int]) -> int:
    return sum(dice)

CATEGORIES = [
    aces,
    twos,
    threes,
    fours,
    fives,
    sixes,
    three_of_a_kind,
    four_of_a_kind,
    yahtzee,
    full_house,
    small_straight,
    large_straight,
    chance
]

def category_scores(dice: list[int]) -> dict[str, int]:
    return {category.__name__: category(dice) for category in CATEGORIES}

def main():
    argc = len(sys.argv)
    if argc < 6:
        print("Usage: python3 yahtzee.py [dice 1] [dice 2] [dice 3] [dice 4] [dice 5]")
        return
    else:
        dice = [int(_) for _ in sys.argv[1:]]
        print(category_scores(dice))

main()