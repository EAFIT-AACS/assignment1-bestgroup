import sys

def encontrar_Pares_Iguales(n, estado_Final, transicion):
    # Creamos una tabla para marcar pares diferenciados
    marcado = [[False] * n for _ in range(n)]
    
    # Inicialmente se marcan los pares donde uno es final y el otro no lo es.
    for i in range(n):
        for j in range(i + 1, n):
            if ((i in estado_Final) != (j in estado_Final)):
                marcado[i][j] = True

    # Propagamos las diferencias:
    cambiar = True
    while cambiar:
        cambiar = False
        for i in range(n):
            for j in range(i + 1, n):
                if not marcado[i][j]:
                    # Revisamos para cada símbolo si la transición lleva a un par ya marcado.
                    for simbolo in range(len(transicion[0])):
                        ti = transicion[i][simbolo]
                        tj = transicion[j][simbolo]
                        # Aseguramos el orden para consultar en la tabla
                        a, b = (ti, tj) if ti < tj else (tj, ti)
                        if marcado[a][b]:
                            marcado[i][j] = True
                            cambiar = True
                            break

    # Los pares no marcados son equivalentes.
    eq_pares = []
    for i in range(n):
        for j in range(i + 1, n):
            if not marcado[i][j]:
                eq_pares.append((i, j))
    return eq_pares

def main():
    # Se lee el archivo "input.txt"
    with open("input.txt", "r") as f:
        linea = [line.strip() for line in f if line.strip() != ""]

    indice = 0
    # Primer línea: cantidad de casos.
    casos = int(linea[indice])
    indice += 1

    # Para cada caso se procesa la entrada y se calcula el resultadoado.
    for _ in range(casos):
        n = int(linea[indice])
        indice += 1

        # El alfabeto se lee (aunque en este algoritmo se usa solo para determinar
        # la cantidad de columnas en la tabla de transición).
        alfabeto = linea[indice].split()
        indice += 1

        # Se leen los estados finales (convertidos a enteros).
        estado_Final = set(map(int, linea[indice].split()))
        indice += 1

        # Se leen n líneas de la tabla de transición.
        transicion = []
        for i in range(n):
            fila = list(map(int, linea[indice].split()))
            indice += 1
            transicion.append(fila)

        # Se obtienen los pares de estados equivalentes.
        eq_pares = encontrar_Pares_Iguales(n, estado_Final, transicion)

        # Se formatea la salida: cada par se imprime como (i,j) y todos los pares en una línea.
        resultado = " ".join("({},{})".format(p, q) for p, q in eq_pares)
        print(resultado)

if __name__ == "__main__":
    main()
