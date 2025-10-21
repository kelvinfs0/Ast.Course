from math import sqrt
print("请输入一元二次方程中的未知数abc：")
a = (input("a="))
a2 = int(a)
b = (input("b="))
b2 = int(b)
c = (input("c="))
c2 = int(c)
print("求解方程" + a + "x^2+" + b + "x+" + c)
discriminant = (b2 ** 2) - (4 * a2 * c2)
if discriminant > 0:
    x1 = (-b2 + sqrt(discriminant)) / (2*a2)
    x2 = (-b2 - sqrt(discriminant)) / (2*a2)
    x12 = str(x1)
    x22 = str(x2)
    print("x1=" + x12 + "；" + "x2=" + x22)
elif discriminant == 0:
    x0 = -b2 / (2 * a2)
    x02 = str(x0)
    print("delta=0，只有一个实数解x=" + x02)
else:
    print("delta<0，没有实数解")