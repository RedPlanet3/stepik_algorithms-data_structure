def check(d, ind, close):
    if close == ')':
        open = '('
    elif close == '}':
        open = '{'
    elif close == ']':
        open = '['
    sd = {'(', '{', '['}
    sd.remove(open)
    if d and open in d:
        for j in range(len(d) - 1, -1, -1):
            if d[j] in sd:
                print(i + 1)
                return False
            elif d[j] == open:
                d.pop()
                ind.pop()
                return True
    else:
        print(i + 1)
        return False

s = input()
d = []
ind = []
ch = True
if s:
    for i in range(len(s)):
        if ch != False:
            if s[i] in (')', '}', ']'):
                ch = check(d, ind, s[i])
            elif s[i] in ('(', '{', '['):
                ind.append(i+1)
                d.append(s[i])
if ch == True:
    if ind:
        print(ind.pop())
    else:
        print('Success')  