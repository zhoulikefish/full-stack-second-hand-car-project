# -*- coding: utf-8 -*-
# @Time    : 2023/7/11 14:42
# @Author  : Zhang Shiqing
# @File    : temp.py
# @Software: PyCharm

import pandas as pd
import numpy as np

# 读取数据
car_df = pd.read_csv('./车主指南网-7.15.csv')

# 拼接
car_df['image_paths'] = car_df['image_paths'].str.replace('[', '').str.replace(']', '').str.replace('\'', '')
car_df = car_df.dropna(subset=['price_field'])
car_df = car_df.dropna(subset=['car_img'])
# https://imgs.icauto.com.cn/shcarimg/nofind.png

car_df = car_df[car_df['car_img'] != 'https://imgs.icauto.com.cn/shcarimg/nofind.png']
car_df['car_img'] = car_df['image_paths']
car_df = car_df.drop(columns=["image_paths"])
# 输出数据
car_df.to_csv('./车主指南网-7.15 new.csv', index=False)
