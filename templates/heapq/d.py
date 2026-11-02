from heapq import heapify, heappop, heappush    

a = [5, 1, 8, 3]
heapify(a)              # O(n), faster than pushing one by one

print(a)                # [1, 3, 8, 5] (the smallest is always at index 0, peek without removing)
print(heappop(a))       # 1