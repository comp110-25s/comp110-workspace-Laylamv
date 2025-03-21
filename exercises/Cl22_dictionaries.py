""" "examples of dictionar syntax."""

# dictionart type is dict[key_type, value_type]
# Dictionary literals are curly brackets
# that surround with key:value pairs
ice_cream: dict[str, int] = {"chocolate": 8, "vanilla": 8, "strawberry": 4}

# len evaluates to number of key value entires
print(f"{len(ice_cream)} flavors")

# add key-value entires using subscription notation
ice_cream["mint"] = 3

# access values by their key using subscription notation
print(ice_cream["chocolate"])

# re-assign values bu their key using assignment
ice_cream["vanilla"] += 10


# remove items by key using pop method
ice_cream.pop("strawberry")

# loop through items using for-in loops
total_orders: int = 0


for flavor in ice_cream:
    print(f"{flavor}: {ice_cream[flavor]}")
    total_orders += ice_cream[flavor]

print(f"total orders: {total_orders}")
