import random

caracteres = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

longitud = int(input("Introduce la longitud de la contraseña: "))

contrasena = ""

for i in range(longitud):
    contrasena += random.choice(caracteres)

print("Tu contraseña generada es:", contrasena)
