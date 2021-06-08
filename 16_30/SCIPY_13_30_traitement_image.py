# traitement d'image scipy https://docs.scipy.org/doc/scipy/reference/ndimage.html
import matplotlib.pyplot as plt
import numpy as np
from scipy import ndimage

np.random.seed(0)
X = np.zeros((32, 32))
X[10:-10, 10:-10] = 1
X[np.random.randint(0, 32, 30), np.random.randint(0, 32, 30)] = 1
#plt.imshow(X)
#plt.show()

open_x = ndimage.binary_opening(X)
#plt.imshow(open_x)
#plt.show()

image = plt.imread('bacteria.png')
image = image[:,:,0]

#plt.imshow(image, cmap='gray')
#plt.show()

image_2 = np.copy(image)

plt.hist(image_2.ravel(), bins=255)
plt.show()

image = image < 0.6
plt.imshow(image)
plt.show()

open_image = ndimage.binary_opening(image)
plt.imshow(open_image)
plt.show()


label_image, n_labels = ndimage.label(open_image)
plt.imshow(label_image)
plt.show()

sizes = ndimage.sum(open_image, label_image, range(n_labels))
plt.scatter(range(n_labels), sizes)
plt.show()
