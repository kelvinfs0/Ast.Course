books = {}
def add_book(ISBN, title, author):
    if ISBN in books:
        print("该ISBN的书籍已存在。")
        fh = input("按回车键返回主菜单")
        return
    books[ISBN] = {'书名': title, '作者': author}
    print(f"书籍{title}已添加。")
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
        print(f"ISBN: {ISBN}, 书名: {info['title']}, 作者: {info['author']}")
    fh = input("按回车键返回主菜单")


def search_book(ISBN):
    if ISBN in books:
        info = books[ISBN]
        print(f"查找ISBN: {ISBN}, 书名: {info['title']}, 作者: {info['author']}")
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
        author = input("请输入更改后的作者: ")
        books[ISBN] = {'书名': title, '作者': author}
        print(f"已更新ISBN为{ISBN}的书籍信息。")
        fh = input("按回车键返回主菜单")
    else:
        print("没有找到该书籍。")
        fh = input("按回车键返回主菜单")


def main():
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
            author = input("输入作者: ")
            add_book(ISBN, title, author)
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
            break
        else:
            print("无效选择，请重试。")


if __name__ == "__main__":
    main()