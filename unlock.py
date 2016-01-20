# -*- coding:utf-8 -*-
# version:python3.5

import pickle
# 初始化用户以及密码
user_dict = {'admin':{'passwd':'admin','flag':'unlock'}}

# 把账号、密码保存到文件中
with open('account.pkl','wb') as f:
    pickle.dump(user_dict, f)