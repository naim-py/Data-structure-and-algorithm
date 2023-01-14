def gcd(n, m):
    if m == 0:
        return n
    else:
        return gcd(m, n % m)
n,m = map(int,input("Enter any two integer number").split())
print(gcd(n,m))