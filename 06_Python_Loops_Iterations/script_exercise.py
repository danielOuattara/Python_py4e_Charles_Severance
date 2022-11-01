numbers_sum = 0
average = 0
numbers_count = 0
while True:
    line = input(' Enter a number: > ')
    if line == 'done':
        break
    print(line)
    try:
        numbers_sum = numbers_sum + float(line)
        numbers_count += 1
    except:
        print('Invalid input')
        continue

if numbers_count >= 1:
    average = numbers_sum / numbers_count
print('numbers_count = ', numbers_count, '\nnumbers_sum = ', numbers_sum, '\naverage = ', average)
print('Program Terminated')

#  ----------------------------------------

# while True:
#     print("Enter secret : ")
#     line = input('> ')
#     if line[0] == '#':
#         continue
#     if line == 'done':
#         break
#     print(line)
# print('Program Terminated')
