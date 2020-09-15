def append_right(max_right_num):
    for i in range(len(left_max)):
        o = left_max.pop()
        if max_right_num < o:
            max_right_num = o
        right_max.append(max_right_num)

n = int(input())
massiv = [int(i) for i in input().split()]
m = int(input())
left_max, right_max = [], []
max_right_num, max_left_num = 0, 0
if m >= n:
    print(max(massiv))
else:
    for i in range(m):
        left_max.append(massiv.pop(0))
    while True:
        if len(massiv) < 1:
            if len(left_max) < 1:
                print(right_max.pop(), end=' ')
                break
            else:
                if len(right_max) > 1:
                    max_right_num = right_max[-1]
                append_right(max_right_num)
                while len(right_max) >= m:
                    print(right_max.pop(), end=' ')
                break
        else:
            if len(right_max) == 0:
                max_right_num = 0
                append_right(max_right_num)
                max_left_num = 0
            r = right_max.pop()
            if r >= max_left_num:
                print(r, end=' ')
            else:
                print(max_left_num, end=' ')
            l = massiv.pop(0)
            if l > max_left_num:
                max_left_num = l
            left_max.append(l)