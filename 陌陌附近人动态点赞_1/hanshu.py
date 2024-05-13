from ascript.android.system import R

# 导入动作模块
from ascript.android import action

# 导入节点检索模块
from ascript.android import node

# 导入图色检索模块
from ascript.android import screen

# 导入控件查找器
from ascript.android.node import Selector

from airscript.action import click
from ascript.android.screen import gp

from ascript.android.screen.gp import GPStack
import cv2
from ascript.android.system import R
from ascript.android import plug
from ascript.android.screen import FindImages
from ascript.android.screen import Ocr
import time
import random



def shaixuanfujin():
    print(10, "秒后开始执行筛选")
    num_fujin = 10
    for i_num in range(num_fujin):
        print("#", end="", flush=True)
        time.sleep(1)

    # # 点击附近
    ###附近控件位置
    Selector().type("FrameLayout").id("com.immomo.momo:id/nearby_people_filter").click().find_all()

    # # # time.sleep(2)

    # # # # ---------------------点击筛选----------------------
    print("正在筛选“男”，等待", 10, "秒")
    

    num_shaixuan = 10
    for i_num in range(num_shaixuan):
        print("#", end="", flush=True)
        time.sleep(1)

    ##筛选控件位置
    Selector().id("com.immomo.momo:id/nearby_people_filter").type(
        "FrameLayout"
    ).click().find_all()

    # # -------------------------筛选男生-----------------------
    time.sleep(random.randint(3, 5))
    ###男生控件位置
    res_man_yxz = FindImages.find_all_template([R.img("4.png"),],confidence= 0.95)
    l_res_man_ydz = len(res_man_yxz)
    if l_res_man_ydz != 0:
        print("已经筛选，下一步完成")
    else:
        res_man = FindImages.find_all_template([R.img("2.png"),],confidence= 0.95)
        res_man_list = res_man[0]
        res_man_list1 = res_man_list['rect']
        res_man_x = res_man_list1[0]
        res_man_y = res_man_list1[1]
        action.click(res_man_x,res_man_y)

    # # -----------------------完成筛选---------------------------
    time.sleep(random.randint(3, 5))
    ##完成控件位置（不用动）
    Selector().text("完成").type("Button").click().find_all()
    print("筛选完成")

    # # ----------------------------------------------------点击头像进入主页(随机点击，n个选择一个)-------------------------------------------------------------
    # time.sleep(random.randint(5, 7))


def dianjitouxiang():
    print("等待", 10, "秒点击头像")
    num_head = 10  # 10
    for i_num in range(num_head):
        print("#", end="", flush=True)
        time.sleep(1)

    click_head = (
        Selector()
        .type("ImageView")
        .path(
            "/FrameLayout/ViewPager/RecyclerView/FrameLayout/ViewGroup/FrameLayout/ImageView"
        )
        .parent(1)
        .find_all()
    )

    ##--------------------判断是否在线---------------------
    if isinstance(click_head, type(None)):
        print("无在线，等待十秒后自动刷新")
        time.sleep(10)
        Selector().id("com.immomo.momo:id/tab_item_tv_label").text("首页").type(
            "TextView"
        ).path("/FrameLayout/FrameLayout/TextView").parent(1).click().find_all()

        time.sleep(3)
        click_head = (
            Selector()
            .type("ImageView")
            .path(
                "/FrameLayout/ViewPager/RecyclerView/FrameLayout/ViewGroup/FrameLayout/ImageView"
            )
            .parent(1)
            .find_all()
        )
        print("已刷新，等", 10, "秒后继续")

        num_head = 10  # 10
        for i__num in range(num_head):
            print("#", end="", flush=True)
            time.sleep(1)

        # print(click_head)
        l_click_head = len(click_head)
        # print(l_click_head)
        # 随机选择头像点击的随机数
        click_head_i = random.randint(0, l_click_head - 1)
        # print(click_head_i)
        # 随机选择头像点击
        time.sleep(5)
        click_head[click_head_i].click()
    else:
        l2_click_head = len(click_head)
        click_head_i_2 = random.randint(0, l2_click_head - 1)
        time.sleep(5)
        click_head[click_head_i_2].click()


    ## 点击动态
    time.sleep(5)
    Selector().text("动态").type("TextView").parent(1).click().find_all()
    time.sleep(3)
    print("执行滑动")
    action.swipe(443,1729, 479,566, 3000)
    time.sleep(3)
    res_ydz = FindImages.find_all_template([R.img("3.png"),],confidence= 0.95)
    l_res_ydz = len(res_ydz)
    if l_res_ydz == 0:
        res_dz = FindImages.find_all_template([R.img("1.png"),],confidence= 0.95)
        l_res_dz = len(res_dz)
        if l_res_dz != 0:
            rect_dz_list = res_dz[0]
            rect_dz_list1 = rect_dz_list['rect']
            rect_dz_x = rect_dz_list1[0]
            rect_dz_y = rect_dz_list1[1]
            time.sleep(3)
            action.click(rect_dz_x,rect_dz_y)
            print("已点赞，等待退出")
            time.sleep(5)
            Selector().type("ImageView").id("com.immomo.momo:id/iv_back").click().find_all()
        else:
            print("无动态，等待退出")
            time.sleep(3)
            Selector().type("ImageView").id("com.immomo.momo:id/iv_back").click().find_all()

    else:
        print("已点赞，等三秒退出")
        Selector().type("ImageView").id("com.immomo.momo:id/iv_back").click().find_all()
    print("等待", 120, "进行下一个流程")
    num_head = 120  # 10
    for i_num in range(num_head):
        print("#", end="", flush=True)
        time.sleep(1)   
    