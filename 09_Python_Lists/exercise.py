print(70 * '-')

file = open("mail_box.txt")
for line in file:
    if not line.startswith("From"):
        continue
    line = line.strip()
    words = line.split()
    if not len(words) > 2:
        continue
    week_day = words[2]
    print(week_day)

print(70 * '-')

# The double Split Pattern

message_info = "From louis@media.berkeley.edu Fri Jan  4 18:10:48 2008"
info_list = message_info.split()
print("info_list = ", info_list)

email = info_list[1].split("@")
domain_name = email[1]
print("domain_name = ", domain_name)