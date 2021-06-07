from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
iris = load_iris()
x = iris.data # une tableau (150, 4) chaques lignes => une fleur chaque colonne => caractère de la fleur
#0
#1
#2 longeur pétale
y = iris.target # uen liste de x150 [000000, 11111, 22222]






ax = plt.axes(projection='3d')
ax.scatter(x[:, 0], x[:, 1], x[:, 2], c=y, alpha=0.5, s=x[:,2]*100)
plt.savefig('image 2 3d')
plt.show()
