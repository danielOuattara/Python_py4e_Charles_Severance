largest = None
smallest = None
list_input = []
valid_inputs = 0

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        print('terminated !')
        break
    try:
        list_input.append(int(user_input))
    except:
        continue
    valid_inputs = valid_inputs + 1
    for number in list_input:
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
print('Number of valid inputs :', valid_inputs)
print('Maximum is', largest)
print('Minimum is', smallest)
