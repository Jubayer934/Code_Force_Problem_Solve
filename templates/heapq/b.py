from heapq import heappop, heappush

h = []
for x in [5, 1, 8, 3]:
    heappush(h, -x)
print(h)
print(-heappop(h))      # 8  (largest)
print(-heappop(h))      # 5
