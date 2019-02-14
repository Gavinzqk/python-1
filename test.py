#！/usr/bin/env python
# _*_ encoding:utf-8 _*_
# author:snate
import time
# 将商品列表从文件中读出，并写入字典
def ReadProductDic():
    with open('Product_List.txt', 'r', encoding="utf-8") as f:
        for line in f.readlines():
            Product_Info = line.strip("\n").split(" ")
            # Index = int(Product_Info[0])
            Product_Name = Product_Info[1]
            Product_Price = Product_Info[2]
            Product_List[Product_Name] = int(Product_Price)
# 将购买的商品以及商品的数量写入到文件中
def WriteShoppingProductFile(Shopping_Chart):
    with open('Shopping_list.txt', 'a', encoding="utf-8") as f:
        for index,Proudct_Name in enumerate(Shopping_Chart):
            Product_Str=""
            index = str(index)
            Prduct_Num = str(Shopping_Chart[Product_Name])
            Product_Str= Product_Str+index + " " + Product_Name + " "+ Prduct_Num
            f.writelines(Product_Str+"\n")
# 退出系统
def Exit_System():
    for i in  range(3):
        print('''\n\t\t谢谢使用电子购物商城，\033[34;1m%s\033[0m秒后，退出系统！''' %(3-i))
        time.sleep(1)
    exit()
# 判断是否需要继续
def BreakFlag():
    while True:
        Break_Flag = input('''\t\t您是否要继续？（y/n)''')
        if  Break_Flag =="y" or Break_Flag == "n":
            return Break_Flag
        else:
            print("您的输入有误，请重新输入")
# 遍历 商品字典 输入商品编号，商品的名称 商品的价格
def ThroughProductDic(Product_list):
    for index, Product in enumerate(Product_list):
        Dic_key[index] = Product
        print(index,Product,Product_List[Product])
#   遍历购物车字典，打印序号、商品名称、商品的单价、商品的数量
def ThroughShoppingDic(Shopping_Chart):
    for index,name in enumerate(Shopping_Chart):
        Dic_key[index] = name
        print('''\n\t\t%s\t\t%s\t\t%s\t\t%s\t\t''' %(index,name,Product_List[name],Shopping_Chart[name]))
Dic_key = {}
Shopping_Chart = {}  # 保存购买的商品
# 商品列表
Product_List={}
ReadProductDic()
# 判断工资标准
name=input('请输入您的用户名：')
print('''\n\t\t\t\t\033[31;5m欢迎%s来到电子商城\033[0m''' %name)
with open("user.txt",'r+',encoding='utf-8') as f:
    count = f.readlines().count(name)
    cnt = 0
    for line in f.readlines():
        line = line.strip("\n").split(" ")
        # 文件中可能存在多个用户的余额信息，选取最后的余额
        if name == line[1]:
            cnt += 1
            if cnt == count:
                balance = line[2]
                break
    else:
        Balance = input("请输入您的工资：")
        Balance = int(Balance)
while True:
    Break_Flag =''
    print('''\n\t请选择您需要进行的操作：\n\t\t\t\t1.购物\n\t\t\t\t2.查看并修改购物车\n\t\t\t\t3.结账并退出''')
    # 用来确定用户的选择
    while True:
        choose = input('''\n\t请输入您的选择''')
        if choose.isdigit():
            choose = int(choose)
            if choose >=4 or choose <= 0:
                print('''\n\t\t您的输入有误，请重新输入，谢谢！''')
            else:
                break
        elif choose == "q":
            print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
            ThroughShoppingDic(Shopping_Chart)
            WriteShoppingProductFile(Shopping_Chart)
            print('''您的余额为：%s''' % Balance)
            Exit_System()
        else:
            print("invalid option")
    # 用户的选择为1，购物
    if choose == 1:
        while Break_Flag != 'n':
            ThroughProductDic(Product_List)
            User_Choose = input('''\t\t请输入您要购买的商品的编号：''')
            if User_Choose.isdigit():
                User_Choose = int(User_Choose)
                if User_Choose >=0 and User_Choose<len(Dic_key):
                    Product_Name = Dic_key[User_Choose]
                    if Product_List[Product_Name]< Balance:
                        Balance -= Product_List[Product_Name]
                        print('''\t\t将商品\033[31;1m[%s]\033[0m加入到购物车！''' %Product_Name)
                        # 判断商品是否在购物车中，如果在购物车中的数量加1，若果不在购物车中，
                        if Product_Name in Shopping_Chart:
                            Shopping_Chart[Product_Name] += 1
                        else:
                            Shopping_Chart[Product_Name] =1
                    else:
                        print('''\t\t您的余额不足，请重新输入！''')
                else:
                    print('''\t\t您输入的编号为\033[31;1m%s]\033[0m不存在'''% User_Choose)
            elif User_Choose == 'q':
                print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
                ThroughShoppingDic(Shopping_Chart)
                WriteShoppingProductFile(Shopping_Chart)
                print('''您的余额为：%s''' % Balance)
                with open("user.txt", 'r+', encoding='utf-8') as f:
                    User_Info = name+ ""+str(Balance)
                    f.writelines(User_Info+"\n")
                Exit_System()
            else:
                print("invalid option")
            Break_Flag = BreakFlag()

    elif  choose == 2:
        while True:
            ThroughShoppingDic(Shopping_Chart)
            Shopping_Chart_Choose = input('''\t\t1.增加\n\t\t2.删除\n\t\t3.结账并退出\n\t\t4.返回\n\t\t请输入您的选择：''')
            if Shopping_Chart_Choose.isdigit():
                Shopping_Chart_Choose = int(Shopping_Chart_Choose)
                if Shopping_Chart_Choose<=0 or Shopping_Chart_Choose >= 5:
                    print('''您输入编号为[%s]的操作不存在，请您重新输入！''' % Shopping_Chart_Choose)
                else:
                    break
            elif  Shopping_Chart_Choose=="q":
                print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
                ThroughShoppingDic(Shopping_Chart)
                WriteShoppingProductFile(Shopping_Chart)
                print('''您的余额为：%s''' % Balance)
                with open("user.txt", 'r+', encoding='utf-8') as f:

                    User_Info = name + "" + str(Balance)
                    f.writelines(User_Info + "\n")
                Exit_System()
            else:
                print("您的输入有误，请重新输入")
        if Shopping_Chart_Choose == 1:
            while  Break_Flag != 'n':
                ThroughShoppingDic(Shopping_Chart)
                Add_Shoppping_Index = input('''\n\t\t请输入您要增加商品的编号：''')
                if Add_Shoppping_Index.isdigit():
                    Add_Shoppping_Index = int(Add_Shoppping_Index)
                    if Add_Shoppping_Index>= 0 and Add_Shoppping_Index<len(Shopping_Chart):
                        Add_Product_Name = Dic_key[Add_Shoppping_Index]
                        while Break_Flag != 'n':
                            Add_Product_Num = input('''\t\t请输入您要增加的商品数量：''')
                            if Add_Product_Num.isdigit():
                                Add_Product_Num = int(Add_Product_Num)
                                if Balance >= Product_List[Add_Product_Name]*Add_Product_Num:
                                    Shopping_Chart[Add_Product_Name] += Add_Product_Num
                                    Balance -= Product_List[Add_Product_Name]*Add_Product_Num
                                else:
                                    print('''\t\t您的余额不足！''')
                            elif Add_Product_Num == "q":
                                print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
                                ThroughShoppingDic(Shopping_Chart)
                                WriteShoppingProductFile(Shopping_Chart)
                                print('''您的余额为：%s''' % Balance)
                                Exit_System()
                            else:
                                print('invalid option')
                            Break_Flag = BreakFlag()
                    else:
                        print('''您输入编号为[%s]的操作不存在!''' % Shopping_Chart_Choose)
                elif Add_Shoppping_Index == 'q':
                    print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
                    ThroughShoppingDic(Shopping_Chart)
                    WriteShoppingProductFile(Shopping_Chart)
                    print('''您的余额为：%s''' % Balance)
                    with open("user.txt", 'r+', encoding='utf-8') as f:
                        User_Info = name + "" + str(Balance)
                        f.writelines(User_Info + "\n")
                    Exit_System()
                else:
                    print("invalid option")
                Break_Flag = BreakFlag()
        elif Shopping_Chart_Choose==2:
            while Break_Flag != 'n':
                ThroughShoppingDic(Shopping_Chart)
                Del_Shoppping_Index = input('''\n\t\t请输入您要删除商品的编号：''')
                if Del_Shoppping_Index.isdigit():
                    Del_Shoppping_Index = int(Del_Shoppping_Index)
                    if Del_Shoppping_Index >= 0 and Del_Shoppping_Index < len(Shopping_Chart):
                        Del_Product_Name = Dic_key[Del_Shoppping_Index]
                        while Break_Flag != 'n':
                            Del_Product_Num = input('''\t\t请输入您要增加的商品数量：''')
                            if Del_Product_Num.isdigit():
                                Del_Product_Num = int(Del_Product_Num)
                                if Del_Product_Num>=0 and Del_Product_Num<=Shopping_Chart[Del_Product_Name]:
                                    Balance += Product_List[Del_Product_Name]*Del_Product_Num
                                else:
                                    print('''\t\t您输入的商品数量有误，请重新输入！''')
                            elif Add_Product_Num == "q":
                                print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
                                ThroughShoppingDic(Shopping_Chart)
                                WriteShoppingProductFile(Shopping_Chart)
                                print('''您的余额为：%s''' % Balance)
                                with open("user.txt", 'r+', encoding='utf-8') as f:
                                    User_Info = name + "" + str(Balance)
                                    f.writelines(User_Info + "\n")
                                Exit_System()
                            else:
                                print('invalid option')
                            Break_Flag = BreakFlag()
                    else:
                        print('''您输入编号为[%s]的操作不存在!''' % Shopping_Chart_Choose)
                elif Add_Shoppping_Index == 'q':
                    print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
                    ThroughShoppingDic(Shopping_Chart)
                    WriteShoppingProductFile(Shopping_Chart)
                    print('''您的余额为：%s''' % Balance)
                    with open("user.txt", 'r+', encoding='utf-8') as f:
                        User_Info = name + "" + str(Balance)
                        f.writelines(User_Info + "\n")
                else:
                    print("invalid option")
                Break_Flag = Break_Flag
        elif Shopping_Chart_Choose==3:
            print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
            ThroughShoppingDic(Shopping_Chart)
            Exit_System()
        else:
            continue
    else:
        print('''\n\t\t序号\t\tname\t\tprice\t\tnum\t\t''')
        ThroughShoppingDic(Shopping_Chart)
        WriteShoppingProductFile(Shopping_Chart)
        print('''您的余额为：%s''' %Balance)
        with open("user.txt", 'r+', encoding='utf-8') as f:
            User_Info = name + "" + str(Balance)
            f.writelines(User_Info + "\n")
        Exit_System()