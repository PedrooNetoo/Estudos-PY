altura = [[0,0],[0,0]]
qtnd = 0

for l in range(2):
    for c in range(2):
        altura[l][c] = float(input("Digite a sua altura: "))
        if altura[l][c] > 1.5:
            qtnd += 1

print(qtnd)