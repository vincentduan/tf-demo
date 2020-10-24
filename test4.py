import matplotlib.pyplot as plt
import numpy as np
from test3 import df

# 将df中0到100行的数据的第四列赋值给y向量 
y = df.loc[0:100, 4].values
# 将Iris-setosa转为-1,其余转为1
y = np.where(y == 'Iris-setosa', -1, 1)
# 将df0到100行的数据的第0列和第2列抽取出来，赋值给x向量
X = df.iloc[0:100, [0, 2]].values
# 将X向量的钱50条数据的第0列作为x轴，第1列作为y轴坐标，画在二维坐标轴，画出来的点是红色的'o',
plt.scatter(X[:50, 0], X[:50, 1], color = 'red', marker='o', label='setosa')
plt.scatter(X[50:100, 0], X[50:100, 1], color = 'blue', marker='x', label='versicolor')
plt.xlabel('花瓣长度')
plt.ylabel('花径长度')
plt.legend(loc='upper left')
# 下面两行解决乱码问题
plt.rcParams['font.sans-serif'] = ['KaiTi'] # 指定默认字体
plt.rcParams['axes.unicode_minus'] = False

plt.show()