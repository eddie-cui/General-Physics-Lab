import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Data from the image
temperature = np.array([])   # you need to fill in your data (temperature in °C)
viscosity = np.array([]) # you need to fill in your data (viscosity in Pa·s)

# Define fitting functions
def linear_func(x, a, b):
    return a * x + b

def exponential_func(x, a, b):
    return a * np.exp(b * x)

def power_func(x, a, b):
    return a * np.power(x, b)

# Perform curve fitting
linear_params, _ = curve_fit(linear_func, temperature, viscosity)
exp_params, _ = curve_fit(exponential_func, temperature, viscosity)
power_params, _ = curve_fit(power_func, temperature, viscosity)

# Generate x values for plotting the fit
x_fit = np.linspace(min(temperature), max(temperature), 300)

# Plotting
figs = []

# 1. Scatter Plot
plt.figure()
plt.scatter(temperature, viscosity, color='blue')
plt.title('Scatter Plot of Temperature vs Viscosity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Viscosity (Pa·s)')
plt.grid(True)
figs.append(plt.gcf())

# 2. Linear Fit
plt.figure()
plt.scatter(temperature, viscosity, color='blue', label='Data')
plt.plot(x_fit, linear_func(x_fit, *linear_params), color='red', label=f'Linear Fit: η = {linear_params[0]:.4f}T + {linear_params[1]:.4f}')
plt.title('Linear Fit of Temperature vs Viscosity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Viscosity (Pa·s)')
plt.legend()
plt.grid(True)
figs.append(plt.gcf())

# 3. Exponential Fit
plt.figure()
plt.scatter(temperature, viscosity, color='blue', label='Data')
plt.plot(x_fit, exponential_func(x_fit, *exp_params), color='green', label=f'Exponential Fit: η = {exp_params[0]:.4f}e^({exp_params[1]:.4f}T)')
plt.title('Exponential Fit of Temperature vs Viscosity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Viscosity (Pa·s)')
plt.legend()
plt.grid(True)
figs.append(plt.gcf())

# 4. Power Fit
plt.figure()
plt.scatter(temperature, viscosity, color='blue', label='Data')
plt.plot(x_fit, power_func(x_fit, *power_params), color='purple', label=f'Power Fit: η = {power_params[0]:.4f}T^{power_params[1]:.4f}')
plt.title('Power Fit of Temperature vs Viscosity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Viscosity (Pa·s)')
plt.legend()
plt.grid(True)
figs.append(plt.gcf())

# Display all plots
plt.show()

# 计算拟合曲线上的粘滞系数值
linear_fit_values = linear_func(temperature, *linear_params)
exp_fit_values = exponential_func(temperature, *exp_params)
power_fit_values = power_func(temperature, *power_params)

# 计算相关系数
linear_corr = np.corrcoef(viscosity, linear_fit_values)[0, 1]
exp_corr = np.corrcoef(viscosity, exp_fit_values)[0, 1]
power_corr = np.corrcoef(viscosity, power_fit_values)[0, 1]

# 打印相关系数
print(f"Linear Fit 相关系数: {linear_corr:.4f}")
print(f"Exponential Fit 相关系数: {exp_corr:.4f}")
print(f"Power Fit 相关系数: {power_corr:.4f}")