import numpy as np
import math

M = np.array([[0.85,0,0.5],[0.05,0.95,0.5],[0.1,0.5,0.3]])
c = np.array([0.4,0.3,0.3])
y = np.linalg.solve(M,c)

print(y)
