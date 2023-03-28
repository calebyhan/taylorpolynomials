import math
import matplotlib.pyplot as plt
import numpy as np

def e_approx(x, n):
    approx = 0
    for i in range(n):
        approx += x ** i / math.factorial(i)
    return approx

def determine_error(function, original):
    i = 1
    error = 2
    while error > 1e-15:
        approx = function(1, i)
        exact = original(1)
        error = abs(approx - exact)
        print(f'{i} terms: Approx = {approx}, Exact = {exact}, Error = {error}')
        i += 1

determine_error(e_approx, math.exp)

def cos_approx(x, n):
    approx = 0
    for i in range(n):
        coef = (-1) ** i
        num = x ** (2 * i)
        denom = math.factorial(2 * i)
        approx += coef * (num / denom)
    return approx

# angles = np.arange(-2*np.pi,2*np.pi,0.1)
# p_cos = np.cos(angles)
# t_cos = [cos_approx(angle,3) for angle in angles]

# fig, ax = plt.subplots()
# ax.plot(angles,p_cos)
# ax.plot(angles,t_cos)
# ax.set_ylim([-5,5])
# ax.legend(['cos() function','Taylor Series - 3 terms'])

# plt.show()
