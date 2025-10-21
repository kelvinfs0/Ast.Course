from math import pi
zc = 1
zbc = zc / 4
zmj = zbc ** 2
ybj = zc / (2 * pi)
ymj = round(pi * ybj ** 2,4)
from math import sqrt
mj = 1
zbc = sqrt(mj)
zzc = zbc * 4
ymj = sqrt(mj / pi)
yzc = round(2 * pi * ybj,4)
print("周长为一的正方形面积为：",zmj)
print("周长为一的圆形面积为：",ymj)
print("面积为一的正方形的周长为:",zzc)
print("面积为一的圆形的周长为：",yzc)
print("周长为一的正方形面积小于圆形",zmj<ymj)
print("面积为一的正方形周长大于圆形",zzc>yzc)
