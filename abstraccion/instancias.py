from Cuadrado import Cuadrado
from Hexagono import Hexagono
from Rectangulo import Rectangulo
from Triangulo import Triangulo
from Circulo import Circulo

c = Cuadrado(4)
h = Hexagono(8, 12)
r = Rectangulo(4, 9)
t = Triangulo(8, 10)
ci = Circulo(12)

print('Cuadrado')
print(f'el perimetro del cuadrado es: {c.perimetro()}')
print(f'el area del cuadrado es: {c.area()}')

print('Hexagono')

print(f'el perimetro del hexagono es: {h.perimetro()}')
print(f'el area del hexagono es: {h.area()}')

print('Rectangulo')

print(f'el perimetro del rectangulo es: {r.perimetro()}')
print(f'el area del rectangulo es: {r.area()}')

print('Triangulo')

print(f'el perimetro del triangulo es: {t.perimetro()}')
print(f'el area del triangulo es: {t.area()}')

print('Circulo')
print(f'el area del circulo es: {ci.area()}')
print(f'el perimetro del circulo es: {ci.perimetro()}')