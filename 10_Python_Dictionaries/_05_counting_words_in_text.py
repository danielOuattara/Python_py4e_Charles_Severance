""" counting Words In Text """


# Counting Pattern for 1 line of text
# -----------------------------------

# print('-' * 70)

# print('Enter a line of text : ')
# line = input('')

# print('-' * 70)

# words = line.split()
# print(f'Words =, {words}')

# print('-' * 70)

# counts = dict()
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print("counts = ", counts)

# print('-' * 70)

# for key, value in counts.items():
#     print(key, " = ", value)


# Definite Loops and Dictionaries
# -----------------------------------

user = {'firstName': 'Daniel', 'lastName': 'Ouattara'}
for key in user:
    print(key, user[key])


# Retrieving lists of Keys and Values
# -------------------------------------
user = {'firstName': 'Daniel', 'lastName': 'Ouattara'}

print(list(user))     # print a list of keys from the user dict
print(user.keys())    # print a list of keys from the user dict
print(user.values())  # print a list of values from the user dict
print(user.items())   # print a list of tuple key/value pairs from the user dict


# Bonus: Two Iteration Variables!
# --------------------------------

for key, value in user.items():
    print(key, value)


# Counting words in a text file
# ------------------------------

def words_counter():
    """ Counting words in a text file + other actions"""
    counts = {}

    filename = input('Enter file :')
    file = open(filename)
    for line in file:
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1

    counts_sorted_by_key = dict(
        sorted(counts.items()))
    # print("counts_sorted_by_key = ", counts_sorted_by_key)
    for key, value in counts_sorted_by_key.items():
        print(key, value)

    counts_sorted_by_value = dict(
        sorted(counts.items(), key=lambda item: item[1], reverse=True))
    # print("counts_sorted_by_value = ", counts_sorted_by_value)

    big_count = None
    big_word = None
    for word, count in counts.items():
        if big_count is None or count > big_count:
            big_count = count
            big_word = word

    file.close()
    print(f'big_word = {big_word}\nbig_count = {big_count}')


words_counter()

# ------


def words_counter_2():
    """ Counting words in a text file + other actions"""

    filename = input('Enter file :')
    counts = {}

    with open(filename, encoding='utf-8') as file:
        for line in file:
            for word in line.split():
                counts[word] = counts.get(word, 0) + 1

    counts_sorted_by_key = dict(
        sorted(counts.items()))
    print("counts_sorted_by_key = ", counts_sorted_by_key)

    counts_sorted_by_value = dict(
        sorted(counts.items(), key=lambda item: item[1], reverse=True))
    print("counts_sorted_by_value = ", counts_sorted_by_value)

    big_count = None
    big_word = None
    for word, count in counts.items():
        if big_count is None or count > big_count:
            big_count = count
            big_word = word
    file.close()
    print(f'big_word = {big_word}\nbig_count = {big_count}')


words_counter_2()


# ----------------------------------------------------------

def words_counter_3():
    """ Counting words in a text file + other actions"""

    counts = {}
    filename = input('Enter file: ')
    with open(filename) as file:
        for line in file:
            for word in line.split():
                counts[word] = counts.get(word, 0) + 1

    big_word, big_count = max(counts.items(), key=lambda item: item[1])
    print(f'big_word = {big_word}\nbig_count = {big_count}')


words_counter_3()
# ----------------------------------------------------------

counts = {'chuck': 1, 'annie': 42, 'jan': 100}
for key in counts:
    if counts[key] > 10:
        print(key, counts[key])
