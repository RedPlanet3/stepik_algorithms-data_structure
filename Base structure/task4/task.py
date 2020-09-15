max_steck = []
maximum = 0
for i in range(int(input())):
    s = input().strip()
    if 'push' in s:
        num = int(s[5:])
        if num > maximum:
            maximum = num
        max_steck.append(maximum)
    elif s == 'pop':
        if len(max_steck) > 0:
            max_steck.pop()
            maximum = max_steck[-1]
    elif s == 'max':
        if len(max_steck) > 0:
            print(maximum)