from collections import deque

g = {1: [2, 3], 2: [4], 3: [4], 4: []}

dist = {1: 0}
q = deque([1])             
while q:
    u = q.popleft()
    for v in g[u]:
        if v not in dist:
            dist[v] = dist[u] + 1
            q.append(v)
print(dist)           # {1: 0, 2: 1, 3: 1, 4: 2}