"""Exerccise 2: Wordle"""

__author__: str = "730737128"


def contains_char(word: str, character: str) -> bool:
    """This searches for a character in a word"""
    assert len(character) == 1, f"len('{character}') is not 1"
    idx: int = 0
    while idx < len(word):  # the loop iterates to see if character is somewhere in word
        if word[idx] == character:
            return True
        idx = idx + 1

    return False


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """This returns a string of emoji colors based on the contains_char function"""
    assert len(guess) == len(secret), "Guess must be the same length as secret"

    result: str = ""
    idx: int = 0

    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result = (
                result + GREEN_BOX
            )  # Letter in secret and guess are matching and at correct position
        elif contains_char(word=secret, character=guess[idx]):
            result = (
                result + YELLOW_BOX
            )  # Letter in secret and guess are matching but at differnt positions
        else:
            result = (
                result + WHITE_BOX
            )  # None of the letters in secret are in the guess word

        idx = idx + 1

    return result


def input_guess(expected_length: int) -> str:
    """This prompts the user for a guess of the expected length"""
    guess = input(
        f"Enter a {expected_length} character word:"
    )  # prompts for input guess

    while len(guess) != expected_length:
        guess = input(
            f"That wasn't {expected_length} chars! Try again:"
        )  # prmompts for another input if not correct length

    return str(guess)


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    total_turns: int = 6
    won_game: bool = False

    while turn <= total_turns and not won_game:
        print(f"=== Turn {turn}/{total_turns} ===")
        guess = input_guess(
            expected_length=len(secret)
        )  # This ensures the guess is the correct length
        result = emojified(
            guess=guess, secret=secret
        )  # This codifies the emoji function color results of the guess versus secret comparison
        print(result)

        if guess == secret:
            won_game = True
        else:
            turn = turn + 1

    if won_game == True:
        print(f"You won in {turn}/6 turns!")
    else:
        print(f"X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
