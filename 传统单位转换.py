print ("传统长度转换器")
a = float(input("请输入要转换的数值："))
#y = input("请选择原数值单位：(米、公里、里、丈、尺)")
z = input("请选择要转换的单位：(米、公里、里、丈、尺)")
if z == "米":
    print(a,"米等于",a,"米")
elif z == "公里":
    gl = a / 1000
    print(a,"米等于",gl,"公里")
elif z == "里":
    l = a /500
    print(a,"米等于",l,"里")
elif z == "丈":
    zz = a / 3.333
    print(a,"米等于",zz,"丈")
elif z == "尺":
    c = a * 3
    print(a,"米等于",c,"尺")
print("转换完成:")