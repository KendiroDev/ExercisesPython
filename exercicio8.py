from math import sqrt


x1 = float(input("Digite as coordenadas X do ponto A"))
y1 = float(input("Digite as coordenadas de Y do ponto A"))
x2 = float(input("Digite as coordenadas X do ponto B"))
y2 = float(input("Digite as coordenadas de Y do ponto B"))

print ("Distancia entre os dois pontos")


dist = sqrt ((x2-x1)**2 + (y2-y1)**2)

print ("A distancia entre os dois pontos é de ", dist)