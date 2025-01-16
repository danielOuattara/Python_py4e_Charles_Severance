"""List 01 """

print(70 * '-')

#  A List is a Kind Of Collection
friends = ["Jo", "Glenn", "Sally"]

# List Constants
prime_numbers = [2, 3, 5, 7]

numbers_list = [1, 23, [3, 2], 4, 1, 4]

# Lists & definite loops
for friend in friends:
    print("Good morning", friend)

print(70 * '-')

# Looking Inside List
print(friends[0])
print(friends[1])
print(friends[2])

print(70 * '-')

# List are Mutable
friends[0] = "Joseph"
print(friends)

# print(dir(friends))

print(70 * '-')
# print(help(friends))
friends.append("Maria")
friends.insert(2, "Big Jo")

print(friends)

numbers_list = [1, 23, [3, 2], 4, 1, 4, 1]
print('1 appears ', numbers_list.count(1), 'times here')

print(70 * '-')

# Using the range function

print(range(4))

friends = ["Jo", "Glenn", "Sally"]

for i in range(len(friends)):
    friend = friends[i]
    print("Hello", friend)

print('---')
# OR

for friend in enumerate(friends):
    print(friend)

print('---')
# OR (which is better)

for i, friend in enumerate(friends):
    print(i, friend)


print(70 * '-')

for i in range(4):
    print(i)
