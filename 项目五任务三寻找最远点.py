points = ((10, 2), (3, 4), (5, 6))
zyjl = 0.0

for point in points:
    jl = (point[0] ** 2 + point[1] ** 2) ** 0.5
    if jl > zyjl:
        zyjl = jl
        zyd = point

print(f"到原点最远的点是:{zyd},距离是:{zyjl}")