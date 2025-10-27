
money = int(input("请输入要兑换的金额："))
one_a = money + 1
twe_a = (money // 2) + 1
five_a = (money // 5) + 1
ten_a = (money // 10) + 1
twen_a = (money // 20) + 1
fifty_a = (money // 50) + 1
hundred_a = (money // 100) + 1
ff = 0
for one in range(0,one_a):
    #print(one)
    for twe in range(0,twe_a):
        for five in range(0,five_a):
            for ten in range(0,ten_a):
                for twen in range(0,twen_a):
                    for fifty in range(0,fifty_a):
                        for hundred in range(0,hundred_a):
                            if one + twe * 2 + five * 5 + ten * 10 + twen * 20 + fifty * 50 + hundred * 100 == money:
                                ff = ff +1
                                print(f"一元{one}张，二元{twe}张，五元{five}张,十元{ten}张，二十元{twen}张，五十元{fifty}张，一百元{hundred}张")
print(f"方法有{ff}种")