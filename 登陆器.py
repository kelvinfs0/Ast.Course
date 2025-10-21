import time

print("欢迎使用")
tuserid = "root"
tpsw = "admin"
n = 1
l = 1
while l < 11:
    while n <= 3:
        userid = input("请输入用户名：")
        password = input("请输入密码：")
        if userid == tuserid and password == tpsw:
            print("登陆成功！")
            exit()
        else:
            m = 3-n
            print(f"账户或密码不正确,你还有{m}次机会尝试")
            n = n + 1
            l = l + 1

    else:
        print("尝试次数过多,请在一分钟后再试")
        time.sleep(3)
        n = 1
        
else:
    print("今日尝试次数过多已被禁止登录")
    exit()