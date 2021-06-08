import matplotlib.pyplot as plt
import numpy as np
from scipy import signal # traitement d'images : https://docs.scipy.org/doc/scipy/reference/ndimage.html
from scipy import fftpack

x = np.linspace(0, 20, 100)
y = x + 4*np.sin(x) + np.random.randn(x.shape[0])
new_y = signal.detrend(y)

plt.figure()
plt.plot(x, y)
plt.plot(x, new_y)
plt.show()

x = np.linspace(0, 30, 1000)
y = 3*np.sin(x) + 2*np.sin(5*x) +np.sin(10*x) + np.random.random(x.shape[0])*10
fourier = fftpack.fft(y)
power = np.abs(fourier)
frequences = fftpack.fftfreq(y.size)

plt.figure()
plt.plot(np.abs(frequences), power)
plt.show()

fourier[power < 400] = 0

plt.figure()
plt.plot(np.abs(frequences), power)
plt.show()

filtered_signal = fftpack.ifft(fourier)

plt.figure(figsize=(12, 8))
plt.plot(x, y, lw=0.5)
plt.plot(x, filtered_signal, lw=3)
plt.show()




