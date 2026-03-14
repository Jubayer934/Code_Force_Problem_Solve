def result(a, b):
    na = b[0] + a[1:]
    nb = a[0] + b[1:]
 
    print(f"{na} {nb}")
    
        
 
 
 
def user_input(_):
    a, b = input().split()
    result(a, b)
 
"""
Code Start Here
"""
n = int(input())
 
for _ in range(n):
    user_input(_)