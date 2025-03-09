import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置随机种子，保证复现性
np.random.seed(0)

# 离散化
L = 10  # 积分长度
fs = 1e-3  # 采样率
x = np.arange(0, L + fs, fs)  # x 的范围
y = x ** 2  # y = x^2 曲线
S = L * (L ** 2)  # 样本空间面积

# 在区间内撒样本
N_Lis = [int(1e1), int(1e2), int(1e3), int(1e4)]  # 样本个数列表

# 求解定积分 (解析解)
res_integ = 1 / 3 * (10 ** 3 - 0 ** 3)  # 解析解

# 创建绘图
fig, axs = plt.subplots(2, 2, figsize=(14, 7))

for n, ax in zip(N_Lis, axs.ravel()):
    cnt = 0
    x_random = L * np.random.rand(n)  # 随机点 x
    y_random = L ** 2 * np.random.rand(n)  # 随机点 y

    # 统计落在曲线下的点
    for i in range(n):
        if y_random[i] <= x_random[i] ** 2:
            cnt += 1

    # 近似解
    res_appro = cnt / n * S

    # 绘制曲线和随机点
    ax.plot(x, y, 'k', linewidth=2, label="y=x^2")
    ax.fill_between(x, y, color='cyan', alpha=0.5, label="积分区域")
    ax.scatter(x_random, y_random, c='r', s=10, alpha=0.5, label="随机点")
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title(f"解析解≈{res_integ:.1f}   近似解≈{res_appro:.1f}")
    ax.legend(fontsize=10)
    ax.grid()

# 设置总标题
fig.suptitle('求解 y=x^2 定积分', fontsize=18)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
