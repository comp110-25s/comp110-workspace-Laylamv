# Function writing


def count_regs(county_of_interest: str, counties: list[str]) -> int:
    idx: int = 0
    total: int = 0
    while idx < len(counties) - 1:  # or while idx < len(counties )
        if county_of_interest == counties[idx]:
            total += 1  # need a local variable to keep track of how many times the county of interest appears in the list
        idx += 1
    return total


print(count_regs("Orange", ["Wkake", "Orange", "Orange", "Durham"]))


def hehe(n: int) -> int:
    return 0
