list = []
while True:
    list_input = input("请输入列表元素(输入end结束)：")
    if list_input == "end":
        break
    elif list_input.isdigit():
        list.append(int(list_input))
    else:
        print("无效输入，请重新输入")
new_list = list[1::2]
print(f"提取出的奇数元素为{new_list}")
