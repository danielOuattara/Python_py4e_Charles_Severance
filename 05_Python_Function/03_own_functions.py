def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


# --------------- Call function

x = 5
print('Hello')


def print_lyrics_2():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')


print_lyrics_2()
print('Yo')
x = x + 2
print(x)


# ---------------- Params
def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'fr':
        print('Bonjour')
    else:
        print('Hello')


greet('en')
greet('es')
greet('fr')


# --------------- Function Return statement

def greet():
    return "Hello"


print(greet(), "Glenn")
print(greet(), "Sally")

# ---


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'


print(greet('en'), 'Glenn')
print(greet('es'), 'Sally')
print(greet('fr'), 'Michael')
