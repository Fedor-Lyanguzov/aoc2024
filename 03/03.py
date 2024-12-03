import re


data = open("input.txt").read().strip()

def mul(a, b):
    return a*b

print(sum(eval(x) for x in re.findall("mul\(\d{1,3},\d{1,3}\)", data)))

q = "mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)"
f = True
s = 0
for x in re.findall(q, data):
    if x=='do()':
        f = True
    elif x=='don\'t()':
        f = False
    elif f:
        s += eval(x)
print(s)
