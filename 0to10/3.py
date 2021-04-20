import re
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

str_sub = re.sub(r'[,\.]', '', str)

str_split = str_sub.split()

str_len = [len(i)for i in str_split]

print(str_len)