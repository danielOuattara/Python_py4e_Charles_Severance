# print(help(tuple))

users = ("Daniel", "Julie", "Gaia", "Amaya")
print(users)

# print all item in tuple
for person in users:
    print(person)

print(50 * '~')
# Tuples are immutables, like string

for item in dir(list()):
    print(item)

print(50 * '~')

for item in dir(tuple()):
    print(item)
print(50 * '~')

# Tuples are more efficient

# Tuples and assignment
(x, y) = (4, "Moon")
print(x)
print(y)

print(50 * '~')

(x, *y) = (4, "Moon", "cool")
print(x)
print(y)

print(50 * '~')

# Tuples and dictionaries
dico = dict()
dico["mai"] = 4
dico["december"] = 12

for (k, v) in dico.items():
    print(k, v)

print(50 * '~')

items_in = dico.items()
print(f'items_in = {items_in}')

print(50 * '~')

# Tuples are Comparable
print((0, 1, 2) < (1, 2, 3))
print(("Daniel", "Julie", "Gaia", "Amaya") < ("Daniel", "Gaia", "Amaya"))
