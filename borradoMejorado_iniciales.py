import random

# 1. Generación de la lista de 100 notas aleatorias entre 0 y 10
# Usamos comprensión de listas en lugar de un bucle while para crear la lista en una sola instrucción
notas = [random.randint(0, 10) for _ in range(100)]

# 2. Contamos los ceros antes de eliminarlos para mantener tu mensaje informativo original
num_ceros = notas.count(0)
print(f"En mi lista tengo {num_ceros} ceros.")

# 3. Borrado optimizado (Complejidad lineal O(n))
# Creamos una nueva lista conservando únicamente las notas distintas de 0.
# El operador [:] modifica la lista 'notas' original en memoria (in-place) sin crear otra variable.
notas[:] = [nota for nota in notas if nota != 0]

# 4. Mostramos la nueva longitud y el contenido final de la lista sin ceros
print(len(notas), notas)
