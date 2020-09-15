size, n = [int(i) for i in input().split()]
arrival, duration = [], []
start = 0
buffer = 0
end_time = []
if n > 0:
    for i in range(n):
        a, d = [int(i) for i in input().split()]
        arrival.append(a)
        duration.append(d)
    timer = arrival[start]
    while True:
        if start >= len(arrival):
            break
        delete = 0
        for i in range(len(end_time)-1, -1, -1):
            if end_time[i] <= timer:
                buffer -= 1
                delete += 1
            else:
                break
        for i in range(delete):
            end_time.pop()
        for i in range(arrival.count(timer)):
            add = True
            if buffer < size:
                buffer += 1
                if len(end_time) == 0:
                    act = timer
                    if duration[start] == 0:
                        buffer -= 1
                        add = False
                else:
                    act = end_time[0]
                print(act)
                if add:
                    end_time.insert(0, act + duration[start])
            else:
                print(-1)
            start += 1
        if start < len(arrival):
            timer = arrival[start]