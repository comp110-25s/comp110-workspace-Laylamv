"""Test function for animal_counter."""

from animals_module import animal_counter


def test_animal_counter_use_1() -> None:
    """Tests the expected use of animal_counter."""
    assert animal_counter("Horses", ["Horses", "Cows", "Horses", "Cats"]) == 2


def test_animal_counter_use_2() -> None:
    """Tests the use of animal counter again."""
    assert animal_counter("Horses", ["Cats", "Dogs"]) == 0


def test_amimal_counter_edge_case1() -> None:
    """Tests unexpected input."""
    assert animal_counter("Horses", []) == 0
