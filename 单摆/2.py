import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt
import matplotlib as mpl

# 设置全局字体为Times New Roman（论文标准字体）
#此程序用于计算改变绳长测g
plt.rcParams['font.family'] = 'Times New Roman'

# 数据
L=[] # 绳长 厘米！！
L=[l*10**(-2) for l in L]  # 转换为米
T_2=[]# 周期2T
T=[(time/2)**2 for time in T_2]



# 格式化数据为表格展示
L_1 = [np.format_float_positional(x, precision=4, unique=False, fractional=False, trim='k') for x in L]
T_2_1 = [np.format_float_positional(x, precision=4, unique=False, fractional=False, trim='k') for x in T_2]
T_1 = [np.format_float_positional(x, precision=4, unique=False, fractional=False, trim='k') for x in T]

# 创建表格数据（英文标题）
data = [
    ["L (m)"] + L_1,
    ["2T (s)"] + T_2_1,
    ["T² (s²)"] + T_1
]

# 绘制表格
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('tight')
ax.axis('off')
table = ax.table(cellText=data, colLabels=[""] + [f"Point {i+1}" for i in range(len(L))], 
                 loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(L) + 1)))
plt.title("Experimental Data for Simple Pendulum", fontsize=14)
plt.show()

# 线性拟合
slope, intercept, r_value, p_value, std_err = linregress(L, T)

# 打印拟合结果和相关系数
print(f"Linear fit: T^2 = {slope: 4f} * L + {intercept:.4f}")
print(f"Correlation coefficient (r): {r_value:.4f}")
print(f"Standard error: {std_err:.4f}")

# ...existing code...

# 打印拟合结果和相关系数
print(f"Linear fit: T^2 = {slope:.4f} * L + {intercept:.4f}")
print(f"Correlation coefficient (r): {r_value:.4f}")
print(f"Standard error: {std_err:.4f}")

# 创建更密集的x轴点以绘制平滑的拟合线
x_fit = np.linspace(min(L), max(L), 100)
y_fit = slope * x_fit + intercept

# 绘制第一个图 - 原始Y轴范围
plt.figure(figsize=(10, 8), dpi=100)

# 绘制数据点和拟合线
plt.plot(L, T, 'bo', markersize=8, label='Experimental Data')
plt.plot(x_fit, y_fit, 'r-', linewidth=2, 
         label=f'Linear Fit: T^2 = {slope:.4f} * L + {intercept:.4f}')

# 美化图表
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# 添加相关系数
plt.text(0.05, 0.95, f"Correlation Coefficient r = {r_value:.4f}", 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'))

# 设置图像属性
plt.xlabel('L (m)', fontsize=14)
plt.ylabel('Period (T²) [s²]', fontsize=14)
plt.title('Relationship Between Period and Length (Original Scale)', fontsize=16)
plt.legend(fontsize=12, loc='lower right', framealpha=0.9)



plt.show()

# ...existing code...

# 绘制第二个图 - 放大的X轴和Y轴范围
plt.figure(figsize=(10, 8), dpi=100)

# 计算数据的x轴和y轴范围以放大变化
x_min = min(L) - 0.02  # 减小一些，保留一点边距
x_max = max(L) + 0.02  # 增加一些，保留一点边距
y_min = min(T) - 0.01
y_max = max(T) + 0.01

# 绘制数据点和拟合线
plt.plot(L, T, 'bo', markersize=8, label='Experimental Data')
plt.plot(x_fit, y_fit, 'r-', linewidth=2, 
         label=f'Linear Fit: T^2 = {slope:.4f} * L + {intercept:.4f}')

# 设置x轴和y轴范围以放大变化
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(np.linspace(x_min, x_max, 8))  # 8个刻度点，可根据需要调整
plt.yticks(np.linspace(y_min, y_max, 10))

# 美化图表
plt.grid(True, linestyle='--', alpha=0.7)
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.axvline(0, color='black', linewidth=0.8, linestyle='--')

# 添加相关系数
plt.text(0.05, 0.95, f"Correlation Coefficient r = {r_value:.4f}", 
         transform=plt.gca().transAxes, fontsize=12, verticalalignment='top',
         bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray', boxstyle='round,pad=0.5'))

# 设置图像属性
plt.xlabel('L (m)', fontsize=14)
plt.ylabel('Period (T²) [s²]', fontsize=14)
plt.title('Relationship Between Period and Length (Zoomed X-Y Axes)', fontsize=16)
plt.legend(fontsize=12, loc='lower right', framealpha=0.9)


plt.show()