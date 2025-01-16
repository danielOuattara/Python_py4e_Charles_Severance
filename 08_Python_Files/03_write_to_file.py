""" writing to file"""

# write
f_out = open('output.txt', 'w')
print(f_out)
line_1 = "This here's the battle"
f_out.write(line_1)
f_out.close()

# ----------------------------------------------------

# write
with open('output_2.txt', 'w') as f_out_2:
    print(f_out_2)
    line_1 = "This here's the battle\n"
    f_out_2.write(line_1)
    f_out_2.write(line_1)
    f_out_2.write(line_1)
    f_out_2.close()

# read
with open('output_2.txt', encoding='utf-8') as f_hand:
    for line in f_hand:
        line = line.rstrip()
        print(line)
