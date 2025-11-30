print("学生成绩录入系统")
print("="*50)
print("  - 请输入学生成绩（0-100分）")
print("  - 输入-1结束录入")
print("="*50)
grades = []  # 存储成绩
z_score = 0  # 总成绩
score_max = input("请输入卷面最高分数: ")
if float(score_max) < 0.0:
    print("错误：最高分数不能为负数！")
    exit()
while True:
        try:
            input_str = input("请输入学生成绩: ")
            score = float(input_str)

            if score == -1:
                break
            
            # 检查成绩
            if score < 0:
                print("错误：成绩不能为负数！")
                continue
            elif score > float(score_max):
                print(f"错误：成绩超过最高分数{score_max}")
                continue
            
            # 记录成绩
            grades.append(score)
            z_score =z_score + score            
        except ValueError:
            print("错误：请输入数字！")
print("\n" + "="*50)
print("成绩统计结果")
print("="*50)
    
if len(grades) > 0:
        average_score = z_score / len(grades)
        print(f"有效成绩数量: {len(grades)}")
        print(f"所有成绩: {grades}")
        print(f"总成绩: {z_score:.2f}")
        print(f"平均分: {average_score:.2f}")       
else:
        print("未录入任何有效成绩！")
