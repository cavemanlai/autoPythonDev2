#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Version:python3.5.0
import  pickle
import os
import random

with open('account.pkl','rb') as f:  # 载入用户账户密码信息
    user_dict = pickle.load(f)

exit_flag = False   #初始化锁定的状态为false
count_lock = 0  # 初始化账号锁定次数为0次

print('**********************************')
while True:
    user = input('请输入账号: ').strip()
    if user == '':continue  # 用户名为空，重新输入
    passwd = input('请输入密码: ').strip()

    # 判断是否存在输入的账号
    if user_dict.get(user):
        # 判断账号是否锁定，锁定则退出。
        if user_dict[user]['flag'] == 'lock':
            print('账号已经锁定，请解锁！')
            break
        # 验证密码是否正确
        if user_dict[user]['passwd'] == passwd:
            while True:
                guess_choise = input('你要开始玩猜数字游戏么?(选择yes或no): ').strip()
                if guess_choise == '':continue
                elif guess_choise == 'yes':
                    print('欢迎登陆Python自动化开发--猜数字系统')
                    print('*******************************************')
                    print('猜数字的范围在1到10之间.')
                    real_num = random.randrange(1,11)   # 随机生成1到10之间的一个数字
                    retry_count = 0
                    while retry_count < 3:  # 有3次机会猜数字
                        guess_num = input('请输入你猜的数字: ').strip()
                        if guess_num == '':continue
                        if guess_num.isdigit():
                            guess_num = int(guess_num )
                            if guess_num > real_num :
                                print('错误，请输入一个小一点的数字！')
                            elif guess_num < real_num :
                                print('错误，请输入一个大一点的数字！')
                            else:
                                print('恭喜你，猜到你幸运的数字 %s ！！！' % real_num)
                                break
                        else:
                            print('输入的不是数字，请重新输入一个数字')
                            continue

                        retry_count +=1
                    else:
                        print('哦哦，幸运数字是 %s，下次肯定会猜中的哦！' % real_num)
                        print('-------------------------------------')

                elif guess_choise == 'no': # 不想猜数字游戏，则直接退出系统
                    print('欢迎再次登录！')
                    exit_flag = True
                    break
                else:
                    print('你输入的不是yes或者no,请重新输入。')
                    continue
        else:
            count_lock += 1 # 密码不正确，统计输错次数
            if (3 - count_lock):
                print('账号或密码错误，还有 %s 次机会尝试登陆！' % (3-count_lock))

        if count_lock == 3:   # 若锁定次数有3次，就锁定账号
            with open('account.pkl','wb') as f:
                user_dict['admin']['flag'] = 'lock'     # 标志账号admin为锁定状态
                user_dict = pickle.dump(user_dict, f)   # 修改后数据写到 account.pkl中
            print('*******************************************')
            print('账号被锁定，请解锁！')
            break
    else:
        print('输入的账号不存在，请重新输入！')
        continue

    if exit_flag:   # 在猜数字游戏中，选择no，则直接退出整个程序
        break

print('Bye bye!')