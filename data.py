"""
Created on 24th Jan 2024
@author: dazhi guan
"""
# 导入 pandas 和 matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# 读取文件
df= pd.read_excel('E:/10_TestProject/13_ICV_BMW/DynamicData/RT_data/RT_data_XLS/Case1_HalfAccele30_01.XLS')

# print(data["t"])
plt.plot(df["t"],df["Speed2D"],label='Speed',linewidth=1,color='c',marker='s',markerfacecolor='blue',markersize=1)
plt.plot(df["t"],df["AccelForward[m/s虏]"],label='Speed',linewidth=1,color='c',marker='s',markerfacecolor='red',markersize=1)
plt.plot(df["t"],df["AngleHeading[掳]"],label='Speed',linewidth=1,color='c',marker='.',markerfacecolor='green',markersize=1)

plt.xlabel("Time")
#横坐标为物品编号
plt.ylabel('Speed')
#纵坐标为各类指标
plt.title("Time&Speed")

plt.show()