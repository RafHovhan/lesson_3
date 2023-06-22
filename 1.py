N = int(input("N = "))
X = int(input("X = "))
A = []
count = 0

for i in range(N):
    a = int(input("a = "))
    A.append(a)
for h in A:
    if X == h:
        count += 1
print(count)