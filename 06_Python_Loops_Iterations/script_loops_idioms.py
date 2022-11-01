smallest = None
print("Before:", smallest)

for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        #  break
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)

print('---')
#  ----------------------------------------------

biggest = float('-inf')
for iter_number in [3, 41, 12, 9, 74, 15]:
    if iter_number > biggest:
        biggest = iter_number

print(biggest)
