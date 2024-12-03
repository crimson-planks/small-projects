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
for eliminating_variable_index in range(width-1):
    reference_index = eliminating_variable_index
    while True:
        if reference_index>=height: break
        if system_of_linear_equations[reference_index][eliminating_variable_index]!=fractions.Fraction(0,1): break
        reference_index+=1
    tmp = system_of_linear_equations[0].copy()
    system_of_linear_equations[0] = system_of_linear_equations[reference_index]
    system_of_linear_equations[reference_index] = tmp
    for ch in range(eliminating_variable_index+1,height):
        mul_number = -fractions.Fraction(system_of_linear_equations[ch][eliminating_variable_index],system_of_linear_equations[0][eliminating_variable_index])
        system_of_linear_equations[ch] = system_of_linear_equations[0]*mul_number + system_of_linear_equations[ch]
    print(reference_index,system_of_linear_equations)
for reference_index in reversed(range(0,height)):
    for ch in range(0,reference_index):
        mul_number = -fractions.Fraction(system_of_linear_equations[ch][reference_index],system_of_linear_equations[reference_index][reference_index])
        system_of_linear_equations[ch] = system_of_linear_equations[reference_index]*mul_number + system_of_linear_equations[ch]
for i in range(0,height):
    mul_number = 1/system_of_linear_equations[i][i]
    system_of_linear_equations[i] = system_of_linear_equations[i]*mul_number
    print(system_of_linear_equations[i][width-1])
print(system_of_linear_equations)