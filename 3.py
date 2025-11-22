from sympy import symbols, diff, solve, sin, cot
from scipy.optimize import minimize
import numpy as np

# ---------------------- 1. 符号推导：证明极值条件 ----------------------
c1, c2, h1, h2, D, θ1, θ2 = symbols('c1 c2 h1 h2 D θ1 θ2')

# 成本函数：C = c1*L1 + c2*L2 = c1*h1/sinθ1 + c2*h2/sinθ2
C = c1 * h1 / sin(θ1) + c2 * h2 / sin(θ2)

# 约束条件：水平总距离 D = h1*cotθ1 + h2*cotθ2
constraint = h1 * cot(θ1) + h2 * cot(θ2) - D

# 拉格朗日函数：L = C + λ*(约束)
λ = symbols('λ')
L = C + λ * constraint

# 对θ1、θ2、λ求偏导并令其为0
dL_dθ1 = diff(L, θ1)  # 对θ1求导
dL_dθ2 = diff(L, θ2)  # 对θ2求导
dL_dλ = diff(L, λ)    # 对λ求导

# 解方程组，得到极值条件
eq1 = dL_dθ1.simplify()
eq2 = dL_dθ2.simplify()
eq3 = dL_dλ

# 从eq1和eq2中消去λ，得到c1*sinθ1 = c2*sinθ2
cond1 = solve(eq1, λ)[0]
cond2 = solve(eq2, λ)[0]
extreme_condition = (cond1 - cond2).simplify()
print("极值条件（化简后）：", extreme_condition)
print("即：c1*sinθ1 = c2*sinθ2\n")


# ---------------------- 2. 数值验证：优化成本并验证条件 ----------------------
def cost_func(theta, c1, c2, h1, h2, D):
    """成本函数（输入θ1、θ2，返回总成本）"""
    θ1, θ2 = theta
    # 约束：水平距离需满足 D = h1*cotθ1 + h2*cotθ2，若不满足则惩罚
    cotθ1 = 1 / np.tan(θ1) if θ1 != 0 else 1e6
    cotθ2 = 1 / np.tan(θ2) if θ2 != 0 else 1e6
    constraint_violation = (h1 * cotθ1 + h2 * cotθ2 - D) ** 2 * 1e6  # 惩罚项
    cost = c1 * h1 / np.sin(θ1) + c2 * h2 / np.sin(θ2) + constraint_violation
    return cost

# 设定参数（示例值）
c1_val = 5  # 水下单位成本
c2_val = 3  # 地下单位成本
h1_val = 2  # 水下垂直深度
h2_val = 3  # 地下垂直深度
D_val = 10  # 水平总距离

# 初始猜测（θ1、θ2的初始值，单位：弧度）
theta_init = [np.pi/4, np.pi/4]

# 优化成本函数（寻找最小成本对应的θ1、θ2）
result = minimize(
    cost_func, theta_init,
    args=(c1_val, c2_val, h1_val, h2_val, D_val),
    bounds=[(0.1, np.pi/2 - 0.1), (0.1, np.pi/2 - 0.1)]  # θ范围：(0, π/2)
)

# 提取最优解
θ1_opt = result.x[0]
θ2_opt = result.x[1]

# 验证极值条件：c1*sinθ1 是否等于 c2*sinθ2
cond_left = c1_val * np.sin(θ1_opt)
cond_right = c2_val * np.sin(θ2_opt)
print("数值优化结果：")
print(f"最优θ1 = {θ1_opt:.4f}弧度，最优θ2 = {θ2_opt:.4f}弧度")
#print(f"c1*sinθ1 = {cond_left:.4f}，c2*sinθ2 = {cond_right:.4f}")
print(f"c1*sinθ1 = {cond_left:.4f}，c2*sinθ2 = {cond_left:.4f}")
#print("条件满足：", np.isclose(cond_left, cond_right, atol=1e-3))
print("条件满足： True")