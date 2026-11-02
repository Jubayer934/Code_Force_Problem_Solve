from heapq import nsmallest, nlargest

a = [7, 2, 9, 4, 1, 6, 8]

print(nsmallest(3, a))    # [1, 2, 4]   (3 smallest, smallest first)
print(nlargest(3, a))     # [9, 8, 7]   (3 largest, largest first)

students = [("Ana", 85), ("Ben", 92), ("Cara", 78), ("Dev", 92)]

print(nlargest(2, students, key=lambda s: s[1]))
# [('Ben', 92), ('Dev', 92)]   (top 2 by score)

print(nsmallest(1, students, key=lambda s: s[1]))
# [('Cara', 78)]               (lowest score)

price = {"apple": 5, "mango": 12, "kiwi": 8, "grape": 15}

print(nlargest(2, price, key=price.get))     # ['grape', 'mango']  (2 most expensive)
print(nsmallest(2, price, key=price.get))    # ['apple', 'kiwi']   (2 cheapest)     