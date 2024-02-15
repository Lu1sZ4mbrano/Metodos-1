import numpy as np

# Definir los vectores como matrices numpy
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.array([3, 2, 1])
d = np.array([6, 5, 4])

# (a) Operaciones con vectores
result_a = a + b + c + d
result_b = a + b - c - d
result_c = a - b + c - d
result_d = -a + b - c + d

# (b) Ángulo entre vectores y los vectores base e1, e2, e3
base_vectors = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
angles_a = np.arccos(np.dot(a, base_vectors.T) / (np.linalg.norm(a) * np.linalg.norm(base_vectors, axis=1)))
angles_b = np.arccos(np.dot(b, base_vectors.T) / (np.linalg.norm(b) * np.linalg.norm(base_vectors, axis=1)))
angles_c = np.arccos(np.dot(c, base_vectors.T) / (np.linalg.norm(c) * np.linalg.norm(base_vectors, axis=1)))
angles_d = np.arccos(np.dot(d, base_vectors.T) / (np.linalg.norm(d) * np.linalg.norm(base_vectors, axis=1)))

# (c) Magnitud de los vectores
magnitude_a = np.linalg.norm(a)
magnitude_b = np.linalg.norm(b)
magnitude_c = np.linalg.norm(c)
magnitude_d = np.linalg.norm(d)

# (d) Ángulo entre a y b, y entre c y d
angle_ab = np.arccos(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
angle_cd = np.arccos(np.dot(c, d) / (np.linalg.norm(c) * np.linalg.norm(d)))

# (e) Proyección de a sobre b
projection_ab = np.dot(a, b) / np.linalg.norm(b) ** 2 * b

# (f) ¿Son los vectores a, b, c, d coplanares?
coplanar = np.isclose(np.dot(np.cross(a, b), np.cross(c, d)), 0)

# (g) Producto punto entre (a + b) y (c + d)
dot_product = np.dot(a + b, c + d)

# (h) Productos cruz entre a × b, b × c, c × d y ángulos con d
cross_ab = np.cross(a, b)
cross_bc = np.cross(b, c)
cross_cd = np.cross(c, d)
angle_cross_cd_d = np.arccos(np.dot(cross_cd, d) / (np.linalg.norm(cross_cd) * np.linalg.norm(d)))

# (i) c . (a x b)
dot_cross_ab_c = np.dot(c, np.cross(a, b))

# Mostrar resultados
print("(a) Resultados de las operaciones con vectores:")
print("a + b + c + d =", result_a)
print("a + b - c - d =", result_b)
print("a - b + c - d =", result_c)
print("-a + b - c + d =", result_d)

print("\n(b) Ángulos entre los vectores y los vectores base e1, e2, e3:")
print("Ángulos de a con e1, e2, e3:", angles_a)
print("Ángulos de b con e1, e2, e3:", angles_b)
print("Ángulos de c con e1, e2, e3:", angles_c)
print("Ángulos de d con e1, e2, e3:", angles_d)

print("\n(c) Magnitudes de los vectores:")
print("Magnitud de a:", magnitude_a)
print("Magnitud de b:", magnitude_b)
print("Magnitud de c:", magnitude_c)
print("Magnitud de d:", magnitude_d)

print("\n(d) Ángulo entre a y b, y entre c y d:")
print("Ángulo entre a y b:", angle_ab)
print("Ángulo entre c y d:", angle_cd)

print("\n(e) Proyección de a sobre b:")
print("Proyección de a sobre b:", projection_ab)

print("\n(f) ¿Son los vectores a, b, c, d coplanares?")
print("¿Los vectores son coplanares?:", coplanar)

print("\n(g) Producto punto entre (a + b) y (c + d):")
print("(a + b) · (c + d) =", dot_product)

print("\n(h) Productos cruz entre a × b, b × c, c × d y ángulos con d:")
print("Producto cruz entre a × b:", cross_ab)
print("Producto cruz entre b × c:", cross_bc)
print("Producto cruz entre c × d:", cross_cd)
print("Ángulo entre c × d y d:", angle_cross_cd_d)
print("\n(i) Producto punto c por producto cruz a x b:", dot_cross_ab_c)