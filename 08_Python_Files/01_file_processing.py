# File processing: mostly text file here

# Opening a File
# --------------------

#  open() to handle a file: open , read, write, close, mostly in utf-8
# -------------------------------------------------
# file_handle = open("filename", "mode")

# The newline Character: "\n", it's count for 1 character
stuff = "Hello \nWorld of Python!"
print(stuff)
print(len(stuff))

# What is 'handle'
file_handle = open("demo.txt", "r")
print(file_handle)
file_handle.close()

#  When the file is missing: --> Traceback

# File processing
