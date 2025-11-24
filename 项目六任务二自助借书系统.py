book = {}
books = {'9787115613639': {'书名': 'Python编程：从入门到实践', '数量': 5},
        '9787115637505': {'书名': 'Hello算法', '数量': 7},
        '9787111705673': {'书名': '计算机网络：系统方法', '数量': 4},}

def main():
    print("欢迎使用图书管理系统！")
    ymchoice = input("读者(u)或管理员(a)登录：")
    if ymchoice == 'a':
        adminpwd = input("请输入管理员密码：")
        if adminpwd == 'root':
            print("管理员登录成功！")
            admin_meun()
        else:
            print("密码错误")
            main()
    elif ymchoice == 'u':
        print("以读者账户进入")
        user_meun()
    else:
        print("无效输入，请重试。")
        main()


def admin_meun():
    while True:
        print("\n****************************")
        print("图书管理系统")
        print("1. 添加书籍")
        print("2. 删除书籍")
        print("3. 查看所有书籍")
        print("4. 搜索书籍")
        print("5. 清空书单")
        print("6.更改书籍信息")
        print("7. 退出")
        choice = input("请选择操作 (1-7): ")
        if choice == '1':
            ISBN = input("输入书籍ISBN: ")
            title = input("输入书名: ")
            num = input("输入数量: ")
            add_book(ISBN, title, num)
        elif choice == '2':
            ISBN = input("输入要删除的书籍ISBN: ")
            remove_book(ISBN)
        elif choice == '3':
            view_books()
        elif choice == '4':
            ISBN = input("输入要搜索的书籍ISBN: ")
            search_book(ISBN)
        elif choice == '5':
            clear_books()
        elif choice == '6':
            print("更改书籍信息：")
            ISBN = input("输入要更改的书籍ISBN: ")
            change_book(ISBN)
        elif choice == '7':
            print("退出系统。")
            exit()
        else:
            print("无效选择，请重试。")


def user_meun():
    print("用户菜单")
    print("0.退出系统")
    print("1.查看所有书籍")
    print("2.借阅书籍")
    print("3.已借书籍")
    print("4.归还书籍")
    print("5.归还所有书籍")
    uchoice = input("请选择操作 (0-5): ")
    if uchoice == '0':
        print("退出系统。")
        exit()
    elif uchoice == '1':
        view_books()
        user_meun()
    elif uchoice == '2':
        uborrow()
    elif uchoice == '3':
        uyborrow()
    elif uchoice == '4':
        ureturn()
    elif uchoice == '5':
        uallreturn()

#----------------------------------------用户借阅-----------------------------------------#

def uborrow():
        borrow_ISBN = input("请输入要借阅的书籍ISBN：")
        if borrow_ISBN in books:
            if books[borrow_ISBN]['数量'] > 0:
                books[borrow_ISBN]['数量'] -= 1
                book[borrow_ISBN] = books[borrow_ISBN]
                print(f"已成功借阅书籍：{books[borrow_ISBN]['书名']}")
                fh = input("按回车键返回菜单")
            else:
                print("该书籍暂无库存，无法借阅。")
                fh = input("按回车键返回菜单")
        else:
            print("没有找到该书籍。")
            fh = input("按回车键返回菜单")
        user_meun()


def uyborrow():
    if not book:
        print("您未借阅任何书籍。")
        fh = input("按回车键返回菜单")
    else:
        for ISBN, info in book.items():
            print(f"ISBN: {ISBN}, 书名: {info['书名']}, 数量: {info['数量']}")
        fh = input("按回车键返回菜单")
    user_meun()


def ureturn():
    return_ISBN = input("请输入要归还的书籍ISBN：")
    if return_ISBN in book:
        books[return_ISBN]['数量'] += 1
        del book[return_ISBN]
        print(f"已成功归还书籍：{books[return_ISBN]['书名']}")
        fh = input("按回车键返回菜单")
    else:
        print("您未借阅该书籍，无需归还。")
        fh = input("按回车键返回菜单")
    user_meun()


def uallreturn():
    if not book:
        print("您未借阅任何书籍。")
        fh = input("按回车键返回菜单")
    else:
        for return_ISBN in list(book.keys()):
            books[return_ISBN]['数量'] += 1
            print(f"已成功归还书籍：{books[return_ISBN]['书名']}")
        book.clear()
        fh = input("按回车键返回菜单")
    user_meun()

#----------------------------------------图书管理-----------------------------------------#

def add_book(ISBN, title, num):
    if ISBN in books:
        print("该ISBN的书籍已存在。")
        fh = input("按回车键返回主菜单")
        return
    books[ISBN] = {'书名': title, '数量': num}
    print(f"书籍“{title}”已添加。")
    print(books)
    fh = input("按回车键返回主菜单")


def remove_book(ISBN):
    if ISBN in books:
        del books[ISBN]
        print(f"已删除ISBN为{ISBN}的书籍。")
        fh = input("按回车键返回主菜单")
    else:
        print("没有找到该书籍。")
        fh = input("按回车键返回主菜单")


def view_books():
    if not books:
        print("没有书籍可显示。")
        fh = input("按回车键返回主菜单")
        return
    for ISBN, info in books.items():
        print(f"ISBN: {ISBN}, 书名: {info['书名']}, 数量: {info['数量']}")
    fh = input("按回车键返回主菜单")


def search_book(ISBN):
    if ISBN in books:
        info = books[ISBN]
        print(f"查找ISBN: {ISBN}, 书名: {info['书名']}, 数量: {info['数量']}")
        fh = input("按回车键返回主菜单")
    else:
        print("没有找到该书籍。")
        fh = input("按回车键返回主菜单")


def clear_books():
    qr = input("确定要清空所有书籍吗？(y/n): ")
    if qr.lower() == 'y':
        books.clear()
        print("已清空所有书籍。")
        fh = input("按回车键返回主菜单")
    else:
        print("操作已取消。")
        fh = input("按回车键返回主菜单")
        return


def change_book(ISBN):
    if ISBN in books:
        title = input("请输入更改后的书名: ")
        num = input("请输入更改后的数量: ")
        books[ISBN] = {'书名': title, '数量': num}
        print(f"已更新ISBN为{ISBN}的书籍信息。")
        fh = input("按回车键返回主菜单")
    else:
        print("没有找到该书籍。")
        fh = input("按回车键返回主菜单")





if __name__ == "__main__":
    main()