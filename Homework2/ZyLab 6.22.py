# Dominic Jason 2203959

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = int(input())

solved = False

for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if a * x + b * y == c and d * x + e * y == f:
            solved = True
            print(f'{x} {y}')
if not solved:
    print('No solution')
