car_info = {}
def input_car_info(bh,pp,ys,jg,num):
    car_info[bh] = {'品牌': pp, '颜色': ys, '价格': jg, '数量': num}
    print(f"汽车{pp}编号{bh}已添加。")
    fh = input("按回车键返回主菜单")

def del_car_info(bh):
    if bh in car_info:
        del car_info[bh]
        print(f"已删除编号为{bh}的汽车。")
        fh = input("按回车键返回主菜单")
    else:
        print("没有找到该汽车。")
        fh = input("按回车键返回主菜单")

def show_car_info():
    if not car_info:
        print("没有汽车信息可显示。")
        fh = input("按回车键返回主菜单")
        return
    for bh, info in car_info.items():
        print(f"编号: {bh}, 品牌: {info['品牌']}, 颜色: {info['颜色']}, 价格: {info['价格']}, 数量: {info['数量']}")
    fh = input("按回车键返回主菜单")

def modify_car_info(bh, pp, ys, jg, num):
    if bh in car_info:
        car_info[bh] = {'品牌': pp, '颜色': ys, '价格': jg, '数量': num}
        print(f"汽车编号{bh}的信息已更新。")
    else:
        print("没有找到该汽车。")
    fh = input("按回车键返回主菜单")

def search_car(bh):
    if bh in car_info:
        info = car_info[bh]
        print(f"编号：{bh}, 品牌: {info['品牌']}, 颜色: {info['颜色']}, 价格: {info['价格']}, 数量: {info['数量']}")
        fh = input("按回车键返回主菜单")
    else:
        print("没有找到该汽车。")
        fh = input("按回车键返回主菜单")

def main_menu():
    while True:
        print("\n****************************")
        print("汽车进销存管理系统")
        print("1. 添加汽车")
        print("2. 删除汽车")
        print("3. 查看所有汽车")
        print("4. 搜索汽车")
        print("5. 修改汽车信息")
        print("6. 退出")
        choice = input("请选择操作 (1-6): ")
        if choice == '1':
            bh = input("输入汽车编号: ")
            pp = input("输入品牌: ")
            ys = input("输入颜色: ")
            jg = input("输入价格: ")
            num = input("输入数量: ")
            input_car_info(bh, pp, ys, jg, num)
        elif choice == '2':
            bh = input("输入要删除的汽车编号: ")
            del_car_info(bh)
        elif choice == '3':
            show_car_info()
        elif choice == '4':
            bh = input("输入要搜索的汽车编号: ")
            search_car(bh)
        elif choice == '5':
            bh = input("输入要修改的汽车编号: ")
            pp = input("输入新的品牌: ")
            ys = input("输入新的颜色: ")
            jg = input("输入新的价格: ")
            num = input("输入新的数量: ")
            modify_car_info(bh, pp, ys, jg, num)
        elif choice == '6':
            print("退出系统。")
            break
        else:
            print("无效选择，请重试。")


if __name__ == "__main__":
    main_menu()