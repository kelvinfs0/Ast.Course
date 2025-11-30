print("工作日判定")
day = input("今天是星期几：")
if day in ['星期一', '星期二', '星期三', '星期四', '星期五']:
    print("今天是工作日")
elif day in ['星期六', '星期日']:
    print("今天是休息日")
else:
    print("输入有误，请输入正确的星期几")