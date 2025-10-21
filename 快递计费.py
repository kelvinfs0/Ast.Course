print("快递计费系统")
zl = float(input("请输入重量："))
wz = int(input("请输入目的地(同城为0，省内为1，省外为2):"))
a = 0
if zl > 3:
    if wz == 0:
        a = 10 + (zl - 3) * 2
    if wz == 1:
        a = 10 + (zl - 3) * 3
    if wz == 2:
        a = 10 + (zl - 3) * 5
elif zl <= 3:
    if wz == 0:
        a = 10
    if wz == 1:
        a = 12
    if wz == 2:
        a = 15
print("费用为：",a,"元")
