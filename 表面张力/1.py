import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# 输入7组点坐标
m = np.array([])  # 砝码质量 (g)
g = 9.794  # 重力加速度 (m/s^2)
f = m * g  # 计算外力 f (mN)
u = np.array([])  # 电压 U (mV)

# 使用 linregress 进行线性拟合
slope, intercept, r_value, p_value, std_err = linregress(f, u)
line = slope * f + intercept

# 绘制散点图和拟合直线
plt.scatter(f, u, color='blue', label='Data points')
plt.plot(f, line, color='red', label=f'Fit line: U = {slope:.5f}f  {intercept:.5f}')
plt.title('Calibration Curve of Force Sensor')
plt.xlabel('Force f (mN)')
plt.ylabel('Voltage U (mV)')
plt.legend()
plt.grid(True)

# 在右下角显示保留两位小数的直线方程
plt.text(0.95, 0.05, f'U = {slope:.2f}f  {intercept:.2f}', 
         transform=plt.gca().transAxes, fontsize=12, color='black', 
         verticalalignment='bottom', horizontalalignment='right')

# 显示相关系数
plt.text(min(f), max(u)-15, f'r = {r_value:.5f}', fontsize=12, color='green')

# 显示图形
plt.show()

# 打印数据表格
m_formatted = [np.format_float_positional(x, precision=4, unique=False, fractional=False, trim='k') for x in m]
f_formatted = [np.format_float_positional(x, precision=4, unique=False, fractional=False, trim='k') for x in f]
u_formatted = [np.format_float_positional(x, precision=3, unique=False, fractional=False, trim='k') for x in u]
data_table = [
    ["Mass (g)"] + m_formatted,
    ["Force (mN)"] + f_formatted,
    ["Voltage (mV)"] + u_formatted
]

# 绘制表格
fig_table, ax_table = plt.subplots(figsize=(10, 4))
ax_table.axis('tight')
ax_table.axis('off')
table = ax_table.table(
    cellText=data_table,
    colLabels=[""] + [f"Point {i+1}" for i in range(len(m))],
    loc='center',
    cellLoc='center'
)
table.auto_set_font_size(False)
table.set_fontsize(10)
table.auto_set_column_width(col=list(range(len(m) + 1)))
plt.show()