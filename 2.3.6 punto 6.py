from sympy.abc import x, t
import sympy as sp

# Inicialización de impresión con LaTeX
sp.init_printing(use_latex="mathjax")

# Definición de producto interno
def punto(f, g):
    return sp.integrate(f * g * sp.sqrt(1 - t**2), (t, -1, 1))

# Definición de base de polinomios
def base_pol(n):
    return [t**i for i in range(n+1)]

# Algoritmo de Gram-Schmidt para ortogonalización
def gram_schmidt(base):
    ortho_base = [base[0]]
    for i in range(1, len(base)):
        p_i = base[i]
        for j in range(i):
            p_i -= punto(base[i], ortho_base[j]) / punto(ortho_base[j], ortho_base[j]) * ortho_base[j]
        ortho_base.append(p_i)
    return ortho_base

# grado de la base de polinomios
n = 3
print(f'Base de polinomios de grado {n}:', base_pol(n+1))
print('===============================')
# Construcción de la base ortogonal

base = base_pol(n+1)
ortho_base = gram_schmidt(base)

# Impresión de los polinomios ortogonales
for i, p in enumerate(ortho_base):
    print(f'P_{i} = {p}')

