"""my first exercise in CAMP110!"""

__author__ = "730737128"


def greet(name: str) -> str:
    """A welcoming first function definition."""
    return "hello, " + name + "!"


if __name__ == "__main__":
    print(greet(name=input("what is your name? ")))
