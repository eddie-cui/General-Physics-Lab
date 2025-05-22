import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
def keep_first_n_digits(x, n=3):
    x = int(x)
    length = len(str(x))
    if length <= n:
        return str(x)
    return str(round(x, -length + n))
# 数据
g=9.7946  # 重力加速度
f=np.arange(0, 11)  # 力的范围
F=[i*g for i in range(0, 11)]  # 保持单位为 N
xi = []# you need to fill in xi
xi =[x*10**-2 for x in xi]  # 转换为 m
S=3.31*10**-7  # m^2
D=2.852*10**-2  # cm
H=69.85*10**-2  # cm
L=73.15*10**-2  # cm
Pa=[F[i]/S for i in range(len(F))]  # Pa = F/s
Pa=np.array(Pa)  # 转换为 numpy 数组
# 计算长度变化量
delta_x = [xi[i] - xi[0] for i in range(len(xi))]
delta_l=[(delta_x[i]*D)/(2*H*L) for i in range(len(delta_x))]  # mm
delta_l=np.array(delta_l)  # 转换为 numpy 数组
delta_x = np.array(delta_x)
xi=np.array(xi)
# 格式化数据为 5 位有效数字
f = [str(i) for i in f]
xi_1 = [np.format_float_positional(x, precision=3, unique=False, fractional=False, trim='k') for x in xi]
delta_x_1 = [np.format_float_positional(x, precision=3, unique=False, fractional=False, trim='k') for x in delta_x]
F_1 = [np.format_float_positional(x, precision=3, unique=False, fractional=False, trim='k') for x in F]
Pa_1 = [keep_first_n_digits(i, 3) for i in Pa]
Pa_1=[str(i) for i in Pa_1]
delata_l_1 = [np.format_float_positional(x, precision=3, unique=False, fractional=False, trim='k') for x in delta_l]
delata_l_1[5]='0.000740'
# 创建表格数据
data = [
    ["xi (m)"] + xi_1,
    ["Δx (m)"] + delta_x_1,
    ["ΔL/L"] + delata_l_1,
    ["F (m/kg)"] + f,
    ["F (N)"] + F_1,
    ["F/S (N/m^2)"] + Pa_1,
]
# 绘制表格
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=[""] + [f"Point {i}" for i in range(len(xi_1))], loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(xi_1) + 1)))

plt.show()
# 计算力 F
# g = 9.7946  # 重力加速度
# F = [float(i * g) for i in range(len(mean_length))]  # 保持单位为 mN
# F = np.array(F)
# F_1 = [np.format_float_positional(x, precision=5, unique=False, fractional=False, trim='k') for x in F]
# data_F = [
#     ["ΔL (mm)"] + delta_length_1,
#     ["F (mN)"] + F_1
# ]
# # 绘制力 F 的表格
# fig_F, ax_F = plt.subplots(figsize=(10, 4))
# ax_F.axis('tight')
# ax_F.axis('off')
# table_F = ax_F.table(cellText=data_F, colLabels=[""] + [f"Point {i}" for i in range(len(length1))], loc='center', cellLoc='center')
# table_F.auto_set_font_size(False)
# table_F.set_fontsize(10)
# table_F.auto_set_column_width(col=list(range(len(length1) + 1)))
# plt.show()
# 线性拟合
slope, intercept, r_value, p_value, std_err = linregress(delta_l, Pa)

# 打印拟合结果和相关系数
print(f"F = {slope:.3f} * ΔL + {intercept:.3f}")
print(f"Correlation coefficient (r): {r_value:.3f}")

# 绘制图像
plt.figure(figsize=(8, 6))
plt.plot(delta_l, Pa, 'bo', label='Experimental Data')  # 实验数据点
slope1=keep_first_n_digits(slope, 3)
intercept1=keep_first_n_digits(intercept, 3)
plt.plot(delta_l, slope * delta_l + intercept, 'r-', label=f'Fit: F = {slope1} * ΔL/L + {intercept1}')  # 拟合线
# plt.plot(delta_l, slope * delta_l + intercept, 'r-', label=f'Fit: F = {slope:.5f} * ΔL + {intercept:.5f}')  # 拟合线
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')  # x轴
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')  # y轴
plt.text(0.05, 0.95, f"r = {r_value:.3f}", transform=plt.gca().transAxes, fontsize=12, verticalalignment='top')
# 设置图像属性
plt.xlabel('ΔL/L', fontsize=12)
plt.ylabel('F/S', fontsize=12)  # 保持单位为 mN
plt.title('F/S vs ΔL/L', fontsize=14)
plt.legend()
plt.grid()
plt.show()