import numpy as np, fractions
width = 4
height = 3
#2x + 3y = 12
#5x + 7y = 50
system_of_linear_equations = np.array([
    [2,3,-12],
    [5,7,-50]
])
system_of_linear_equations = system_of_linear_equations*fractions.Fraction(1,1)
print(system_of_linear_equations)
