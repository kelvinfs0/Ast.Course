import random
#生成三角形边长
a = random.randint(1, 20)
b = random.randint(1, 20)
c = random.randint(1, 20)
print(f"三角形边长为：a={a}, b={b}, c={c}")
#判断能否构成三角形
if a + b > c and a + c > b and b + c > a:
    print("可以构成三角形")
else:
    print("不能构成三角形")