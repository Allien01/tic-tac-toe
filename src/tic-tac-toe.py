entrada = input("Enter cells: ").replace("_", " ")
print("---------")
print("| " + entrada[0] + " " + entrada[1] + " " + entrada[2] + " |")
print("| " + entrada[3] + " " + entrada[4] + " " + entrada[5] + " |")
print("| " + entrada[6] + " " + entrada[7] + " " + entrada[8] + " |")
print("---------")

# definindo uma funcao auxiliar para verificar jogadas
def verifica(x):
    acumulador = 0
    for i in x:
        if i == "XXX":
            resultado = "X wins"
            acumulador += 1
        elif i == "OOO":
            resultado = "O wins"
            acumulador += 1
    if acumulador > 1:
        print("Impossible")
        quit()
    elif acumulador == 1:
        print(resultado)
        quit()

# separando a entrada em uma matriz 3x3 para avaliar o jogo
linhas = []
for i in range(0, 10, 3):
    if i != 0:
        start = i - 3
        linhas.append(list(entrada[start : i]))

# separando a a matriz por linhas
line = []
for i in range(3):
    x = ' '
    for j in range(3):
        x += linhas[i][j]
    line.append(x.lstrip())

# separando a matriz por colunas
column = []
for j in range(3):
    y = ' '
    for i in range(3):
        y += linhas[i][j]
    column.append(y.lstrip())

# separando a lista em diagonais
diagonal1 = []
diagonal = ' '
for i in range(3):
    diagonal += linhas[i][i]
diagonal1.append(diagonal.lstrip())
diagonal2 = []
diagonals = linhas[0][2] + linhas[1][1] + linhas[2][0]
diagonal2.append(diagonals)

# funcao verifica coluna e linha, diagonal1 e diagonal2
verifica(line)
verifica(column)
verifica(diagonal1)
verifica(diagonal2)

# Testando se o jogo não terminou
count = 0
xis = 0
zero = 0
for i in range(3):
    for j in range(3):
        if linhas[i][j] == ' ':
            count += 1
        elif linhas[i][j] == 'X':
            xis += 1
        else:
            zero += 1
# Testando se empatou
if count == 0:
    print("Draw")
# Testando a falha no jogo
elif abs( xis - zero) >= 2:
    print("Impossible")
elif abs( xis - zero) == 0 or abs( xis - zero) == 1:
    print("Game not finished")
