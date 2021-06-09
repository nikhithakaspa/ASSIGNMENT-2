# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1USD4abHZ4RPfVuPo4IFI-sKxhX5lxZiF
"""

# -*- coding: utf-8 -*-
"""Quadilateral:2.ipynb
Automatically generated by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/1QSBS7HsfjVJlqaGYzWAF31cTQUQB52RA
"""

import matplotlib.pyplot as plt
T, R, U, E = (-2, 3.46), (0, 0), (3,0), (3.39,3.38)
 
 
def line_gen(C1, C2):
    return ((C1[0], C2[0]), (C1[1], C2[1]))
 
 
l1 = line_gen(T, R)
l2 = line_gen(R, U)
l3 = line_gen(U, E)
l4 = line_gen(E, T)

 
 
def drawLine(line):
    plt.plot(line[0], line[1])
    
def drawVertix(coordinate, name):
    plt.plot(coordinate[0], coordinate[1], 'o')
    plt.text(coordinate[0] * (1 + 0.1), coordinate[1] * (1 - 0.1) , name)
 
 
# drawing Quadrilateral
drawLine(l1)
drawLine(l2)
drawLine(l3)
drawLine(l4)

 
# plotting vertices
drawVertix(T, "T")
drawVertix(R, "R")
drawVertix(U, "U")
drawVertix(E,"E") 
 
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Quadrilateral TRUE')
plt.grid()
plt.show()