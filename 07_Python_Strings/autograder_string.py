text = "X-DSPAM-Confidence:    0.8475"

column_pos = text.find(':')
piece = float(text[column_pos + 1:])
print(piece)


piece = text[column_pos + 1:].strip()
print(piece)
