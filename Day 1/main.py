from random import randint
list = []
P = 2
Q = 4
S = 12
a, b, c, d = 0, 0, 0, 0
def g():
    a, b, c, d = randint(P, Q), randint(P, Q), randint(P, Q), randint(P, Q)
    if a + b + c + d == S:
        ls = [a, b, c, d]
        if not any(sorted(sublist) == sorted(ls) for sublist in list):
            list.append(ls)
def main():
    for _ in range (0, 1000000):
        g()
    print(list)
if __name__ == '__main__':
    main()
