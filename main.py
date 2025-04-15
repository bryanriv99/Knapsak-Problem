import numpy as np

# Definir productos y caracteristicas
nombre = ['Decoy Detonators', 'Love Potion', 'Extendable Ears', 'Skivin Snackbox', 'Fever Fudge', 'Puking Pastilles', 'Nosebleed Nougat']
peso = [4, 2, 5, 5, 2, 1.5, 1]
precio = [10, 8, 12, 6, 3, 2, 2]
sumasRuleta = []

# Cantidad de productos
cantDecoy = 10
cantLove = 10
cantEars = 10
cantSnack = 10
cantFudge = 10
cantPastilles = 10
cantNougat = 10

# Solicitar al usuario la cantidad de cromosomas
cantidad_cromosomas = 10


# Generar cromosomas
cromosomas = []
pesoTotal = 0
for _ in range(cantidad_cromosomas):
    cromosoma = [0] * 7
    cromosoma[1] = 3  # Por defecto, el gen en el indice 1 tiene 3 objetos
    cromosoma[3] = 2  # Por defecto, el gen en el indice 3 tiene 2 objetos
    pesoTotal = (peso[1] * 3) + (peso[3] * 2)  # Peso inicial con los valores por defecto

    for i in range(7):
        if i == 1:
            while True:
                num = np.random.randint(3, 11)  # Generar un numero aleatorio entre 3 y 10
                varTemp = peso[i] * num
                if pesoTotal - (peso[i] * 3) + varTemp <= 30:
                    cromosoma[i] = num
                    pesoTotal = pesoTotal - (peso[i] * 3) + varTemp
                    break

        elif i == 3:
            while True:
                num = np.random.randint(2, 11)  # Generar un numero aleatorio entre 2 y 10
                varTemp = peso[i] * num
                if pesoTotal - (peso[i] * 2) + varTemp <= 30:
                    cromosoma[i] = num
                    pesoTotal = pesoTotal - (peso[i] * 2) + varTemp
                    break

        else:
            while True:
                num = np.random.randint(0, 11)
                varTemp = peso[i] * num
                if pesoTotal + varTemp <= 30:
                    cromosoma[i] = num
                    pesoTotal += varTemp
                    break

    cromosomas.append(cromosoma)

cromosomaMayor = []
valorMasGrande = 0


# Seleccion ruleta

for i in range(cantidad_cromosomas):
    suma = 0
    for j in range(7):
        valores = precio[j]
        multi = cromosomas[i][j] * valores
        suma = suma + multi
    sumasRuleta.append(suma)

sumaAptitudes = 0

for i in range(10):
    sumaAptitudes = sumaAptitudes + sumasRuleta[i]

Psel = []

for i in range(10):
    div = sumasRuleta[i] / sumaAptitudes
    Psel.append(div)

Psel_acum = []

sumPsel_acum = 0
for i in range(10):
    sumPsel_acum = sumPsel_acum + Psel[i]
    Psel_acum.append(sumPsel_acum)

valorAleatorio1 = np.random.rand()

# Verifica cual numero es mayor para seleccionar el primer cromosoma

for i in range(10):
    if valorAleatorio1 <= Psel_acum[i]:
        indice = i
        break


valorAleatorio2 = np.random.rand()

for i in range(10):
    if valorAleatorio2 <= Psel_acum[i]:
        indice2 = i
        break

for i in range(50):
    padre1 = cromosomas[indice]
    padre2 = cromosomas[indice2]

    # Cruzar cromosomas
    Pc = 0.85
    umbral = 0.5
    Pm = 0.1
    aleatorioCruza = np.random.rand()
    hijo1 = []
    hijo2 = []
    # Si el numero es mayor a 0.85 se cruzan, si no, no

    if aleatorioCruza < Pc:
        aleatorioCruza2 = np.random.rand()

        # Si es mayor hijo1 = padre1 y si es menor hijo1 = padre2
        for i in range(7):
            if aleatorioCruza2 > umbral:
                hijo1.append(padre1[i])
                hijo2.append(padre2[i])
            else:
                hijo1.append(padre2[i])
                hijo2.append(padre1[i])
        # Termina cruza

    else:
        # Si no se cruzan, los hijos son copias de los padres
        hijo1 = padre1[:]
        hijo2 = padre2[:]

    # Inicia la mutación
    for i in range(7):
        aleatorioMutacion = np.random.rand()
        if aleatorioMutacion < Pm:
            if hijo1[i] < 10 and (sum(peso[j] * hijo1[j] for j in range(7)) + peso[i] <= 30):
                hijo1[i] = hijo1[i] + 1
            elif hijo1[i] > 0:
                hijo1[i] = hijo1[i] - 1
        aleatorioMutacion2 = np.random.rand()
        if aleatorioMutacion2 < Pm:
            if hijo2[i] < 10 and (sum(peso[j] * hijo2[j] for j in range(7)) + peso[i] <= 30):
                hijo2[i] = hijo2[i] + 1
            elif hijo2[i] > 0:
                hijo2[i] = hijo2[i] - 1

    # Inicia el reemplazo
    # Evaluar los cromosomas mas aptos
    precioTotalPadre1 = 0
    precioTotalPadre2 = 0
    precioTotalHijo1 = 0
    precioTotalHijo2 = 0
    valorPrecios = []
    cromosomasOrdenados = []
    for i in range(7):
        precioTotalPadre1 = precioTotalPadre1 + padre1[i] * precio[i]
        precioTotalPadre2 = precioTotalPadre2 + padre2[i] * precio[i]
        precioTotalHijo1 = precioTotalHijo1 + hijo1[i] * precio[i]
        precioTotalHijo2 = precioTotalHijo2 + hijo2[i] * precio[i]

    valorPrecios.append(precioTotalPadre1)
    valorPrecios.append(precioTotalPadre2)
    valorPrecios.append(precioTotalHijo1)
    valorPrecios.append(precioTotalHijo2)

    cromosomasOrdenados.append(padre1)
    cromosomasOrdenados.append(padre2)
    cromosomasOrdenados.append(hijo1)
    cromosomasOrdenados.append(hijo2)

    # Ordenar cromosomas y precios juntos
    cromosomas_y_precios = list(zip(cromosomasOrdenados, valorPrecios))
    cromosomas_y_precios.sort(key=lambda x: x[1], reverse=True)

    # Desempaquetar cromosomas y precios ordenados
    cromosomasOrdenados, valorPrecios = zip(*cromosomas_y_precios)

    # Asignar los padres mas aptos
    padre1 = cromosomasOrdenados[0]
    padre2 = cromosomasOrdenados[1]

    cromosomaMayor = cromosomasOrdenados[0]
    valorMasGrande = valorPrecios[0]

print('Cromosoma mas apto:', cromosomaMayor)
print('Precio total:', valorMasGrande)

for i in range(7):
    print('Producto:', nombre[i], '  Cantidad:', cromosomaMayor[i], '  Precio:', precio[i], '  Peso:', peso[i])