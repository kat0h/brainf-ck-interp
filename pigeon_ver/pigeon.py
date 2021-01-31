import sys
with open(sys.argv[1]) as f:
    src = f.read()
# src length
srclen = len(src)

newsrc = ""
for i in src:
    if i in {"ポ", "ッ"}:
        newsrc += i
src = newsrc

src = [src[i: i+3] for i in range(0, len(src), 3)]
if len(src[-1]) != 3:
    del src[-1]

key = {'ポポポ': '>', 'ポポッ': '<', 'ポッポ': '+', 'ポッッ': '-',
       'ッポポ': '.', 'ッポッ': ',', 'ッッポ': '[', 'ッッッ': ']'}

newsrc = ""
for i in src:
    newsrc += key[i]
src = newsrc
srclen = len(src)

# program counter
pc = 0
# pointer locate
pt = 0
pt_max = pt
# register
rg = [0] * (3*10**4)
# jump reg
jp = []
status = True
while status:
    c = src[pc]
    if c in '>':
        if pt < 30000 - 1:
            pt += 1
            pt_max = max(pt_max, pt)
    elif c in '<':
        if pt > 0:
            pt -= 1
    elif c in '+':
        rg[pt] += 1
    elif c in '-':
        rg[pt] -= 1
    elif c in '.':
        print(chr(rg[pt]), end="")
    elif c in ',':
        rg[pt] = ord(input()[0])
    elif c in '[':
        if rg[pt] == 0:
            j = 0
            while True:
                pc += 1
                if src[pc] == '[':
                    j += 1
                if src[pc] == ']':
                    if j == 0:
                        break
                    else:
                        j -= 1
    elif c in ']':
        if rg[pt] != 0:
            j = 0
            while True:
                pc -= 1
                if src[pc] == ']':
                    j += 1
                if src[pc] == '[':
                    if j == 0:
                        break
                    else:
                        j -= 1
    else:
        pass
    # 終了判定
    if pc < srclen - 1:
        pc += 1
    else:
        status = False
