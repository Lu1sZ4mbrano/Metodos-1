from sympy import symbols, pi, cos, sin, integrate

# Define las variables simbólicas
t = symbols('t')

# Parametrización del círculo de radio 1 en el plano xy
x_func = cos(t)  # Parametrización de x
y_func = sin(t)  # Parametrización de y

# Define el campo vectorial F(x, y) en términos de las variables simbólicas
F_x = -y_func / x_func**2 + y_func**2
F_y = x_func / y_func**2 + x_func**2

# Integra el producto punto entre el campo vectorial y el vector de desplazamiento sobre el círculo
# desde 0 a π en sentido contrario a las agujas del reloj
work_clockwise = integrate(F_x * x_func.diff(t) + F_y * y_func.diff(t), (t, 0, pi))

# desde 0 a −π en sentido de las agujas del reloj
work_anticlockwise = integrate(F_x * x_func.diff(t) + F_y * y_func.diff(t), (t, 0, -pi))

print("Trabajo en sentido contrario a las agujas del reloj:", work_clockwise)
print("Trabajo en sentido de las agujas del reloj:", work_anticlockwise)