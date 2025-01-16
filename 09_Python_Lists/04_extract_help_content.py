""""Extract help content"""

import io
import sys

# Redirect the output of help(str) to a string
help_str_io = io.StringIO()
sys.stdout = help_str_io
help(str)
sys.stdout = sys.__stdout__

# Get the string from the StringIO object
help_str = help_str_io.getvalue()

# Write the output to a file
with open("help_str.txt", encoding='utf-8', mode="w",) as file:
    file.write(help_str)
    file.close()

"""
Changes made:
1. Used io.StringIO() to capture the output of help(str).
2. Redirected sys.stdout to the StringIO object to capture the output.
3. Restored sys.stdout to its original state.
4. Retrieved the captured output from the StringIO object and stored it in the help_str variable.
5. Wrote the content of help_str to the file "str_help".
This approach ensures that the content of help(str) is captured and written to the file as you intended.
"""
