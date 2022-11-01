# Reading  & converting

# name = input('Enter your name :')
# print(name)

# Looking Inside Strings

fruit = 'banana'
second_letter = fruit[1]
print(second_letter)

x = 3
w = fruit[x - 1]
print(w)

# String length

fruit_length = len(fruit)
print(fruit_length)

# Looping through Strings

print(70 * '-')

for letter in fruit:
    print(letter)


print(70 * '-')
i = 0
while i < len(fruit):
    print(fruit[i])
    i = i + 1