# counting Words In Text
# =======================


# Counting Pattern for 1 line of text
# -----------------------------------

# counts = dict()
# print('Enter a line of text : ')
# line = input('')
#
# words = line.split()
# print(f'Words =, {words}')
#
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
#
#
# for key, value in counts.items():
#     print(key, " = ", value)
#

# Definite Loops and Dictionaries
# -----------------------------------

user = {'firstName': 'Daniel', 'lastName': 'Ouattara'}
for key in user:
    print(key, user[key])

print(list(user))  # print a list of keys from the user dict
print(user.keys())  # print a list of keys from the user dict
print(user.values())  # print a list of values from the user dict
print(user.items())  # print a list of tuple key/value pairs from the user dict


# ----------------------------------------------------------------

def words_counter():
    counts = {}

    filename = input('Enter file :')
    file = open(filename)
    for line in file:
        for word in line.split():
            counts[word] = counts.get(word, 0) + 1

    big_count = None
    big_word = None
    for word, count in counts.items():
        if big_count is None or count > big_count:
            big_word = word
            big_count = count

    file.close()
    print(f'big_word = {big_word}\nbig_count = {big_count}')


words_counter()


def words_counter_2():
    filename = input('Enter file :')
    counts = {}

    with open(filename) as file:
        for line in file:
            for word in line.split():
                counts[word] = counts.get(word, 0) + 1

    big_count = None
    big_word = None
    for word, count in counts.items():
        if big_count is None or count > big_count:
            big_word = word
            big_count = count
    file.close()
    print(f'big_word = {big_word}\nbig_count = {big_count}')


words_counter_2()


# ----------------------------------------------------------

def words_counter_3():
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
