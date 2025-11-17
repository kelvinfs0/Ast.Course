print("********温度转换器********")
print("1.摄氏度转华氏度  2.华氏度转摄氏度：")
choice = input("请选择转换类型(1或2)：")
if choice == "1":
    ssds = input("请输入摄氏度温度：")
    ssd = float(ssds)
    shsd = ssd * 9 / 5 + 32
    print("*******计算中*******")
    print("******转换成功******")
    print(str(ssd) + "摄氏度等于" + str(shsd) + "华氏度")
elif choice == "2":
    hsds = input("请输入华氏度温度：")
    hsd = float(hsds)
    scsd = (hsd - 32) * 5 / 9
    print("*******计算中*******")
    print("******转换成功******")
    print(str(hsd) + "华氏度等于" + str(scsd) + "摄氏度")