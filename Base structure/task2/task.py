def mass_prob(ch, mass):
    for p in mass:
        if p not in roads:
            roads[p] = ch
        ch -= 1
def height(poisk, mass, ch = 0):
    mass.append(poisk)
    ch += 1
    if parent[poisk] != -1:        
        if parent[poisk] in roads:
            mass_prob(ch+roads[parent[poisk]], mass)
            return ch + roads[parent[poisk]]
        else:
            return height(parent[poisk], mass, ch)
    else:
        mass_prob(ch, mass)
        return ch

n = int(input())
roads = {}
parent = [int(i) for i in input().split()]
for i in range(n):
    if i not in roads:
        height(i, list())
print(max(roads.values()))