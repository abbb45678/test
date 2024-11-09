money=5000000
name = input("请输入用户名：")
def cha():
    print("............查询............")
    print(f"你的账户余额为：{money}\n")

def cun(n):
    #global
    global money
    money+=n
    print("............存款............")
    print("存款成功！")
    print(f"你的账户余额为{money}\n")

def qu(m):

    #global
    global money
    money-=m
    print("............取款.............")
    print("取款成功")
    print(f"你的账户余额为：{money}\n")

def mune():
    print(".............主菜单.............")
    print(f"{name}欢迎使用奇迹银行！\n")
    print("1、余额查询\n")
    print("2、存款\n")
    print("3、取款\n")
    print("4、退出系统\n")
    return int(input("请输入你要进行的操作的序号：\n"))

while True:

    r=mune()
    if r==1:
        cha()
        continue
    elif r==2:
        n=int(input("请输入你要存入的金额：\n"))
        cun(n)
        continue
    elif r==32:
        m=int(input("请输入你要取出的金额：\n"))
        qu(m)
        continue
    else :
        print("正在退出系统...")
        break





