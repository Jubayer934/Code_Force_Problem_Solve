def generate_binary_string(n):
    print("1",end="")
    return ''.join('0'for i in range(n-1))

t = int(input())
for _ in range(t):
    n = int(input())
    print(generate_binary_string(n))