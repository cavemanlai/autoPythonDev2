#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Version:Python3.5.0

# 初始化城市信息
city_dict = {'广州': {'天河': ['天河体育馆', '金山大夏'],
                    '越秀': ['越秀公园', '光孝寺'],
                    '番禺': ['长隆欢乐世界', '大夫山']},
             '深圳': {'福田': ['莲花山', '赛格'],
                    '龙华': ['元山公园', '龙城广场'],
                    '南山': ['世界之窗', '欢乐谷']},
             '佛山': {'禅城': ['梁园', '孔庙'],
                    '南海': ['千灯湖', '南国桃园'],
                    '顺德': ['清晖园', '西山庙']}}

# 创建城市索引列表
city_index = [(index, key) for index, key in enumerate(city_dict)]
city_index.append((len(city_index), '退出')) # 增加退出选项
while True:
    print('欢迎查询城市信息')
    print('--------------------------------')
    for i in city_index:    # 打印城市索引菜单
        for j in i:
            print(j, end=' ')
        print('')

    get_city = input('请选择查询的索引号：')
    if not get_city.isdigit():
        print('请输入一个数字索引号。')
        continue
    elif int(get_city) >= len(city_index):   # 输入索引号大于等于城市索引号长度
        print('输入的数字太大，请重输入。')
        continue
    elif int(get_city) == len(city_index)-1:   # 最大的索引号为 退出程序对应的索引号
        print('欢迎再次登录，bye bye!')
        break
    else:
        choose_city = city_index[int(get_city)][1]   # 获取选择的城市名称
        # 创建 区 的索引列表
        area_index = [(index, key) for index, key in enumerate(city_dict[choose_city])]
        area_index.append((len(area_index), '返回'))  # 增加返回上一级菜单选项
        while True:
            for i in area_index:    # 打印选择城市的区索引菜单
                for j in i:
                    print(j, end=' ')
                print('')

            get_area = input('请选择查询的索引号：')
            if not get_area.isdigit():
                print('请输入一个数字索引号。')
                continue
            elif int(get_area) >= len(area_index):   # 输入索引号大于城市索引号
                print('输入的数字太大，请重输入。')
                continue
            elif int(get_area) == len(area_index)-1:  # 最大的索引号为 上级菜单对应的索引号
                print('返回到上一级菜单。')
                break
            else:
                choose_area = area_index[int(get_area)][1]  # 获取选择区的名称
                print(city_dict[choose_city][choose_area])  # 打印该区的信息
                print('--------------------------------')