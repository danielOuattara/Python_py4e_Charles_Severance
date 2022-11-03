# print(help(tuple))

users = ("Daniel", "Julie", "Gaia", "Amaya")
print(users)

# print all item in tuple
for person in users:
    print(person)

# Tuples are immutables, like string

print(dir(list()))

print(100 * '~')

print(dir(tuple()))

print(100 * '~')
# Tuples are more efficient

# Tuples and assignment
(x, y) = (4, "Moon")
print(x)
print(y)

print(100 * '~')

(x, *y) = (4, "Moon", "cool")
print(x)
print(y)

print(100 * '~')

# Tuples and dictionaries
dict = dict()
dict["mai"] = 4
dict["december"] = 12

for (k, v) in dict.items():
    print(k, v)

print(100 * '~')

items_in = dict.items()
print(items_in)

print(100 * '~')

# Tuples are Comparables
print((0, 1, 2) < (1, 2, 3))
print(("Daniel", "Julie", "Gaia", "Amaya") < ("Daniel", "Gaia", "Amaya"))
