import math
print("-------三角函数计算器-------")
jd = float(input("请输入角度："))
rad = math.radians(jd)
print(f"sin({jd}) = {math.sin(rad)}")
print(f"cos({jd}) = {math.cos(rad)}")
print(f"tan({jd}) = {math.tan(rad)}")