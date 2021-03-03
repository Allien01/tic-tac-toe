entrada = input("Enter cells: ")
print("---------")
print("| " + entrada[0] + " " + entrada[1] + " " + entrada[2] + " |")
print("| " + entrada[3] + " " + entrada[4] + " " + entrada[5] + " |")
print("| " + entrada[6] + " " + entrada[7] + " " + entrada[8] + " |")
print("---------")

# separando a entrada em uma lista com 3 listas para avaliar o jogo
linhas = []
for i in range(0, 10, 3):
    if i != 0:
        start = i - 3
        linhas.append(list(entrada[start : i]))

# separando a lista em linhas
y = []
for i in range(3):
    line = ' '
    for j in range(3):
        line += linhas[i][j]
        # colunas.append(linhas[i][j])
    y.append(line.lstrip())


# verificando as entradas das linhas
acumulador = 0
for i in y:
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


# separando a lista por colunas
x = []
for j in range(3):
    colunas = ' '
    for i in range(3):
        colunas += linhas[i][j]
        # colunas.append(linhas[i][j])
    x.append(colunas.lstrip())

# verificando as entradas da colunas
acumulador2 = 0
for i in x:
    if i == "XXX":
        resultado = "X wins"
        acumulador2 += 1
    elif i == "OOO":
        resultado = "O wins"
        acumulador2 += 1
if acumulador2 > 1:
    print("Impossible")
    quit()
elif acumulador2 == 1:
    print(resultado)
    quit()

#separando a lista em diagonais
z = []
diagonal1 = ' '
for i in range(3):
    diagonal1 += linhas[i][i]
z.append(diagonal1.lstrip())

diagonal2 = linhas[0][2] + linhas[1][1] + linhas[2][0]
z.append(diagonal2)


# verificando as entradas das  diagonais
acumulador3 = 0
for i in range(2):
    if z[i] == "XXX":
        resultado = "X wins"
        acumulador3 += 1
        print("testando")
    elif z[i] == "OOO":
        resultado = "O wins"
        acumulador3 += 1
if acumulador3 > 1:
    print("Impossible")
    quit()
elif acumulador3 == 1:
    print(resultado)
    quit()

# Testando se o jogo não terminou
count = 0
xis= 0
zero = 0
for i in range(3):
    for j in range(3):
        if linhas[i][j] == '_':
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
