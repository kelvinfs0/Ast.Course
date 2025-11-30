print("闰年检查")
year = int(input("请输入年份："))
if (year % 4 == 0 and year % 100 != 0):
    print(f"{year}是闰年")
elif (year % 400 == 0):
    print(f"{year}是闰年")
else:
    print(f"{year}不是闰年")