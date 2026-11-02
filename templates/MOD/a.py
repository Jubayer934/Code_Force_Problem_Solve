MOD = 10**9 + 7

print((7 + 5) % MOD)        # 12
print((3 - 5) % MOD)        # 1000000005  (wraps to positive)
print(7 * 5 % MOD)          # 35

print(pow(2, 10, MOD))      # 1024

print(6 * pow(3, MOD - 2, MOD) % MOD)    # 2   (same as 6 / 3)

n = 10
inv2 = pow(2, MOD - 2, MOD)
print(n * (n + 1) % MOD * inv2 % MOD)    # 55