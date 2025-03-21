"""Unit Tests for Dictionary Functions Exercise."""

__author__: str = "730737128"


from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len


def test_invert_use1() -> None:
    """Test inverting a dictionary with unique values."""
    original = {"a": "1", "b": "2", "c": "3"}
    inverted = {"1": "a", "2": "b", "3": "c"}
    assert invert(original) == inverted


def test_invert_use2() -> None:
    """Test inverting dictionary with unique values."""
    original = {"Horse": "fast", "Dog": "loyal", "Cat": "independent"}
    inverted = {"fast": "Horse", "loyal": "Dog", "independent": "Cat"}
    assert invert(original) == inverted


def test_invert_edge1() -> None:
    """Test invert with empty dictionary."""
    original = {}
    assert invert(original) == {}


def test_count_use1() -> None:
    """Test count with unique list of strs."""
    values: list[str] = ["cat", "horse", "cat"]
    assert count(values) == {"cat": 2, "horse": 1}


def test_count_use2() -> None:
    """Test count with multiple instances of the same value."""
    values: list[str] = ["apple", "apple", "apple", "banana"]
    assert count(values) == {"apple": 3, "banana": 1}


def test_count_edge1() -> None:
    """Test count with empty list."""
    values: list[str] = []
    assert count(values) == {}


def test_favorite_color_use1() -> None:
    """Test favorite color with unique dictionary."""
    names_and_colors: dict[str, str] = {"Susan": "blue", "Mark": "Red", "Lucy": "blue"}
    assert favorite_color(names_and_colors) == "blue"


def test_favorite_color_use2() -> None:
    """Test favorite color with tie for favorite color."""
    names_and_colors: dict[str, str] = {
        "Susan": "red",
        "Mark": "blue",
        "Lucy": "red",
        "Tom": "blue",
    }
    assert favorite_color(names_and_colors) == "red"


def test_favorite_color_edge1() -> None:
    """Test favorite color with empty dictionary."""
    names_and_colors: dict[str, str] = {}
    assert favorite_color(names_and_colors) == ""


def test_bin_len_use1() -> None:
    """Test bin len with strings of varying lengths."""
    input: list[str] = ["a", "bc", "def"]
    assert bin_len(input) == {1: {"a"}, 2: {"bc"}, 3: {"def"}}


def test_bin_len_use2() -> None:
    """Test bin len with strings of all same length."""
    input: list[str] = ["app", "hey", "cat"]
    assert bin_len(input) == {3: {"app", "hey", "cat"}}


def test_bin_len_edge1() -> None:
    """test bin len with empty list."""
    input: list[str] = []
    assert bin_len(input) == {}
