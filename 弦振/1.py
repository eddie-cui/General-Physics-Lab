import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

lambda_cm = [] # You need to fill this with your data
# lambda_cm = []# You can also use this to process your lambda in the second part
lambda_log = [np.log10(x/100) for x in lambda_cm]   
print(lambda_log)
T = []  # You need to fill this with your data
# T = [] # You can also use this to process your f in the second part
T_log = [np.log10(x) for x in T]
print(T_log)

def plot_and_fit():
    # 进行线性拟合
    slope, intercept, r_value, p_value, std_err = linregress(T_log, lambda_log)
    
    # 创建拟合线的数据点
    fit_line = [slope * x + intercept for x in T_log]
    
    # 绘制散点图和拟合线
    plt.figure(figsize=(10, 6))
    plt.scatter(T_log, lambda_log, color='blue', marker='o', label='data')
    plt.plot(T_log, fit_line, color='red', label=f'line y = {slope:.4f}x + {intercept:.4f}')
    
    # 添加图表标题和轴标签
    plt.title('log(λ) vs log(T) linear fit')
    plt.xlabel('log(T)')
    plt.ylabel('log(λ)')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # 添加拟合参数信息
    plt.annotate(f'k = {slope:.4f}\nb = {intercept:.4f}\nR² = {r_value**2:.4f}', 
                 xy=(0.05, 0.85), xycoords='axes fraction', 
                 bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
    
    plt.legend()
    plt.tight_layout()
    plt.show()
    
    return slope, intercept, r_value**2

# 调用函数
slope, intercept, r_squared = plot_and_fit()
print(f"拟合结果: ln(λ) = {slope:.4f} * ln(T) + {intercept:.4f}")
print(f"决定系数 R²: {r_squared:.4f}")