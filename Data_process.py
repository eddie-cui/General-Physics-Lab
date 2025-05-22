import numpy as np

c_values = {
    5: 1.65, 6: 1.75, 7: 1.80, 8: 1.86, 9: 1.92, 10: 1.96, 11: 2.00,
    12: 2.03, 13: 2.07, 14: 2.10, 15: 2.13, 16: 2.15, 17: 2.18, 18: 2.20,
    19: 2.22, 20: 2.24, 25: 2.33, 30: 2.39, 40: 2.50, 50: 2.58, 60: 2.64,
    70: 2.69, 80: 2.73, 90: 2.77, 100: 2.81, 110: 2.84, 150: 2.93, 200: 3.02
}
t_values = {
    0.683: {3: 1.32, 4: 1.20, 5: 1.14, 6: 1.11, 7: 1.09, 8: 1.08, 9: 1.07, 10: 1.06, 11: 1.05, float('inf'): 1.00},
    0.90: {3: 2.92, 4: 2.35, 5: 2.13, 6: 2.02, 7: 1.94, 8: 1.90, 9: 1.86, 10: 1.83, 11: 1.81, float('inf'): 1.65},
    0.95: {3: 4.30, 4: 3.18, 5: 2.78, 6: 2.57, 7: 2.45, 8: 2.36, 9: 2.31, 10: 2.26, 11: 2.23, float('inf'): 1.96},
    0.98: {3: 6.96, 4: 4.54, 5: 3.75, 6: 3.36, 7: 3.14, 8: 3.00, 9: 2.90, 10: 2.82, 11: 2.76, float('inf'): 2.33},
    0.99: {3: 9.93, 4: 5.84, 5: 4.60, 6: 4.03, 7: 3.71, 8: 3.50, 9: 3.36, 10: 3.25, 11: 3.17, float('inf'): 2.58}
}

def edit_zerodelta(measurement, zero_offset):  # 你的零差 请一定关心正负
    for i in range(len(measurement)):
        measurement[i] = measurement[i] - zero_offset
    return measurement

def calc_stddev(measurement):  # 计算标准差
    n = len(measurement)
    mean = np.mean(measurement)
    variance = sum((x - mean) ** 2 for x in measurement) / (n - 1)
    return np.sqrt(variance)

def calc_mean(measurement):     # 计算平均值
    return np.mean(measurement)

def calc_mean_stddev(measurement): # 计算平均值的标准差
    n = len(measurement)
    stddev = calc_stddev(measurement)
    return stddev / np.sqrt(n)

def calc_Gross_error(n, stddev): # 计算粗差
    if n in c_values:
        c = c_values[n]
        return c * stddev
    else:
        raise ValueError("n is not in the table")

def detect_error_value(measurement, Gross_error): # 检测粗差
    mean = np.mean(measurement)
    error_value = []
    for i in range(len(measurement)):
        if abs(measurement[i] - mean) > Gross_error:
            error_value.append(measurement[i])
    return error_value

def remove_error_values(measurement, error_values): # 删除粗差
    return np.array([x for x in measurement if x not in error_values])

def calc_confidence_interval(n, stddev, confidence_level): # 计算置信区间
    if confidence_level in t_values and n in t_values[confidence_level]:
        t = t_values[confidence_level][n]
    elif confidence_level in t_values and n > max(t_values[confidence_level].keys()):
        t = t_values[confidence_level][float('inf')]
    else:
        raise ValueError("n值或置信水平不在映射表中")
    return t * stddev / np.sqrt(n)

def calc_unconfidence(measurement, confidence_level, error_machine):  # 计算不确定度
    n = len(measurement)
    stddev = calc_stddev(measurement)
    if confidence_level in t_values and n in t_values[confidence_level]:
        t = t_values[confidence_level][n]
    elif confidence_level in t_values and n > max(t_values[confidence_level].keys()):
        t = t_values[confidence_level][float('inf')]
    else:
        raise ValueError("n值或置信水平不在映射表中")
    delta_a = t * stddev / np.sqrt(n)
    delta_b = error_machine * confidence_level
    U = delta_a**2 + delta_b**2
    return np.sqrt(U), delta_a, delta_b
def calc_viscosity(speed,d,rho0,rho1,D,g):
    return (rho1-rho0)*g*(d**2)/(18*speed*(1+2.4*(d/D)))
def calc_Re(speed,d,rho,viscosity):
    return speed*d*rho/viscosity
if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    zero_offset = float(input("Enter zero offset: "))
    confidence_level = float(input("Enter confidence level: "))
    error_machine = float(input("Enter error machine: "))
    measurement = []
    for i in range(n):
        measurement.append(float(input("Enter element: ")))
    measurement = np.array(measurement)
    measurement = edit_zerodelta(measurement, zero_offset)
    stddev = calc_stddev(measurement)
    mean = calc_mean(measurement)
    mean_stddev = calc_mean_stddev(measurement)
    Gross_error = calc_Gross_error(n, stddev)
    error_value = detect_error_value(measurement, Gross_error)
    
    # 输出删除错误值前的数据
    print("Zero Delta Measurement:", measurement)
    print("Standard Deviation:", stddev)
    print("Mean:", mean)
    print("Mean Standard Deviation:", mean_stddev)
    print("Gross Error:", Gross_error)
    print("Error Value:", error_value)
    print("Confidence Interval:", calc_confidence_interval(n, stddev, confidence_level))
    print("-----")
    
    # 删除错误值
    measurement = remove_error_values(measurement, error_value)
    n = len(measurement)  # 更新n值
    stddev = calc_stddev(measurement)
    mean = calc_mean(measurement)
    mean_stddev = calc_mean_stddev(measurement)
    confidence_interval = calc_confidence_interval(n, stddev, confidence_level)
    unconfidence, delta_a, delta_b = calc_unconfidence(measurement, confidence_level, error_machine)
    
    # 输出删除错误值后的数据
    print("Zero Delta Measurement after removing error values:", measurement)
    print("Standard Deviation after removing error values:", stddev)
    print("Mean after removing error values:", mean)
    print("Mean Standard Deviation after removing error values:", mean_stddev)
    print("Confidence Interval after removing error values:", confidence_interval)
    print("Delta_a after removing error values:", delta_a)
    print("Delta_b after removing error values:", delta_b)
    print("Unconfidence after removing error values:", unconfidence)
    print("-----")

    # 计算粘度
    '''
    speed=(20*(10**(-2)))/mean
    print("Speed:", speed)
    d=1.041*10**(-3)
    rho0=950
    rho1=7800
    D=2*10**(-2)
    g=9.7946
    viscosity=calc_viscosity(speed,d,rho0,rho1,D,g)
    print("Viscosity:", viscosity)
    print("-----")
    Re=calc_Re(speed,d,rho1,viscosity)
    print("Reynolds number:", Re)'''