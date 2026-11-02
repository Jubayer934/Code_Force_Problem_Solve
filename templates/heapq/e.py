from heapq import heappush, heappop

# g[u] = [(neighbor, weight), ...]
g = {
    1: [(2, 4), (3, 1)],
    2: [(4, 1)],
    3: [(2, 2), (4, 5)],
    4: [],
}

dist = {u: float("inf") for u in g}
dist[1] = 0
h = [(0, 1)]                      # (distance, node)

while h:
    d, u = heappop(h)
    if d > dist[u]:               # outdated entry, skip it
        continue
    for v, w in g[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            heappush(h, (dist[v], v))

print(dist)                       # {1: 0, 2: 3, 3: 1, 4: 4}