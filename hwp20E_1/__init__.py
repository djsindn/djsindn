# __init__.py 为初始化加载文件

# 导入系统资源模块
from ascript.android.system import R

# 导入动作模块
from ascript.android import action

# 导入节点检索模块
from ascript.android import node
from ascript.android.node import Selector

# 导入图色检索模块
from ascript.android import screen
from airscript.action import click
from ascript.android.ui import Loger


import time
import random
from .momohanshu import *


###########################################################
# 华为p20：陌陌养号脚本，脚本定制请联系电话： 19392790683    #
#         微信同号                                        #
###########################################################
###########################################################
# 更新时间：5.10
# 更新内容：添加功能，进入象棋挂机
#                                                         #
###########################################################


# # 点击陌陌所在文件框

# --------------打开文件夹-------------------------------------


open_folde()
while True:

    # # 打开陌陌
    # -------------------打开陌陌-----------------------------------
    momo_click = (
        Selector()
        .text("MOMO陌陌")
        .type("TextView")
        .packageName("com.huawei.android.launcher")
        .path("/FrameLayout/LinearLayout/ViewGroup/TextView")
        .find_all()
    )
    l_momo_click = len(momo_click)
    print("陌陌总数共计", l_momo_click, "个")


    # 倒计时延时
    # ----------------------------倒计时------------------------
    print("10后秒打开陌陌")
    num_10 = 10
    for i_10 in range(num_10):
        print("#", end="", flush=True)
        time.sleep(1)


    # # 轮流打开陌陌
    # --------------------------while 循环 --------------------------------
    i_open_momo = 0
    while i_open_momo < l_momo_click:

        # 点击陌陌
        # print(momo_click)

        momo_click[i_open_momo].click()
        # print(momo_click[i_open_momo])
        # print(i_open_momo)
        time.sleep(10)
        print("当前运行的是第一个")
        print("等待60秒")
        num_60 = 60
        for i_num in range(num_60):
            print("#", end="", flush=True)
            time.sleep(1)
        ########################################################################
        print("已打开第", i_open_momo + 1, "个陌陌")  #

        # --------------功能实现：点击附近 筛选 性别男 点击完成----------------------

        yanghaocaozuoO()
        print("已经完成筛选，下一步进入用户主页")

        # # --------------功能实现：点击头像进入主页 点关注 返回附近--------------------
        time.sleep(3)
        action.swipe(337, 1273, 354, 208, 3000)
        dianjitouxiang()
        # ich = 0
        # while ich <= 5:
        #     print("进入用户主页")
        #     action.swipe(337, 1273, 354, 208, 3000)
        #     dianjitouxiang()
        #     action.swipe(337, 1273, 354, 208, 3000)
        #     randint_time_num4 = random.randint(50, 60)
        #     print(randint_time_num4, "分钟后进入下一次循环")

        #     num_60 = randint_time_num4
        #     for i_num in range(num_60):
        #         print("#", end="", flush=True)
        #         time.sleep(1)
        #     ich += 1

        # # -------------功能实现： 动态浏览 点赞 ---------------------------

        dianjidongtai()

        # # --------------功能实现：自动发动态-------------------------------

        #fadongtai()

        ## ----------------功能实现：自动回关粉丝----------------------------

        fensihuiguan()

        # # --------------功能实现：进入群组，发信息（仅发一条信息）

        group_faxinxi()

        ## ---------------功能实现：进入象棋挂市场 一个小时--------------------

          into_xiangqi()

        # # ----------------功能实现： 看直播 -----------------

        # kanzhibo()

        ###########################################################################
        time.sleep(5)
        action.Key.home()
        time.sleep(2)

        ###------------------功能实现：清理后台----------------------------------

        action.Key.home()
        time.sleep(5)
        print("5秒后开始清理后台")
        # 弹出任务栏
        action.Key.recents()
        # 点击清理
        Selector().desc("关闭所有最近打开的应用").type("ImageView").click().find_all()

        print("等待1分钟")
        num_120 = 60  # 120
        for i_num in range(num_120):
            print("#", end="", flush=True)
            time.sleep(1)  # 测试15秒 实际环境 30秒

        i_open_momo += 1
        open_folde()

    else:
        print("流程结束，请关闭脚本")
# # ------------------结束循环-----------------------------------
