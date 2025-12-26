zb = ((1.0,2.0), (3.0,4.0), (5.0,6.0))
xa = 0.0
ya = 0.0
for x, y in zb:
    xa = xa + x
    ya = ya + y
xa = xa / len(zb)
ya = ya / len(zb)
print(f"坐标点的平均值是：({xa}, {ya})")    