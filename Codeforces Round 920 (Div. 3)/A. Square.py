def result(a, b):
    print(pow(a-b, 2))


n = {}

i = int(input())
for _ in range(i):
    n[_+1] = {}

    n[_+1]["a"] = tuple(map(int, input().split()))
    n[_+1]["b"] = tuple(map(int, input().split()))
    n[_+1]["c"] = tuple(map(int, input().split()))
    n[_+1]["d"] = tuple(map(int, input().split()))

    if n[_+1]["a"][0] == n[_+1]["b"][0]:
        result(n[_+1]["a"][1], n[_+1]["b"][1])
    elif n[_+1]["a"][0] == n[_+1]["c"][0]:
        result(n[_+1]["a"][1], n[_+1]["c"][1])
    elif n[_+1]["a"][0] == n[_+1]["d"][0]:
        result(n[_+1]["a"][1], n[_+1]["d"][1])