import numpy as np

class Perceptron(object):
    """
    eta: 学习率
    n_iter: 权重向量的训练次数
    w_: 神经分叉权重向量
    errors_: 用于记录神经元判断出错次数
    """
    def __init__(self, eta = 0.01, n_iter = 10):
        self.eta = eta
        self.n_iter = n_iter
        pass
    
    def fit(self, X, y):
        """
        输入训练数据，培训神经元，X表示输入样本, y对应样本的正确分类
        X: shape[n_samples, n_features]
        n_samples:表示有多少个训练样本数量
        n_features: 表示有多少个属性
        例如：X: [[1,2,3], [4,5,6]] => n_samples=2;n_features=3

        y: [1, -1]表示第一个向量的分类是1, 第二个向量的分类是-1
        """

        """
        首先初始化权重为0
        加一是因为激活函数w0,也就是阈值,这样就只用判断输出结果是否大于0就可以了
        """
        self.w_ = np.zeros(1 + X.shape[1])
        self.errors_ = []

        """
		只要出现错误分类，那么反复训练这个样本，次数是n_iter
		"""
        for _ in range(self.n_iter): 
            errors = 0
            """
            X:[[1,2,3], [4,5,6]]
            y:[1, -1]

            zip(X, y) => [[1,2,3,1], [4,5,6-1]]
            """
            for xi, target in zip(X,y):
                """
                update = η * (y-y')
                """
                print("target:")
                print(target)
                update = self.eta * (target - self.predict(xi))
                print("update:")
                print(update)
                """
                xi 是一个向量, 例如[1,2,3], target表示1
                update 是一个常量
                update*xi 等价于 [Δw(1) = X[1]*update, Δw(2) = X[2]*update, Δw(3) = X[3]*update]
                """
                # w_[1:]表示w忽略第0个元素，从第一个元素开始往后
                self.w_[1:] += update * xi
                self.w_[0] += update * 1
                errors += int(update != 0.0)
                self.errors_.append(errors)
            pass
        pass
    pass

    def net_input(self, X):
        """
        z = W0*1 + W1*X1 + W2*X2+ ...+ Wn*Xn
        """
        print("net_input:")
        result = np.dot(X, self.w_[1:]) + self.w_[0]
        print(result)
        return result

    def predict(self, X):
        """
        如果self.net_input(X) >= 0.0返回1, 否则返回-1
        """
        result = np.where(self.net_input(X) >= 0.0 , 1, -1)
        print("predict:")
        print(result)
        return result