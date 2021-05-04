print('Task 35!')
print()

print('6.')
import re
def calc(s):
    ss = re.match("^([+-]?\d+.\d+|[+-]?\d+)\s?(\+|-|\*|/)\s?([+-]?\d+.\d+|[+-]?\d+)$", s)
    ch = ss is not None
    if ch != True:
        return 'не понимаю. Пробуй ещё'
    else:
        l = ss.groups()
    if re.match('^\d+.\d+$', l[0]) is not None:
        a = float(l[0])
    else:
        a = int(l[0])
    if re.match('^\d+.\d+$', l[2]) is not None:
        b = float(l[2])
    else:
        b = int(l[2])
    if l[1] == '+':
        return a + b
    elif l[1] == '-':
        return a - b
    elif l[1] == '/':
        return a / b
    elif l[1] == '*':
        return a * b
sd = input('Введи простое арефметическое выражение: ')
print(calc(sd))