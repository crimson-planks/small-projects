import numpy as np, fractions
width = 4
height = 3
#2x + 3y = 12
#5x + 7y = 50
system_of_linear_equations = np.array([
    [1,1,0,3],
    [0,1,1,6],
    [1,0,1,5]
])
system_of_linear_equations = system_of_linear_equations*fractions.Fraction(1,1)