N = int(input("N = "))
A = set()
for i in range(N):
    a = int(input())
    A.add(a)
X = int(input("X = "))
for h in A:
    if h <= X:
        b = h
print(b)