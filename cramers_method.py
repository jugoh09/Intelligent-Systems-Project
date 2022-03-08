# Original cramers method

import numpy as np
import math

A0 = np.array([[0.85,0,0.5],[0.05,0.95,0.4],[0.1,0.5,0.3]])
A1 = np.array([[0.4,0,0.5],[0.3,0.95,0.5],[0.3,0.5,0.3]])
A2 = np.array([[0.85,0.4,0.5],[0.05,0.3,0.5],[0.1,0.3,0.3]])
A3 = np.array([[0.85,0,0.4],[0.05,0.95,0.3],[0.1,0.5,0.3]])

#

#determinant of array
Ax0 = np.linalg.det(A0)
Ax1 = np.linalg.det(A1)
Ax2 = np.linalg.det(A2)
Ax3 = np.linalg.det(A3)

#determine value of x,y,z
x = Ax1/Ax0
y = Ax2/Ax0
z = Ax3/Ax0

def round_down(n, decimals=1):
    return round(n,decimals)

print(round_down(x))
print(round_down(y))
print(round_down(z))

