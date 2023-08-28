import numpy as np

v1 = np.array([13 + 6j, 15 + 21j, 0 + 7j], dtype=complex)
v2 = np.array([35 - 3j, 5 + 9j, 35 + 9j], dtype=complex)
escalar = 15 + 1j

def adicion_de_vectores(vector1, vector2):
    return np.add(vector1, vector2)

def inverso_de_vector(vector):
    return np.negative(vector)

def multiplicacion_escalarxvector(escalar, vector):
    return np.multiply(escalar, vector)

def adicion(matriz1, matriz2):
    return np.add(matriz1, matriz2)

def inversa(matriz):
    return np.negative(matriz)

def multiplicacion_escalarxmatriz(escalar, matriz):
    return np.multiply(escalar, matriz)



m1 = np.array([[3 + 2j, 1 - 1j], [0 + 1j, 22 + 0j]], dtype=complex)
m2 = np.array([[1 + 1j, 2 - 2j], [31 + 0j, 0 + 1j]], dtype=complex)

r_adicion_vectores = adicion_de_vectores(v1, v2)
r_inverso_vector = inverso_de_vector(v1)
r_multiplicacion_escalar_vector = multiplicacion_escalarxvector(escalar, v1)
r_adicion_matrices = adicion(m1, m2)
r_inversa_matriz = inversa(m1)
r_multiplicacion_escalar_matriz = multiplicacion_escalarxmatriz(escalar, m1)

print("Resp adición de vectores:\n", r_adicion_vectores)
print("Resp inverso de vector:\n", r_inverso_vector)
print("Resp multiplicación escalar por vector:\n", r_multiplicacion_escalar_vector)
print("Resp adición de matrices:\n", r_adicion_matrices)
print("Resp nversa de matriz:\n", r_inversa_matriz)
print("Resp multiplicación escalar por matriz:\n", r_multiplicacion_escalar_matriz)
