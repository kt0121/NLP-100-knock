import re
str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

one_index = [1,5,6,7,8,9,15,16,19]

str_sub = re.sub(r'\.', '', str)

str_split = str_sub.split()

chemical_symbols = {}

for i, word in enumerate(str_split):
    if i + 1 in one_index:
        chemical_symbols[word[:1]] = i + 1
    else:
        chemical_symbols[word[:2]] = i + 1

print(chemical_symbols)