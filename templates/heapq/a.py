from heapq import heappush, heappop

h = []                  # a heap is just a list
heappush(h, 5)
heappush(h, 1)
heappush(h, 8)
heappush(h, 3)
heappush(h, 4)
heappush(h, 2)

print(h)           
print(h[0])             # 1   (the smallest is always at index 0, peek without removing)

print(heappop(h))       # 1   (remove and return the smallest)
print(heappop(h))       # 3
print(heappop(h))       # 5
print(heappop(h))       # 8

"""
       1        <-- h[0] (smallest element)
      / \
     3   8      <-- h[1] and h[2]
    /
   5            <-- h[3]

       1        
      / \
     3   8      
    / \
   5   4        <-- 4 is added as the right child of 3

       1        
      / \
     3   2      <-- 2 swapped with 8 and moved up here
    / \  /
   5   4 8      <-- 8 got pushed down to the bottom right
"""