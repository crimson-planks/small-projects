import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
print()
plt.style.use('_mpl-gallery')
'''
This is done by defining e^^x for -1<=x<=0
(There is an equal sign since the piecewise parts have to be continuous anyway :D)
e^^x =
      { f(x) (-1<=x<0)
      { ln(e^^(x+1)) (x<=-1)
      { e^(e^^(x-1)) (x>=0) (numpy has 'log' to mean natural logarithm)
so, I calculated a cubic function(f) such that the derivative of e^^x at x=0⁺ equals the derivative of e^^x at x=0⁻
and since lim(x→0⁺)f(x) = lim(x→-1⁺)(e^f(x)),
lim(x→-1⁺)(e^f(x)) = lim(x→0⁻)f(x) (this is better since I can solve it for f)
conditions: e^^x is continuous (trivial since f is polynomial, e^x is continuous.), f is differentiable, f is twice differentiable.
f(0) = 1
f(-1) = 0
e^f(-1) = f(0) (The first two conditions imply this condition)
(d/dx)(e^f(x))(-1) = f'(0)
(d/dx)(d/dx)(e^f(x))(-1) = f''(0)
4 conditions requires f to be cubic to be determined,
and in that case, f(x) = 1 + (6-2√6)x + (15 - 6√6)x^2 + (10 - 4√6)x^3

you can make more accurate approximations by making it 3 times differentiable, or even infinite times

'''
a1 = 6 - 2*np.sqrt(6)
a2 = (-a1**3 -2*a1**2 -36*a1 +36)/(6*a1 - 24)
quartic_approximation= np.array([1, a1, a2, 2*a2 -a1**2/3, -a1**2/4 + a2])
print(quartic_approximation)
cubic_approximation = np.array([1,6 - 2*np.sqrt(6),15 - 6*np.sqrt(6),10 - 4*np.sqrt(6),0])
linear_approximation = np.array([1,1,0,0,0])
def e_tetration_base_case(x: np.float64,polynomial):
   return polynomial[0]+polynomial[1]*x+polynomial[2]*x*x+polynomial[3]*x**3+polynomial[4]*x**4
def e_tetration_base_case_derivative(x: np.float64,polynomial):
   return polynomial[1]+polynomial[2]*2*x+polynomial[3]*3*x**2+4*polynomial[4]*x**3
def e_tetration_base_case_2derivative(x: np.float64,polynomial):
   return polynomial[2]*2+polynomial[3]*6*x+12*polynomial[4]*x**2
def e_tetration(x: np.float64,polynomial):
    if -1<x<=0:
       return e_tetration_base_case(x,polynomial)
    if x<=-1:
       return np.log(e_tetration(x+1,polynomial))
    return np.exp(e_tetration(x-1,polynomial))

def e_tetration_derivative(x: np.float64,polynomial):
   if -1<x<=0:
      return e_tetration_base_case_derivative(x,polynomial)
   if x<=-1:
      return (1/e_tetration(x+1,polynomial))*e_tetration_derivative(x+1,polynomial)
   return np.exp(e_tetration(x-1,polynomial))*e_tetration_derivative(x-1,polynomial)

def e_tetration_2derivative(x: np.float64,polynomial):
   if -1<x<=0:
      return e_tetration_base_case_2derivative(x,polynomial)
   if x<=-1:
      return (e_tetration(x+1,polynomial)*e_tetration_2derivative(x+1,polynomial)-e_tetration_derivative(x+1,polynomial)**2)/(e_tetration(x+1,polynomial)**2)
   return np.exp(e_tetration(x-1,polynomial))*(e_tetration_2derivative(x-1,polynomial)+e_tetration_derivative(x-1,polynomial)**2)
# make data
x = np.linspace(-1.95, 2.1, 1024)
y_quartic = np.array([e_tetration(num,quartic_approximation) for num in np.nditer(x)])
#yd_quartic = np.array([e_tetration_derivative(num,quartic_approximation) for num in np.nditer(x)])

y_cubic = np.array([e_tetration(num,cubic_approximation) for num in np.nditer(x)])
#yd_cubic = np.array([e_tetration_derivative(num,cubic_approximation) for num in np.nditer(x)])

y_linear =np.array([e_tetration(num,linear_approximation) for num in np.nditer(x)])
#yd_linear =np.array([e_tetration_derivative(num,linear_approximation) for num in np.nditer(x)])

# plot
fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')

ax.plot(x, y_quartic, linewidth=2.0, label="quartic", color="#10507f")
#ax.plot(x, yd_quartic, linewidth=2.0, label="quartic'", color="#5090bf")
ax.plot(x, y_cubic, linewidth=2.0, label="f(x) = (10 - 4√6)x^3 + (15 - 6√6)x^2 + (6-2√6)x + 1", color="#1010af")
#ax.plot(x, yd_cubic, linewidth=2.0, label="(d/dx)(cubic)", color="#5050ff")
#ax.plot(x, y_linear, linewidth=2.0, label="linear", color="#10af10")
#ax.plot(x, yd_linear, linewidth=2.0, label="(d/dx)(linear)", color="#50ff50")

#ax.plot(np.repeat(-1,512), np.linspace(-5,5,512), linewidth=1.0, label="x=-1")
#ax.plot(np.repeat(0,512), np.linspace(-5,5,512), linewidth=1.0, label="x=0")
ax.annotate("vertical asymptote at -x→2⁺", (-1.875,-4))
plt.title('quartic approximation of natural tetration (thrice differentiable)')
plt.xlabel('x label')
plt.ylabel('y label')
ax.legend()
fig.savefig("quartic_approximation_of_natural_tetration.png")

plt.show()