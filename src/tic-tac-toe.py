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


entrada = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
print("---------")
print("|  " + entrada[0][0]+ entrada[0][1]+ entrada[0][2]+ "  |")
print("|  " + entrada[1][0]+ entrada[1][1]+ entrada[1][2]+ "  |")
print("|  " + entrada[2][0]+ entrada[2][1]+ entrada[2][2]+ "  |")
print("---------")

jogada = 0
while True:
    row, col = input("Enter the cordinates: ").split()
    try:
        row = int(row)
        col = int(col)
    except:
        print("You should enter numbers!")
        continue
    x = row -1
    y = col -1
    if (row < 1 or row > 3) or ( col < 1 or col > 3):
        print("Coordinates should be from 1 to 3!")
        continue
    # Testando se a celula esta ocupada
    if entrada[x][y] != " ":
            print("This cell is occupied! Choose another one!")
            continue
    jogada += 1
    # Atualizando a entrada do jogador
    if jogada % 2 != 0:
        entrada[x][y] = "X"
    else:
        entrada[x][y] = "O"

    # imprimindo a matriz com a nova entrada
    print("---------")
    print("| " + entrada[0][0] + " " + entrada[0][1] + " " + entrada[0][2] + " |")
    print("| " + entrada[1][0] + " " + entrada[1][1] + " " + entrada[1][2] + " |")
    print("| " + entrada[2][0] + " " + entrada[2][1] + " " + entrada[2][2] + " |")
    print("---------")

    # separando lista em uma matriz por linhas
    line = []
    for i in range(3):
        x = ' '
        for j in range(3):
            x += entrada[i][j]
            line.append(x.lstrip())

    # separando a matriz por colunas
    column = []
    for j in range(3):
        y = ' '
        for i in range(3):
            y += entrada[i][j]
            column.append(y.lstrip())

    # separando a lista em diagonais
    diagonal1 = []
    diagonal = entrada[0][0] + entrada[1][1] + entrada[2][2]
    diagonal1.append(diagonal)
    diagonal2 = []
    diagonals = entrada[0][2] + entrada[1][1] + entrada[2][0]
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
            if entrada[i][j] == ' ':
                count += 1
            elif entrada[i][j] == 'X':
                xis += 1
            else:
                zero += 1
    # Testando se empatou
    if count == 0:
        print("Draw")
        quit()
    # Testando a falha no jogo
    elif abs( xis - zero) >= 2:
        print("Impossible")
        quit()
