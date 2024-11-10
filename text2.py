# 1、两数之和
# n=int(input("请输入第一个数："))
# m=int(input("请输入第二个数："))
# p=m+n
# print(f"两数之和为：{p}")

# def sum(a,b):
#     c=a+b
#     return c
# c=sum(2,4)
# print(f"{c}")

# 2、求阶乘
# n=eval(input("请输入一个数："))
# i=1
# j=1
# while i<=n:
#     j*=i
#     i+=1
# print(f"{n}的阶乘为：{j}")

# def fun(n):
#     result=1
#     while n>0:
#         result*=n
#         n-=1
#     return result
# n=int(input())
# print(f"{n}的阶乘为：{fun(n)}")

# 3、求圆的面积
# r=int(input("请输入圆的半径："))
# s=3.14*r*r
# print(f"半径为{r}的圆的面积为：{s}")

# def fun(r):
#     result=3.14*r*r
#     return result
# r=int(input("请输入元的半径："))
# print(f"圆的面积为：{fun(r)}")

# 4、求区间内的素数
# def is_Prime(i):
#     if i==1:
#         return False
#     for j in range(2,i):
#         if i%j==0:
#             return False
#     return True
# def print_isPrime(m,n):
#     for i in range(m,n+1):
#         if is_Prime(i):
#             print(f"{i}是素数")
#
# m=int(input("请输入区间的起始值："))
# n=int(input("请输入区间的结束值："))
# print_isPrime(m,n)

# 5、求前n个数字的平方和
# def fun(n):
#     sum=0
#     for i in range(1,n+1):
#         j=i*i
#         i+=1
#         sum+=j
#     print(f"前{n}个数字的平方和为：{sum}")
#     return sum
#
# n=int(input("请输入一个正整数："))
# fun(n)

# 6、计算列表数字的和
# def sumlist(list):
#     sum=0
#     for i in list:
#         sum+=i
#     print(f"{list}中数字之和为：{sum}")
#     return sum
# list1=[1,3,5,7]
# list2=[2,4,6,8]
# sumlist(list1)
# sumlist(list2)

# 7、求数字范围内的所有偶数
# m=int(input("请输入起始范围的值："))
# n=int(input("请结束起始范围的值："))
# for i in range(m,n+1):
#     if i%2==0:
#         print(f"{i}是偶数")

# def is_oushu(i):
#     if i%2==0:
#         return True
#     return False
#
# def print_isoushu(m,n):
#     for i in range(m,n+1):
#         if is_oushu(i):
#             print(f"{i}是偶数")
#
# m=int(input("请输入起始范围的值："))
# n=int(input("请输入结束范围的值："))
# print_isoushu(m,n)

# 8、从列表中移除多个元素
# def deletenumber(list1,list2):
#     for i in list2:
#         list1.remove(i)
#     print(f"删除{list2}中的元素后的列表{list1}")
#     return list1
# my_list=[2,5,7,9,11]
# lista=[2,11]
# print(f"my_list={my_list}")
# print(f"lista={lista}")
# deletenumber(my_list,lista)

# 9、实现对列表的去重
# list1=[1,3,6,6,7,9,9,3,5,7]
# print(f"{list1}去重后：{list(set(list1))}")

# def quchong(list):
#     result=[]
#     for i in list:
#         if i not in result:
#             result.append(i)
#     return result
#
# list1=[1,3,5,3,6,3,7,6,8,7,9,1,9]
# print(f"{list1}去重后：{quchong(list1)}")

# 10、对简单列表进行排序
# list1=[5,3,2,1,7,9,8]
# print(f"{list1}升序排序后：{sorted(list1)}")
# print(f"{list1}降序排序后：{sorted(list1,reverse=True)}")

# 11、对学生成绩进行排列
# score=[
#     {"学号":1,"姓名":"小娜","成绩":99},
#     {"学号":2,"姓名":"小萱","成绩":100},
#     {"学号":3,"姓名":"小君","成绩":89},
#     {"学号":4,"姓名":"小静","成绩":67}
# ]
# score_sort=sorted(score,key=lambda x:x["成绩"],reverse=True)
# print(f"对成绩排序后：{score_sort}")

# 12、写入文件
# f=open("D:/score.txt","w",encoding="UTF-8")
# f.write("[{'number':1,'name':'Bob','score':66},{'number':2,'name':'Lily','score':77},{'number':3,'name':Gina','score':88}]")
# f.flush()
# f.close

# 13、统计输入字符串中每个字母出现的次数
# str=input("请输入字符串：")
# str1=str.lower()
# n=0
# s=""
# for i in range(26):
#     n=str1.count(chr(97+i))
#     if n!=0:
#         s=s+"{}:{}|".format(chr(97+i),n)
# print(s[:-1])

# 14、
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j}*{i}={i*j}\t",end='')
#     print()

# import random
# n=int(input())
# m=[random.randint(0,999)for m in range(10)]
# c=''.join(map(str,m))
# print(f"{c}")

# string=input()
# num=0
# for x in string:
#     if x.isalpha()or '\u4e00'<=x<='9fa5':
#         num+=1
# print(f"{num}")

# s = input("")
# count = 0
# for x in s:
#     if  x.isalpha()or '\u4e00'<=x<='9fa5':
#        count += 1
# print(count)
# class clock():
#     name=None
#     price=None
#     def ring(self):
#         import winsound
#         result=winsound.Beep(2000,3000)
#         return result
# clok1=clock()
# clok1.name="旋风小闹铃"
# clok1.price=520.000
# print(f"闹钟的名字：{clok1.name},闹钟的价格是：{clok1.price}")
# clok1.ring()

# class students:
#     # n=eval(input("请输入学生人数："))这行应该放在构造参数中
#     def __init__(self):
#         self.n = eval(input("请输入学生人数："))
#         self.students_info = []
#
#     def stu_info(self):
#         for i in range(1, self.n + 1):
#             print(f"当前录入第{i}个学生信息，总共需要录入{self.n}位学生")
#             name = input("请输入学生姓名：")
#             age = int(input("请输入学生年龄："))
#             dizhi = input("请输入学生地址：")
#             self.stu_info.append({"name": name, "age": age, "dizhi": dizhi})
#             print(f"学生{i}信息录入完成：【姓名：{name},年龄：{age},地址：{dizhi}】")
#
#
# stu = students()
# stu.stu_info()
#
# print("\n录入学生信息：")
# for info in stu.students_info:
#     print(f"姓名：{info['name']},年龄：{info['age']},地址：{info['dizhi']}")

# class Student:
#     def __init__(self):
#         self.n = int(input("请输入学生人数："))
#         self.students_info = []
#
#     def input_student_info(self):
#         for i in range(1, self.n + 1):
#             print(f"当前录入第{i}个学生信息，总共需要录入{self.n}位学生")
#             name = input("请输入学生姓名：")
#             age = int(input("请输入学生年龄："))  # 将年龄转换为整数
#             address = input("请输入学生地址：")
#             self.students_info.append({"name": name, "age": age, "address": address})
#             print(f"学生{i}信息录入完成：【姓名：{name},年龄：{age},地址：{address}】")
#
# # 创建Student类的实例
# stu = Student()
# # 调用方法录入学生信息
# stu.input_student_info()
#
# # 打印所有录入的学生信息，可以添加以下代码
# print("\n录入的所有学生信息如下：")
# for info in stu.students_info:
#     print(f"姓名：{info['name']}, 年龄：{info['age']}, 地址：{info['address']}")

# class students:
#     name=None
#     age=None
#     adress=None
#     def __init__(self,name,age,adress):
#         self.name=name
#         self.age=age
#         self.adress=adress
# num=int(input("请输入学生人数："))
# for i in range(1,num+1):
#     print(f"当前正在录入第{i}个学生信息，还剩{num-i}个需要录入！")
#     n=input("请输入学生的姓名：")
#     a=int(input("请输入学生的年龄："))
#     ad=input("请输入学生的地址：")
#     stu=students(n,a,ad)
#     print(f"第{i}个学生信息录入成功，学生信息为：")
#     print(f"【姓名：{stu.name},年龄：{stu.age},地址：{stu.adress}】")

#带有私有成员的手机
# class phone:
#     __is_5g_enable=False
#
#     def __check_5g(self):
#         if self.__is_5g_enable==True:
#             print(f"5g开启")
#         else:
#             print(f"5g关闭，开启4g网络")
#     def call_by_5g(self):
#         self.__check_5g()
#         print(f"正在通话中")
# phone=phone()
# phone.call_by_5g()

s="abcde"
print(f"{s[:1]}")
