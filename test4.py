import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.colors import ListedColormap
import test2 as t2

file="./iris.csv"
df = pd.read_csv(file, header=None)
# 将df中0到100行的数据的第四列赋值给y向量 
y = df.loc[0:100, 4].values
# 将Iris-setosa转为-1,其余转为1
y = np.where(y == 'Iris-setosa', -1, 1)
# print(y)
# 将df的0到100行的数据的第0列和第2列抽取出来，赋值给x向量
X = df.iloc[0:100, [0, 2]].values

def plot_desision_regions(X, y, classifier, resolution=0.02):
    marker = ('s', 'x', 'o', 'v')
    # 根据y中不同类别,分配不同的颜色
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[: 0].min() - 1, X[:, 0].max
    x2_min, x2_max = X[: 1].min() - 1, X[:, 1].max
    
    print(x1_min, x1_max)
    print(x2_min, x2_max)


ppn = t2.Perceptron(eta=0.1, n_iter=10)
ppn.fit(X, y)
plt.plot(range(1, len(ppn.errors_) + 1), ppn.errors_, marker='o')
plt.xlabel("Epochs")
plt.ylabel("error count")
plt.show()
plot_desision_regions(X, y, ppn, resolution=0.02)
