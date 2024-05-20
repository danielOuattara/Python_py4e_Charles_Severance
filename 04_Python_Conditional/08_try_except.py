# Error in execution
"""
astr = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr)
print('Second', istr)

"""

# ---

astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

# ----

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)

# --- Not clean code: too much code in 'try' block

astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)
    print('There')
except:
    istr = -1

print('Done', istr)

# --- Daily examples

rawstr = input('Enter a number:')
try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')
