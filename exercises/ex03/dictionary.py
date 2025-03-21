"""Exercise: Dictionary Functions."""

__author__: str = "730737128"


def invert(original: dict[str, str]) -> dict[str, str]:
    """Inverts the keys and values of the original dictionary."""
    inverted: dict[str, str] = {}  # declare empty dict
    for key in original:  # loops through keys in original dictionary
        value: str = original[key]

        if value in inverted:
            raise KeyError("Cannot have repeat of Keys!")

        inverted[value] = key

    return inverted


def count(values: list[str]) -> dict[str, int]:
    """makes a dictionary with keys from list values and values from the count of those values."""
    result_dictionary: dict[str, int] = {}
    idx: int = 0
    while idx < len(values):
        current_value: str = values[
            idx
        ]  # sets current value equal to item in input list at that index

        if current_value in result_dictionary:
            result_dictionary[current_value] += 1
        else:
            result_dictionary[current_value] = 1

        idx = idx + 1

    return result_dictionary


def favorite_color(names_and_colors: dict[str, str]) -> str:
    """Returns the most favorite color."""
    color_count: dict[str, int] = {}
    for name in names_and_colors:
        if names_and_colors[name] in color_count:
            color_count[names_and_colors[name]] += 1
        else:
            color_count[names_and_colors[name]] = 1

    highest_color: str = ""
    total: int = 0

    for colors in color_count:
        if color_count[colors] > total:
            total = color_count[colors]
            highest_color = colors

    return highest_color


def bin_len(input: list[str]) -> dict[int, set[str]]:
    output: dict[int, set[str]] = {}
    for value in input:  # for loops through strings in input list
        if (
            len(value) in output
        ):  # if int value is in output dictionary, then add string value to to set
            output[len(value)].add(value)
        else:
            output_set: set[str] = {
                value
            }  # if the int value is not in the set, have to make a new set variable ewual to that string value
            output[len(value)] = (
                output_set  # this adds a new key-value entry to output,
            )
    return output
