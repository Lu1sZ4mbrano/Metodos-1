# Definir los puntos
def input_punto(cordenada):
    x = float(input(f"Ingrese la coordenada x: {cordenada} "))
    y = float(input(f"Ingrese la coordenada y: {cordenada} "))
    return (x, y)
p1 = input_punto("punto 1")
p2 = input_punto("punto 2")
p3 = input_punto("punto 3")

def calcular_centroide(p1, p2, p3): # usar formula de centroide
    x = (p1[0] + p2[0] + p3[0]) / 3
    y = (p1[1] + p2[1] + p3[1]) / 3
    return (x, y)

centroide = calcular_centroide(p1, p2, p3)
print("El centroide del triángulo es: ", centroide)