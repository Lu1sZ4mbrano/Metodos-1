import numpy as np

q1 = np.array([[0, 1, 0, 0], [-1, 0, 0, 0], [0, 0, 0, 1], [0, 0, -1, 0]])
q2 = np.array([[0, 0, 0, -1], [0, 0, -1, 0], [0, 1, 0, 0], [1, 0, 0, 0]])
q3 = np.array([[0, 0, -1, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, -1, 0, 0]])
q0 = np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])

# revisamos si cumple la tabla de multiplicacion
if (np.dot(q0, q0) == q0).all() and \
    (np.dot(q1, q1) == -q0).all() and \
    (np.dot(q2, q2) == -q0).all() and \
    (np.dot(q3, q3) == -q0).all() and \
    (np.dot(q1, q0) == q1).all() and \
    (np.dot(q2, q0) == q2).all() and \
    (np.dot(q3, q0) == q3).all() and \
    (np.dot(q0, q1) == q1).all() and \
    (np.dot(q0, q2) == q2).all() and \
    (np.dot(q0, q3) == q3).all() and \
    (np.dot(q1, q2) == q3).all() and \
    (np.dot(q2, q1) == -q3).all() and \
    (np.dot(q1, q3) == -q2).all() and \
    (np.dot(q3, q1) == q2).all() and \
    (np.dot(q2, q3) == q1).all() and \
    (np.dot(q3, q2) == -q1).all():
    print("REPRESENTAN BASE PARA LOS CUATERNIONES")
else:
    print("NO REPRESENTAN BASE PARA LOS CUATERNIONES")
