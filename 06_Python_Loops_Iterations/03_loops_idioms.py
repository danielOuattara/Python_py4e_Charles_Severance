"""
Loop idioms, to resolve some problems
"""

# --- What is the smallest number in a list ?
smallest = 1000
print("Before:", smallest)

for item in [3, 41, 12, 2, 9, 74, 1, 15]:
    if smallest is None or item < smallest:
        smallest = item
        #  break
    print("Loop:", "item = ", item, ", smallest = ", smallest)
print("Smallest:", smallest)

print('---')

#  ----------------------------------------------

biggest = float('-inf')
for iter_number in [3, 41, 12, 9, 74, 15]:
    if iter_number > biggest:
        biggest = iter_number

print(biggest)
