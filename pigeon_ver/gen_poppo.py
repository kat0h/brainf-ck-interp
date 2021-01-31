import sys

key = {'>': 'ポポポ', '<': 'ポポッ', '+': 'ポッポ', '-': 'ポッッ',
       '.': 'ッポポ', ',': 'ッポッ', '[': 'ッッポ', ']': 'ッッッ', }

with open(sys.argv[1]) as f:
    src = f.read()

retsrc = ""

for i in src:
    if i in {">", "<", "+", "-", ".", ",", "[", "]", }:
        retsrc += key[i]
    elif i in "\n":
        retsrc += "\n"

print(retsrc)
