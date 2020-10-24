from matplotlib.colors import ListedColormap
import numpy as np

def plot_desision_regions(X, y, classifier, resolution=0.02):
    marker = ('s', 'x', 'o', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[: 0].min() - 1, X[:, 0].max
    x2_min, x2_max = X[: 1].min() - 1, X[:, 1].max
    
    print(x1_min, x1_max)
    print(x2_min, x2_max)

plot_desision_regions(X, y, ppn, resolution=0.02)