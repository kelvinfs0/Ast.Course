number = input("请输入数字：")
box = ''
a = len(number) - 1

while a >=0:
    box += number[a]
    a -=1
print(f"反序结果为{box}")