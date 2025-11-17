import math
s1 = 10 / math.sqrt(2)
s12 = round(s1 * s1,4)
print("对角线为10的正方形的面积为：",s12)
s2 = round(math.pi*(10/2)**2,4)
print("计算直径为10的圆的面积：",s2)
s3 = 10*10
print("计算边长为10的正方形面积：",s3)
print("------------------")
print("s1大于s2：", s12 > s2)
print("s3大于s2,s2小于s1:", s3 > s2 and s2 < s1)