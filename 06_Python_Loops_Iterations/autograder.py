largest = None
smallest = None
list_input = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        print('Invalid input')
        break
    try:
        list_input.append(int(user_input))
    except:
        continue
    for number in list_input:
        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number
print('Maximum is', largest)
print('Minimum is', smallest)