import numpy as np
from scipy.optimize import minimize

# 参数设置
a = 10  # 点I的y坐标（y>0区域）
b = 10  # 点C的y坐标的绝对值（y<0区域）
d = 20  # 点C的x坐标（点I在x=0）
c1 = 1  # y>0区域的每千米成本
c2 = 2  # y<0区域的每千米成本

# 定义总成本函数
def total_cost(x):
    d1 = np.sqrt(x**2 + a**2)  # 从I到边界点P的距离
    d2 = np.sqrt((d - x)**2 + b**2)  # 从P到C的距离
    return c1 * d1 + c2 * d2

# 初始猜测值
x0 = 10

# 使用BFGS方法最小化总成本
res = minimize(total_cost, x0, method='BFGS')
x_opt = res.x[0]

# 计算最优路径下的距离和角度
d1_opt = np.sqrt(x_opt**2 + a**2)
d2_opt = np.sqrt((d - x_opt)**2 + b**2)
sin_theta1 = x_opt / d1_opt  # sin(θ1)
sin_theta2 = (d - x_opt) / d2_opt  # sin(θ2)

# 计算c1 sinθ1 和 c2 sinθ2
c1_sin = c1 * sin_theta1
c2_sin = c2 * sin_theta2

# 输出结果
print("优化结果:")
print(f"最优边界点 x: {x_opt:.6f}")
print(f"sin(θ1): {sin_theta1:.6f}")
print(f"sin(θ2): {sin_theta2:.6f}")
print(f"c1 * sin(θ1): {c1_sin:.6f}")
print(f"c2 * sin(θ2): {c2_sin:.6f}")
print(f"c1 * sin(θ1) ≈ c2 * sin(θ2): {np.isclose(c1_sin, c2_sin)}")

# 计算角度（度）
theta1_deg = np.degrees(np.arcsin(sin_theta1))
theta2_deg = np.degrees(np.arcsin(sin_theta2))
print(f"θ1: {theta1_deg:.2f}°")
print(f"θ2: {theta2_deg:.2f}°")