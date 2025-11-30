print("最大公约数和最小公倍数计算器")
print("="*50)
while True:
    try:
            # 获取输入
            a = int(input("请输入第一个正整数（输入0退出）: "))
            if a == 0:
                break
            if a < 1:
                print("请输入正整数！")
                continue
                
            b = int(input("请输入第二个正整数: "))
            if b < 1:
                print("请输入正整数！")
                continue
            
            # 保存原始值用于显示
            original_a, original_b = a, b
            
            # 计算最大公约数（GCD）- 使用辗转相除法
            temp_a, temp_b = a, b
            while temp_b != 0:
                temp_a, temp_b = temp_b, temp_a % temp_b
            gcd = temp_a
            
            # 计算最小公倍数（LCM）
            lcm = abs(a * b) // gcd
            
            # 输出结果
            print(f"\n计算结果：")
            print(f"数字 {original_a} 和 {original_b}")
            print(f"最大公约数 (GCD): {gcd}")
            print(f"最小公倍数 (LCM): {lcm}")
            print("-" * 30)
            
    except ValueError:
        print("输入无效，请输入整数！")
    except ZeroDivisionError:
        print("错误：除数不能为零！")

