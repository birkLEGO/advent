ls = [11, 13, 19]
def is_prime(n):
    if n % 2 == 0: return n == 2
    if n % 3 == 0: return n == 3
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
def sums(ls):
    return [ls[i] + ls[i+1] for i in range(len(ls)-1)]
def main(ls):
    while not (len(ls) == 1):
        tls = []
        ls = sums(ls)
        for i in ls:
            while not is_prime(i):
                i += 1
            tls.append(i)
        ls = tls
        print(ls)
if __name__ == '__main__':
	main(ls)