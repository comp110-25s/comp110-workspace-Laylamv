"""Pytest practice."""


def animal_counter(animal: str, list_of_animals: list[str]) -> int:
    """Returns the value of how many times the animal of inteerest is in the list."""
    idx: int = 0
    total: int = 0
    while idx < len(list_of_animals):
        if animal == list_of_animals[idx]:
            total = total + 1
        idx += 1
    return total


animals: list[str] = ["Horses", "Cows", "Horses", "Cats"]
print(animal_counter("Eel", animals))
