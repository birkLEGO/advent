from math import isqrt

n = 15
lst = list(range(1, n+1))

def sums(ls):
    return [ls[i] + ls[i + 1] for i in range(len(ls) - 1)]

def is_square(n):
    x = isqrt(n)
    return x * x == n

def backtrack(path, remaining):
    if not remaining:
        print(path)
        return True
    for i, num in enumerate(remaining):
        if not path or is_square(path[-1] + num):
            if backtrack(path + [num], remaining[:i] + remaining[i+1:]):
                return True
    return False

def main(la):
    backtrack([], la)

main(lst)