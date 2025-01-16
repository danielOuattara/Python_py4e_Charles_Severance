"""Dictionaries 1"""

purse = dict()
purse["money"] = 12
purse["candy"] = "strawberry"
purse["map"] = 1

print(purse)

purse["money"] = purse["money"] + 30

print(purse)

# ======================================================

data = {"age": 21, "course": 101}
print(data)

data["age"] += 3
print(data)

# =======================================================

data_2 = dict(age=21, course=101, country='china')
print(data_2)

data_2["age"] += 3
print(data_2)

# =======================================================
