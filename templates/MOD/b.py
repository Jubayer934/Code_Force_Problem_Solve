import time

MOD = 10**9 + 7


# ---------- 1. factorial ----------
def fact_mod(n):
    r = 1
    for i in range(2, n + 1):
        r = r * i % MOD
    return r

def fact_nomod(n):
    r = 1
    for i in range(2, n + 1):
        r *= i
    return r


# ---------- 2. fibonacci (iterative) ----------
def fib_mod(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % MOD
    return a

def fib_nomod(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# ---------- 3. 3^n by repeated multiplication ----------
def pow_mod(n):
    r = 1
    for _ in range(n):
        r = r * 3 % MOD
    return r

def pow_nomod(n):
    r = 1
    for _ in range(n):
        r *= 3
    return r


def timeit(f, n):
    t = time.perf_counter()
    v = f(n)
    return time.perf_counter() - t, v


tests = [
    ("factorial", fact_mod, fact_nomod, [10_000, 30_000, 60_000]),
    ("fibonacci", fib_mod, fib_nomod, [50_000, 100_000, 200_000]),
    ("3^n loop ", pow_mod, pow_nomod, [50_000, 100_000, 200_000]),
]

print(f"{'test':<10} {'n':>8} {'with MOD':>10} {'no MOD':>10} {'slower':>8}  same?")
print("-" * 56)
for name, fm, fn, sizes in tests:
    for n in sizes:
        t1, v1 = timeit(fm, n)
        t2, v2 = timeit(fn, n)
        same = (v2 % MOD == v1)
        print(f"{name:<10} {n:>8} {t1:>9.4f}s {t2:>9.4f}s {t2 / t1:>7.0f}x  {same}")