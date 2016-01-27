#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Version:Python3.5.0

import pickle

def init_user():
    '''
    构造一个空的用户字典，格式：{'用户名'：['密码',账号被锁状态,余额]}
    :return:None
    '''
    # 先构造一个空字典，存储用户信息的文件 user.pkl
    user_dict = {}
    with open('user.pkl','wb') as f:
        pickle.dump(user_dict,f)
    print('init user info finish!')
    return None

if __name__ == '__main__':
    init_user()