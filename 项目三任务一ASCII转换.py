def ASCII_check():
    char = input("请输入一个字符: ")
    if len(char) != 1:
        print("错误：请输入单个字符！")
        return
        # 判断是否为字母
    if char.isalpha():
        # 判断大小写
        if char.isupper():
            case_type = "大写字母"
        else:
            case_type = "小写字母"        
        # 获取ASCII码值
        ascii_value = ord(char)        
        # 输出结果
        print(f"您输入的 '{char}' 是一个{case_type}")
        print(f"ASCII码值: {ascii_value}")                
    else:
        print(f"您输入的 '{char}' 不是一个字母")
        print(f"ASCII码值: {ord(char)}")

# 测试函数
print("字符类型判断程序")
print("=" * 30)
ASCII_check()
