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
    Selector(2).text("附近").id("com.immomo.momo:id/tab_title").parent(
        1
    ).click().find_all()

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
    Selector().id("com.immomo.momo:id/filter_icon_radio_genderMale").text("男生").type(
        "RadioButton"
    ).brother(5).click().find_all()

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
    action.swipe(423, 1924, 482, 804, 3000)
    time.sleep(3)
    dian_zan = (
        Selector()
        .type("TextView")
        .packageName("com.immomo.momo")
        .path("/FrameLayout/ViewPager/RecyclerView/FrameLayout/FrameLayout/TextView")
        .parent(1)
        .find_all()
    )
    if dian_zan != None:

        l_dian_zan = len(dian_zan)
        huadong_i = 0
        while huadong_i < 1:
            print("正在浏览动态，当前是第", huadong_i + 1, "轮浏览")
            action.swipe(333, 1261, 321, 272, 6000)
            time.sleep(10)
            ##--------------------动态点赞---------------

            ##--------------------判断是否点赞------------
            if l_dian_zan == 0:
                print("无点赞页，继续滑动")
                action.swipe(333, 1261, 321, 272, 6000)
            elif 0 < l_dian_zan < 2:
                print("随机点赞")
                # dianzan_1 = random.randint(0, 1)
                # dianzan_2 = random.randint(0, l_dianzan - 1)
                dian_zan[0].click()
            elif l_dian_zan == 2:
                print("正在点赞")
                # dianzan_2 = random.randint(0, 1)
                dian_zan[1].click()
                print("点赞完成")
            else:
                print("已点赞，现在点下一个")
                dianzan_3 = random.randint(1, l_dian_zan - 1)
                dian_zan[dianzan_3].click()

            huadong_i += 1
        else:
            print("点赞完成，等待五分钟退出上一页")
            time.sleep(3)
            num_head = 300  # 10
            for i__num in range(num_head):
                print("#", end="", flush=True)
                time.sleep(1)
                ## 点击返回
                Selector().type("ImageView").packageName("com.immomo.momo").path(
                    "/FrameLayout/FrameLayout/ViewGroup/ImageView"
                ).click().find_all()
    else:
        print("无动态，退出上一页")
        time.sleep(3)
        Selector().type("ImageView").packageName("com.immomo.momo").path(
            "/FrameLayout/FrameLayout/ViewGroup/ImageView"
        ).click().find_all()

    # #------------------------ 进入主页打招呼-----------------------------
    # time.sleep(random.randint(5, 7))
    # num_head = 10
    # for i_num in range(num_head):
    #     print("#", end="", flush=True)
    #     time.sleep(1)

    # Selector().text("打招呼").type("TextView")parent(1).click().find_all()
    # print("已经进入点击打招呼")
    # ### 话术
    # list_huashu = [
    #     "你好呀",
    #     "你在干嘛呢",
    #     "见到你很开心",
    #     "你有对象嘛",
    #     "cpdd",
    #     "歪，是我的男神嘛",
    #     "听说这样打招呼会被回复",
    #     "可以互相关注嘛",
    #     "你网名真不错呀",
    #     "你多大啦",
    #     "可以认识一下嘛",
    #     "想跟你聊聊天可以嘛",
    # ]
    # time.sleep(random.randint(1, 3))
    # random_num = random.randint(0, 12)
    # action.input(list_huashu[random_num])
    # print("已经编辑好话术")
    # # 点击发送
    # time.sleep(random.randint(1, 3))
    # Selector(). type(
    #     "Button"
    # ).id("com.immomo.momo:id/message_btn_sendtext").click().find_all()

    # --------------点关注------------------------
    # #time.sleep(5)

    # print("等待", 10, "秒自动关注")
    # num_head = 10  # 10
    # for i_num in range(num_head):
    #     print("#", end="", flush=True)
    #     time.sleep(1)

    # # --------------判断是否已经关注------------------
    # no_guanhuz = (
    #     Selector()
    #     .id("com.immomo.momo:id/profile_tv_start_chat")
    #     .text("关注")
    #     .type("TextView")
    #     .path("/FrameLayout/FrameLayout/TextView")
    #     .find()
    # )

    # if no_guanhuz == None:
    #     print("返回上一页")
    #     action.Key.back()

    # else:
    #     print("正在关注")
    #     Selector().type("TextView").text("关注").parent(1).click().find()
    #     time.sleep(2)
    #     action.Key.back()

    # ---------------返回附近的人---------------------
    # action.Key.back()
    ##---------------点击动态-----------------------
