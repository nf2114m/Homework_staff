def fn(a, n):
    return tuple(a[i:i+n] for i in range(0, len(a), n))
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
n = 3
s = fn(a, n)
print(s)
