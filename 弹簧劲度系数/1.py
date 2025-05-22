import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# 数据
length1 = [] # 第一组长度数据
length2 = [] # 第二组长度数据

# 计算平均长度
mean_length = [(length1[i] + length2[i]) / 2 for i in range(len(length1))]
mean_length = np.array(mean_length)

# 计算长度变化量
delta_length = [mean_length[i] - mean_length[0] for i in range(len(mean_length))]
delta_length = np.array(delta_length)
# 格式化数据为 5 位有效数字
length1_1 = [np.format_float_positional(x, precision=5, unique=False, fractional=False, trim='k') for x in length1]
length2_1 = [np.format_float_positional(x, precision=5, unique=False, fractional=False, trim='k') for x in length2]
mean_length_1 = [np.format_float_positional(x, precision=5, unique=False, fractional=False, trim='k') for x in mean_length]
delta_length_1 = [np.format_float_positional(x, precision=5, unique=False, fractional=False, trim='k') for x in delta_length]

# 创建表格数据
data = [
    ["Length 1 (mm)"] + length1_1,
    ["Length 2 (mm)"] + length2_1,
    ["Mean Length (mm)"] + mean_length_1,
    ["ΔL (mm)"] + delta_length_1
]
# 绘制表格
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=[""] + [f"Point {i}" for i in range(len(length1))], loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(length1) + 1)))

plt.show()
# 计算力 F
g = 9.7946  # 重力加速度
F = [float(i * g) for i in range(len(mean_length))]  # 保持单位为 mN
F = np.array(F)
F_1 = [np.format_float_positional(x, precision=5, unique=False, fractional=False, trim='k') for x in F]
data_F = [
    ["ΔL (mm)"] + delta_length_1,
    ["F (mN)"] + F_1
]
# 绘制力 F 的表格
fig_F, ax_F = plt.subplots(figsize=(10, 4))
ax_F.axis('tight')
ax_F.axis('off')
table_F = ax_F.table(cellText=data_F, colLabels=[""] + [f"Point {i}" for i in range(len(length1))], loc='center', cellLoc='center')
table_F.auto_set_font_size(False)
table_F.set_fontsize(10)
table_F.auto_set_column_width(col=list(range(len(length1) + 1)))
plt.show()
# 线性拟合
slope, intercept, r_value, p_value, std_err = linregress(delta_length, F)

# 打印拟合结果和相关系数
print(f"F = {slope:.5f} * ΔL + {intercept:.5f}")
print(f"Correlation coefficient (r): {r_value:.5f}")

# 绘制图像
plt.figure(figsize=(8, 6))
plt.plot(delta_length, F, 'bo', label='Experimental Data')  # 实验数据点
plt.plot(delta_length, slope * delta_length + intercept, 'r-', label=f'Fit: F = {slope:.5f} * ΔL + {intercept:.5f}')  # 拟合线
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x轴
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y轴
plt.text(0.05, 0.95, f"r = {r_value:.5f}", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
# 设置图像属性
plt.xlabel('ΔL (mm)', fontsize=12)
plt.ylabel('F (mN)', fontsize=12)  # 保持单位为 mN
plt.title('F vs ΔL', fontsize=14)
plt.legend()
plt.grid()
plt.show()