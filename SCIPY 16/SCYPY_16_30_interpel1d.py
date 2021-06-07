from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np

#infos
#scipy interpel1d doc https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.interp1d.html#scipy.interpolate.interp1d


x = np.linspace(0, 10, 10)
y = x**2

f = interp1d(x, y, 'linear') #

new_x = np.linspace(0, 10, 30)
result = f(new_x)

plt.figure()
plt.scatter(x, y)
plt.scatter(new_x, result, c='r')
plt.show()

plt.figure()
x = np.linspace(0, 10, 10)
y = np.sin(x)
plt.scatter(x, y)

f = interp1d(x, y, 'cubic')

new_x = np.linspace(0, 10, 50)
result = f(new_x)
plt.scatter(new_x, result)

plt.show()

