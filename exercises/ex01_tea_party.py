"""How to Plan a Cozy Tea Party."""

__author__: str = "730737128"


def main_planner(guests: int) -> None:
    """This brings all the functions together."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


def tea_bags(people: int) -> int:
    """This calculates the number of tea bags needed."""
    return 2 * people


def treats(people: int) -> int:
    """This calculates the number of treats needed for each guest."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """This calculates the cost of the tea bags and treats."""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
