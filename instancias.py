from Comic import Comic
from Novela import Novela

batman = Comic('Batma', 'El caballero de la noche', 250, 6, 3)
superman = Comic('Superman', 'Superman regresa', 290, 4, 8)
quijote = Novela('Miguel de Cervantes', 'Don quijote de la mancha', 450, 39, 14)

batman.informacion()
superman.informacion()
quijote.informacion()

batman.valor()
superman.valor()
quijote.valor()

batman.cantidad()
superman.cantidad()
quijote.cantidad()