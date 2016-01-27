#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Version:Python3.5.0

import pickle

def product_info():
    '''
    商品信息，返回一个商品信息的字典
    :return:product_list 和 product_list_index
    '''
    # 初始化商品列表
    product_dict = {'bike': 688, 'iphone6s': 5088, 'coffee': 35,
                    'car':88888, 'iPad Air': 3500, 'jacket': 300,
                    'MacBook pro': 12345, 'hamburger': 80}
    # 给商品添加索引
    product_list_index = [(index+1, key, product_dict[key]) for index, key in enumerate(product_dict)]
    return product_dict,product_list_index

def register():
    '''
    注册新用户
    :return: None
    '''
    while True:
        # 输入注册账号
        username = input('Please input registered account: ').strip()
        # 输入为空，重新输入
        if username == '':continue
        if username in user_dict:
            print('Account already exists, please input again!')
            continue
        else:
            pwd = input('Please input password: ')
            user_dict[username] = [pwd, 0, 0]
            print('Registered successfully!')
            # 把更新后的账号字典保存到文件 user.pkl
            with open('user.pkl', 'wb') as f:
                pickle.dump(user_dict, f)
                break

def login():
    '''
    用户登录，验证账号密码是否正确，密码输入3次则锁定账号
    :return: None
    '''
    flag = False
    # 初始化尝试的次数
    try_count = 0
    while True:
        username = input('Please input the user: ').strip()
        # 输入为空，重新输入
        if username == '':
            continue
        # 如果账号存在
        if username in user_dict:
            # 读取用户字典里面账号输错次数，count为输错次数
            count = user_dict[username][1]
            while True:
                if count < 3:
                    pwd = input('Please input password: ')
                    # 验证密码是否正确
                    if user_dict[username][0] == pwd:
                        print('Login successfully!')
                        # 进入二级菜单选项界面
                        flag = login_module(username)
                        if flag:
                            break
                    else:
                        # 密码错误次数 count 加 1
                        count += 1
                        print('Password error! You have %s times,try again!' % (3-count))
                        continue
                else:
                    # 输错3次后，账号被锁定
                    print('the %s is locked!' % username)
                    # 把该账号的错误次数更新到用户字典中
                    user_dict[username][1] = 3
                    with open('user.pkl', 'wb') as f:
                        # 重新写入到文件user.pkl
                        pickle.dump(user_dict, f)
                    # 账号被锁定后，返回上级菜单
                    break
        else:
            try_count += 1
            # 若果尝试3次后，则返回上级菜单
            if try_count == 3:
                break
            else:
                # 账号不存在，则重新输入，有3次机会
                print('Account does not exist.you have %s times,try again!' %(3-try_count))
                continue
        # 返回上级菜单
        if flag:
            break

def shopping(user):
    '''
    显示商品信息，选择商品索引号，即可加入购物车
    :param user: 登录账号
    :return:
    '''
    user = user
    # 调用商品信息函数,获取商品信息字典以及索引
    product, product_index = product_info()
    # 读取user_dict字典，记录登录的账号拥有的余额
    money = user_dict[user][2]
    print('Your own %s YUAN'.center(35) % money)
    print('-' * 35)
    # 初始化一个空商品列表，记录购买的商品
    shopping_list = []
    # 初始化购买商品总件数
    total_number = 0
    # 初始化花费金额
    total_cost = 0
    # 记录商品最低价格
    mix_price = min(product.values())
    while True:
        for i in product_index:
            # 打印索引号，添加两个空格显示
            print(i[0],end='  ')
            # 设置商品名称长度13，左对齐显示
            print(i[1].ljust(13),end='')
             # 打印商品价格
            print(i[2])

        choose = input('Please choose the index of the product: ').strip()
        if choose.isdigit():
            # 判断输入的索引是否正确,设置索引从1开始
            if int(choose) in range(1, len(product_index)+1):
                # 记录购买商品名称，choose-1 为 该商品在product_index 列表中的索引
                choose_product = product_index[int(choose)-1][1]
                # 判断余额是否大于等于产品的价格
                if money >= product[choose_product]:
                    # 把商品加入购买清单
                    shopping_list.append(choose_product)
                    # 计算花费的金额
                    total_cost += product[choose_product]
                # 余额可以购买最低价的商品
                elif  money >= mix_price:
                    print('Your own %s YUAN, please choose other product.' % money)
                else:
                    print('Your own money can not pay for any product,bye bye!')
                    break
            else:
                print('Input the index error,try again!')
                continue
            # 标记退出
            flag = False
            while True:
                print('Your rest money is %s.' % (money-total_cost))
                continue_shopping = input('Continue shopping？y or n: ').strip()
                if continue_shopping == 'y':
                    break
                elif continue_shopping == 'n':
                    flag = True
                    break
                else:
                    continue
            if flag:
                break
        else:
            print('Input error,try again!')
            continue

    product_set = set(shopping_list)
    print('*' * 35)
    # 打印购物单表头信息
    print('Your shopping list'.center(35))
    print('Product'.ljust(15),'Price'.ljust(7),'Number'.ljust(5),'cost'.ljust(7))
    print('-' * 35)
    for i in product_set:
        number = shopping_list.count(i)
        total_number += number
        cost = product[i] * number
        print('%s %s %s  %s' % (i.ljust(15),str(product[i]).ljust(7),
                            str(number).ljust(5), str(cost).ljust(7)))
    print('-' * 35)
    print('''All number: %s All cost: %s'''
          % (str(total_number).ljust(7), str(total_cost).ljust(7)))
    print('Your rest money is %s.' % (money-total_cost))

    with open('user.pkl','wb') as f:
        # 更新账号的余额，保存到文件user.pkl
        user_dict[user][2] = money-total_cost
        pickle.dump(user_dict, f)

def  rechange(user):
    '''
    新注册的账号默认余额都是0元，登录系统后需要进行充值才可以购买商品
    :param user: 登录账号
    :return: None
    '''
    # 获取参数user
    user = user
    input_money = input('Please input the money of yourself: ').strip()
    while True:
        if input_money.isdigit():
            user_dict[user][2] = int(input_money)
            with open('user.pkl','wb') as f:
                # 更新账号的余额，保存到文件user.pkl
                pickle.dump(user_dict, f)
            print('Rechange successfully!')
            break
        else:
            print('Input error,try again!')
            continue

def  query_balance(user):
    '''
    查询自己的余额
    :param user: 登录账号
    :return: None
    '''
    # 获取参数user
    user = user
    # 打印余额
    print('Your own money %s YUAN.'% user_dict[user][2])

def login_module(user):
    '''
    显示登录成功后的界面
    :param user: 登录账号
    :return: True
    '''
    user = user
    # 登录后显示界面的选项信息
    second_menu = [['1', 'rechange'], ['2','query_balance'], ['3', 'shopping'],
                   ['4', 'return'], ['5', 'exit']]
    while True:
        print('*' * 35)
        # 打印二级菜单选项
        for i in second_menu:
            for j in i:
                print(j, end=' ')
            print('')
        choose = input('Please input the index: ').strip()
        if choose == '':
            continue
        # 选择充值索引，执行充值函数
        if choose == '1':
            rechange(user)
        # 选择查询余额索引，执行查询余额函数
        elif choose == '2':
            query_balance(user)

        # 选择购物索引，执行购物函数
        elif choose == '3':
            shopping(user)
        # 返回上级菜单
        elif choose == '4':
            break
        # 结束程序
        elif choose == '5':
            exit()
        # 输入不匹配，重新输入
        else:
            print('Input error, try again!')
            continue
    return True
if __name__ == '__main__':
    # 预读取账号信息文件 user.pkl,给函数调用
    with open('user.pkl', 'rb') as f:
        # 读取用户信息
        user_dict = pickle.load(f)

    # 构造主菜单列表选项
    main_menu = [['1', 'register'], ['2','login'], ['3', 'exit']]
    while True:
        print('**** Welcome to mall ****')
        # 打印主菜单选项
        for i in main_menu:
            for j in i:
                print(j, end=' ')
            print('')
        choose = input('Please input the index: ').strip()
        if choose == '':
            continue
        # 选择注册索引，执行注册函数
        if choose == '1':
            register()
        # 选择登录索引，执行登录函数
        elif choose == '2':
            login()
        # 选择退出，则程序运行结束
        elif choose == '3':
            print('Good bye!')
            break
        # 输入不匹配，重新输入
        else:
            print('Input error, try again!')
            continue