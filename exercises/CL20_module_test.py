"""Test function in count regs"""

from CL20_module import count_regs, heh


def test_count_regs_empty() -> (
    None
):  # start test function name with test, for unit tests no value needs to be returned
    """Test count_regs function with na"""


def test_hehe() -> None:
    # Other code can be here
    assert hehe(5) == 1
    # only requirement is that there is an assert statement that evaluates to a true or false


def test_count_regs_use1() -> None:
    assert count_regs("Orange", ["Wkake", "Orange", "Orange", "Durham"]) == 2


def test_count_regs_empty() -> None:
    assert count_regs("Orange", []) == 0


def test_count_regs_mutate() -> None:
    """Tests if count regs mutates list"""
    cs: list[str] = ["Orange", "Wake", "Lee"]
    count_regs("Orange", cs)
    assert cs == ["Orange", "Wake", "Lee"]
