import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体为Times New Roman（论文标准字体）
# 此用来计算改变摆角测g
plt.rcParams['font.family'] = 'Times New Roman'

# 数据
angle=[]# 角度（不是弧度！！！）
T_2=[]# 2T（秒）
T=[time for time in T_2]

angle_sine=[np.sin(np.radians(angle_single/2))**2 for angle_single in angle]
angle_sine = np.array(angle_sine)

# 格式化数据为表格展示
angle_1 = [np.format_float_positional(x, precision=3, unique=False, fractional=False, trim='k') for x in angle]
angle_sine_1 = [np.format_float_positional(x, precision=5, unique=False, fractional=False, trim='k') for x in angle_sine]
T_1 = [np.format_float_positional(x, precision=3, unique=False, fractional=False, trim='k') for x in T]

# 创建表格数据（英文标题）
data = [
    ["θ (°)"] + angle_1,
    ["sin²(θ/2)"] + angle_sine_1,
    ["2T (s)"] + T_1
]

# 绘制表格
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=[""] + [f"Point {i+1}" for i in range(len(angle_sine))], 
                 loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(angle_sine) + 1)))
plt.title("Experimental Data for Simple Pendulum", fontsize=14)
plt.show()

# 线性拟合
slope, intercept, r_value, p_value, std_err = linregress(angle_sine, T)

# 打印拟合结果和相关系数
print(f"Linear fit: 2T = {slope:.3f} * sin²(θ/2) + {intercept:.3f}")
print(f"Correlation coefficient (r): {r_value:.5f}")
print(f"Standard error: {std_err:.5f}")

# ...existing code...

# 打印拟合结果和相关系数
print(f"Linear fit: 2T = {slope:.3f} * sin²(θ/2) + {intercept:.3f}")
print(f"Correlation coefficient (r): {r_value:.5f}")
print(f"Standard error: {std_err:.5f}")

# 创建更密集的x轴点以绘制平滑的拟合线
x_fit = np.linspace(min(angle_sine), max(angle_sine), 100)
y_fit = slope * x_fit + intercept

# 绘制第一个图 - 原始Y轴范围
plt.figure(figsize=(10, 8), dpi=100)

# 绘制数据点和拟合线
plt.plot(angle_sine, T, 'bo', markersize=8, label='Experimental Data')
plt.plot(x_fit, y_fit, 'r-', linewidth=2, 
         label=f'Linear Fit: 2T = {slope:.3f} × sin²(θ/2) + {intercept:.3f}')

# 美化图表
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# 添加相关系数
plt.text(0.05, 0.95, f"Correlation Coefficient r = {r_value:.5f}", 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'))

# 设置图像属性
plt.xlabel('sin²(θ/2)', fontsize=14)
plt.ylabel('Period (2T) [s]', fontsize=14)
plt.title('Relationship Between Period and Amplitude (Original Scale)', fontsize=16)
plt.legend(fontsize=12, loc='lower right', framealpha=0.9)


# 标注理论依据
plt.figtext(0.5, 0.01, "According to theory: $T = T_0(1 + \\frac{1}{16}\\theta^2 + ...)$, where $\\sin^2(\\theta/2) \\approx \\frac{\\theta^2}{4}$", 
             fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', alpha=0.9, edgecolor='gray', boxstyle='round,pad=0.5'))

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()

# 绘制第二个图 - 放大的Y轴范围
plt.figure(figsize=(10, 8), dpi=100)

# 计算数据的y轴范围以放大变化
y_min = min(T) - 0.01
y_max = max(T) + 0.01

# 绘制数据点和拟合线
plt.plot(angle_sine, T, 'bo', markersize=8, label='Experimental Data')
plt.plot(x_fit, y_fit, 'r-', linewidth=2, 
         label=f'Linear Fit: 2T = {slope:.3f} × sin²(θ/2) + {intercept:.3f}')

# 设置y轴范围以放大变化
plt.ylim(y_min, y_max)
plt.yticks(np.linspace(y_min, y_max, 10))

# 美化图表
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# 添加相关系数
plt.text(0.05, 0.95, f"Correlation Coefficient r = {r_value:.5f}", 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'))

# 设置图像属性
plt.xlabel('sin²(θ/2)', fontsize=14)
plt.ylabel('Period (2T) [s]', fontsize=14)
plt.title('Relationship Between Period and Amplitude (Zoomed Y-Axis)', fontsize=16)
plt.legend(fontsize=12, loc='lower right', framealpha=0.9)


# 标注理论依据
plt.figtext(0.5, 0.01, "According to theory: $T = T_0(1 + \\frac{1}{16}\\theta^2 + ...)$, where $\\sin^2(\\theta/2) \\approx \\frac{\\theta^2}{4}$", 
             fontsize=10, ha='center', bbox=dict(facecolor='lightyellow', alpha=0.9, edgecolor='gray', boxstyle='round,pad=0.5'))

plt.tight_layout(rect=[0, 0.05, 1, 0.95])
plt.show()