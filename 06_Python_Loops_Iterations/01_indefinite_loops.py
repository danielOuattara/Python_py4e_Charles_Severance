# indefinite loops

n = 5
while n > 0:
    print(n)
    n = n - 1

print('Finish, final n = ', n)

#  ----------------------------------------

while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)
print('Program Terminated')

#  ----------------------------------------

while True:
    print("Enter secret : ")
    line = input('> ')
    if line[0] == '#':
        continue
    print("mid route")
    if line == 'done':
        print("exiting")
        break
    print(line)
print('Program Terminated')
