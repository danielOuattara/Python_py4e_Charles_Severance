str = 'X-DSPAM-Confidance: 0.8475'

print(str)

column_pos = str.find(':')
print(column_pos)

piece = str[column_pos + 1:]
print(piece)

piece_float = float(piece)
print(piece_float)

print(piece_float + 23)