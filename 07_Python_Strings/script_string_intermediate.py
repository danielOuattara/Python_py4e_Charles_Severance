import re

#  slicing
#  ----------------------------
my_string = "Monty Python"

print(my_string[0: 4])
print(my_string[6: 7])
print(my_string[6: 20])

print(my_string[-10: -1])
print(my_string[6: 20])

print(my_string[: 7])
print(my_string[:])

print(70 * '-')

#  String Concatenation
#  ----------------------------

#  Using 'in' as a logical operator in string
fruit = "banana"
print("n" in fruit)
print("z" in fruit)
print("z" not in fruit)

print(70 * '-')

#  String Comparison
#  ----------------------------

print("Hello" < "hello")

print(70 * '-')

#  String Library
#  ----------------------------
name = "Bob Johnson"
print(name.lower())
print(name.count("b"))
print(len(name))
# print(dir(name))  # output doc

print(70 * '-')

age = 12
print(dir(age))  # output doc

print(70 * '-')

print(help(age))  # output doc

print(70 * '-')

#  Searching a String
#  ----------------------------
fruit = 'banana'
na_index = fruit.find('na')  # 2
print(na_index)
za_index = fruit.find('za')  # -1
print(za_index)

print(70 * '-')

greet = "Hello Bob"
print(greet)
new_greet = greet.replace("Bob", "Daniel")
print(new_greet)

not_found_greet = greet.replace("Anna", "Daniel")  # not found "Anna", returns original values
print(not_found_greet)

greet = "Hello Bob dear Bob, the great Bob, special Bob"
print(greet)

new_greet_many = greet.replace("Bob", "Daniel")  # replace all occurrences, not only the first
print(new_greet_many)

print(70 * '-')

#  Stripping whiteSpace
#  ----------------------------
msg = "    Hello You all !    "
print(msg.strip())
msg = "        Hello     You     all        !    Me    you   "
print(re.sub("\s{2,}", " ", msg))

print(70 * '-')

#  Parsing & Extracting
#  ----------------------------

msg_head = "From stephen.marquard@uct.ac.za Sta Jan 5 09:14:16 2008"
at_sign_position = msg_head.find("@")
print(at_sign_position)

space_after_at_sign = msg_head.find(" ", at_sign_position)
print(space_after_at_sign)

host_email = msg_head[at_sign_position + 1: space_after_at_sign]
print(host_email)

host_email_2 = re.search(r"[a-zA-Z\.]+@([a-zA-Z\.]+)", msg_head)
print(host_email_2)

#  print(help(re))
#  ----------------------------
