print("收益计算器")
bj = int(input("请输入本金（元）："))
ll = int(input("请输入年收益率（%）：")) / 100
years = 0
sy = bj

while sy < 2 * bj:
    years += 1
    sy *= (1 + ll) 
print(f"{bj}元以{ll*100}%年收益，需要{years}年翻倍")
print(f"最终金额：{sy:.2f}元")