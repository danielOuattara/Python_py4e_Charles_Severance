# ----- Looping through Strings

fruit = 'banana'

# This ONE
for letter in fruit:
    print(letter)

print(70 * '-')

# -----------------------

# OR This ONE
i = 0
while i < len(fruit):
    print(fruit[i])
    i = i + 1

# ----- Looping and Counting

word = "banana"
count = 0

for letter in word:
    if letter == "a":
        count = count + 1

print("count = ", count)
