import sys
class Animal:
    def __init__(self, name, age):
        self.__name = name  # 私有属性
        self.__age = age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("年龄必须大于0")

    def get_age(self):
        return self.__age

    def feed(self):
        print(f"{self.__name} 正在吃东西，心情变好了！")

class Dog(Animal):
    '''aaa'''

class Cat(Animal):
    '''aaa'''

class PetSystem:
    def __init__(self):
        self.pets = []
        self.version = "v1.0.0"

    def show_menu(self):
        print("\n--- 虚拟宠物系统 ---")
        print("1. 领养宠物狗")
        print("2. 领养宠物猫")
        print("3. 查看所有宠物")
        print("4. 喂食宠物")
        print("5. 修改宠物年龄")
        print("6. 版本信息")
        print("0. 退出系统")
        return input("请选择操作: ")

    def run(self):
        while True:
            choice = self.show_menu()
            if choice == '1':
                name = input("给小狗起个名字: ")
                age = int(input("输入年龄: "))
                self.pets.append(Dog(name, age))
            elif choice == '2':
                name = input("给小猫起个名字: ")
                age = int(input("输入年龄: "))
                self.pets.append(Cat(name, age))
            elif choice == '3':
                for p in self.pets:

                    print(f"[{type(p).__name__}] 名字：{p.get_name()}, 年龄:{p.get_age()} 岁")
            elif choice == '4':
                for p in self.pets:
                    p.feed()
            elif choice == '5':
                name = input("输入要修改的宠物名字: ")
                for p in self.pets:
                    if p.get_name() == name:
                        new_age = int(input("输入新年龄: "))
                        p.set_age(new_age)
                        print("修改成功！")
            elif choice == '6':
                print(f"系统版本: {self.version}")
            elif choice == '0':
                print("再见！")
                break
            else:
                print("无效输入。")

if __name__ == "__main__":
    system = PetSystem()
    system.run()
