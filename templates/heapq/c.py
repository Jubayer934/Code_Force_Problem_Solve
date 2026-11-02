from heapq import heappop, heappush 

h = []
heappush(h, (3, "write code"))
heappush(h, (1, "wake up"))
heappush(h, (2, "eat"))
heappush(h, (4, "sleep"))

print(h)

print(heappop(h))       # (1, 'wake up')
print(heappop(h))       # (2, 'eat')
print(heappop(h))       # (3, 'write code')