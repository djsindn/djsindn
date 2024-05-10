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

randint_time_num = random.randint(10, 20)
randint_time_num1 = random.randint(10, 20)
randint_time_num2 = random.randint(20, 25)


###########################################################
# 华为p20：陌陌养号脚本，脚本定制请联系电话： 19392790683    #
#         微信同号                                        #
###########################################################
# ---------------------打开文件夹---------------------------
def open_folde():
    print(randint_time_num, "秒后打开文件夹")
    num_fujin = randint_time_num
    for i_num in range(num_fujin):
        print("#", end="", flush=True)
        time.sleep(1)
    MOMO_txt = (
        Selector()
        .id("com.huawei.android.launcher:id/folder_icon_name")
        .text("陌陌")
        .type("TextView")
        .packageName("com.huawei.android.launcher")
        .parent(1)
        .find_all()
    )
    MOMO_txt[0].click()
    print("文件夹已打开")


# -----------------------------------------------------------------附近人筛选男生------------------------------------------------------------------
def yanghaocaozuoO():
    print(randint_time_num, "秒后开始执行筛选")
    num_fujin = randint_time_num
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
    print("正在筛选“男”，等待", randint_time_num, "秒")

    num_shaixuan = randint_time_num
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
    print("等待", randint_time_num, "秒点击头像")
    num_head = randint_time_num  # 10
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
        print("已刷新，等", randint_time_num, "秒后继续")

        num_head = randint_time_num  # 10
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

    print("等待", randint_time_num, "秒自动关注")
    num_head = randint_time_num  # 10
    for i_num in range(num_head):
        print("#", end="", flush=True)
        time.sleep(1)

    # --------------判断是否已经关注------------------
    no_guanhuz = (
        Selector()
        .id("com.immomo.momo:id/profile_tv_start_chat")
        .text("关注")
        .type("TextView")
        .path("/FrameLayout/FrameLayout/TextView")
        .find()
    )

    if no_guanhuz == None:
        print("返回上一页")
        action.Key.back()

    else:
        print("正在关注")
        Selector().type("TextView").text("关注").parent(1).click().find()
        time.sleep(2)
        action.Key.back()

    # ---------------返回附近的人---------------------
    # action.Key.back()
    ##---------------点击动态-----------------------


######-------------------------------------------------------动态点赞--------------------------------------------------------------------------------------------------####
def dianjidongtai():

    print("等待", randint_time_num, "秒跳转动态")
    num_head = randint_time_num  # 10
    for i_num in range(num_head):
        print("#", end="", flush=True)
        time.sleep(1)

    Selector().type("TextView").text("动态").id("com.immomo.momo:id/tab_title").parent(
        1
    ).click().find()

    print("等待", randint_time_num, "秒浏览动态")
    num_head = randint_time_num  # 10
    for i_num in range(num_head):
        print("#", end="", flush=True)
        time.sleep(1)

        dianzan = (
            Selector()
            .type("TextView")
            .path(
                "/FrameLayout/ViewPager/RecyclerView/FrameLayout/FrameLayout/TextView"
            )
            .parent(1)
            .find_all()
        )
        l_dianzan = len(dianzan)
        print(l_dianzan)
    ##-------------------滑动屏幕----------------
    huadong_i = 0
    while huadong_i < 3:
        print("正在浏览动态，当前是第", huadong_i + 1, "轮浏览")
        action.swipe(333, 1261, 321, 272, 6000)
        time.sleep(10)
        ##--------------------动态点赞---------------

        ##--------------------判断是否点赞------------
        if l_dianzan == 0:
            print("无点赞页，继续滑动")
            action.swipe(333, 1261, 321, 272, 6000)
        elif 0 < l_dianzan < 2:
            print("随机点赞")
            # dianzan_1 = random.randint(0, 1)
            # dianzan_2 = random.randint(0, l_dianzan - 1)
            dianzan[0].click()
        elif l_dianzan == 2:
            print("正在点赞")
            # dianzan_2 = random.randint(0, 1)
            dianzan[1].click()
            print("点赞完成")
        else:
            print("已点赞，现在点下一个")
            dianzan_3 = random.randint(1, l_dianzan - 1)
            dianzan[dianzan_3].click()

        huadong_i += 1
    else:
        print("浏览完成，进行下一步操作")


##-----------------------------------------------------------------------自动发动态--------------------------------------------------------------------------
def fadongtai():

    print("正在执行下一步操作：点击更多，请等待", randint_time_num, "秒")

    num_gengduo = randint_time_num  # 10
    for i_num in range(num_gengduo):
        print("-", end="", flush=True)
        time.sleep(1)
    ##----------------点击更多（我的主页）--------------
    Selector().path("/FrameLayout/FrameLayout/TextView").type("TextView").text(
        "更多"
    ).id("com.immomo.momo:id/tab_item_tv_label").parent(1).click().find()

    ##------------------点击发动态----------------------
    print("五秒后点击发动态")
    time.sleep(5)
    Selector().type("TextView").text("发动态").click().find()

    dongtai_huashu = [
        # "生活真的好无聊呀....",
        # "有没有人跟我聊聊天呀",
        # "咖啡的香气，书页的温度，完美的一天从早晨开始。",
        # "雨后的城市，清新的空气，每一步都踏着希望的节奏",
        # "星空下的许愿，愿你我都能梦想成真",
        # "时光不老，我们不散，陌上花开，可缓缓归矣",
        # "一缕阳光，一份温暖，生活的美好就藏在这些瞬间",
        # "用心聆听，风中自有诗和远方",
        # "一句问候，一个点赞，温暖如初。就像奥黛丽·赫本说的：“微笑是最好的名片",
        # "昨夜星辰伴我加班，累得连抱怨都成了奢侈。成果不负苦劳人，项目顺利上线！记住了，天将降大任于斯人也，必先苦其心志。",
        # "今天参加活动，遇见一群光芒四射的伙伴。收获满满，感悟良多。正如乔布斯所说：“和优秀的人相处，自己也会变得优秀",
        # "今天的培训，让我眼界大开。收获满满，知识更新，感觉自己又进步了一点点。正如爱因斯坦所说：“学习的根本目的在于培养思维的独立性。”继续加油，不断成长！",
        "讲个冷笑话，谁能告诉我答案：为什么大象不用电脑？",
        "讲个冷笑话，谁能告诉我答案：为什么猩猩的手指那么长？",
        "讲个冷笑话，谁能告诉我答案：为什么鸡蛋不敢跳高？",
        "讲个冷笑话，谁能告诉我答案：为什么鱼不说话？",
        "讲个冷笑话，谁能告诉我答案：为什么猫头鹰晚上才出来活动？",
        "讲个冷笑话，谁能告诉我答案：为什么猪不会飞？",
        "讲个冷笑话，谁能告诉我答案：为什么蚊子喜欢咬人？",
        "讲个冷笑话，谁能告诉我答案：为什么狗喜欢追车？",
        "讲个冷笑话，谁能告诉我答案：为什么蜗牛走得那么慢？",
        "讲个冷笑话，谁能告诉我答案：为什么鸭子不会打电话？",
        "讲个冷笑话，谁能告诉我答案：为什么狮子不会做饭？",
        "讲个冷笑话，谁能告诉我答案：为什么乌龟不参加马拉松比赛？",
        "讲个冷笑话，谁能告诉我答案：为什么猫不穿鞋子？",
        "讲个冷笑话，谁能告诉我答案：为什么鸟不在电线上玩滑翔伞？",
        "讲个冷笑话，谁能告诉我答案：为什么老鼠不去看牙医？",
        "讲个冷笑话，谁能告诉我答案：为什么书从来不生病？",
        "讲个冷笑话，谁能告诉我答案：为什么冰箱里的菜总是那么凉快？",
        "讲个冷笑话，谁能告诉我答案：为什么蚂蚁永远不会生气？",
        "讲个冷笑话，谁能告诉我答案：为什么熊猫是黑白的？",
        "讲个冷笑话，谁能告诉我答案：为什么蜜蜂会变胖？",
        "讲个冷笑话，谁能告诉我答案：为什么蜡烛会哭泣？",
        "讲个冷笑话，谁能告诉我答案：为什么鱼儿在水里睡觉？",
        "讲个冷笑话，谁能告诉我答案：为什么花儿总是那么香？",
        "讲个冷笑话，谁能告诉我答案：为什么兔子的眼睛那么红？",
        "讲个冷笑话，谁能告诉我答案：为什么牛吃草？",
        "讲个冷笑话，谁能告诉我答案：为什么蝴蝶总是那么美？",
        "讲个冷笑话，谁能告诉我答案：为什么狗喜欢摇尾巴？",
        "讲个冷笑话，谁能告诉我答案：为什么鸡会过马路？",
        "讲个冷笑话，谁能告诉我答案：为什么鸽子这么和平？",
        "讲个冷笑话，谁能告诉我答案：为什么老虎有条纹？",
        "讲个冷笑话，谁能告诉我答案：为什么猴子喜欢爬树？",
        "讲个冷笑话，谁能告诉我答案：为什么鹿能跑得那么快？",
        "讲个冷笑话，谁能告诉我答案：为什么蛇会脱皮？",
        "讲个冷笑话，谁能告诉我答案：为什么马喜欢吃草？",
        "讲个冷笑话，谁能告诉我答案：为什么熊会冬眠？",
        "讲个冷笑话，谁能告诉我答案：为什么狼会嚎叫？",
        "讲个冷笑话，谁能告诉我答案：为什么鹅会看家？",
        "讲个冷笑话，谁能告诉我答案：为什么鸭子会游泳？",
        "讲个冷笑话，谁能告诉我答案：为什么乌龟能活那么久？",
        "讲个冷笑话，谁能告诉我答案：为什么老鼠那么小？",
        "讲个冷笑话，谁能告诉我答案：为什么猫喜欢吃鱼？",
        "讲个冷笑话，谁能告诉我答案：为什么狗喜欢吃肉？",
        "讲个冷笑话，谁能告诉我答案：为什么鸟会飞？",
        "讲个冷笑话，谁能告诉我答案：为什么鱼会游泳？",
        "讲个冷笑话，谁能告诉我答案：为什么螃蟹横着走？",
        "讲个冷笑话，谁能告诉我答案：为什么虾米那么红？",
        "讲个冷笑话，谁能告诉我答案：为什么蚂蚁那么小？",
        "讲个冷笑话，谁能告诉我答案：为什么蜜蜂会变瘦？",
        "讲个冷笑话，谁能告诉我答案：为什么蝴蝶会变胖？",
        "讲个冷笑话，谁能告诉我答案：为什么狗会汪汪叫？",
        "讲个冷笑话，谁能告诉我答案：为什么鸡会咯咯叫？",
        "讲个冷笑话，谁能告诉我答案：为什么猪会呼呼睡？",
        "讲个冷笑话，谁能告诉我答案：为什么鹿会跳跳走？",
        "讲个冷笑话，谁能告诉我答案：为什么蛇会嘶嘶叫？",
        "讲个冷笑话，谁能告诉我答案：为什么马会踢踢脚？",
        "讲个冷笑话，谁能告诉我答案：为什么熊会咆哮？",
        "讲个冷笑话，谁能告诉我答案：为什么狼会咬咬人？",
        "讲个冷笑话，谁能告诉我答案：为什么鹅会嘎嘎叫？",
        "讲个冷笑话，谁能告诉我答案：为什么鸭子会嘎嘎叫？",
        "讲个冷笑话，谁能告诉我答案：为什么乌龟会慢慢爬？",
        "讲个冷笑话，谁能告诉我答案：为什么老鼠会吱吱叫？",
        "讲个冷笑话，谁能告诉我答案：为什么猫会喵喵叫？",
        "讲个冷笑话，谁能告诉我答案：为什么狗会旺旺叫？",
        "讲个冷笑话，谁能告诉我答案：为什么鸟会叽叽喳喳？",
        "讲个冷笑话，谁能告诉我答案：为什么鱼会咕噜咕噜？",
        "讲个冷笑话，谁能告诉我答案：为什么螃蟹会咔咔响？",
        "讲个冷笑话，谁能告诉我答案：为什么蚂蚁会排排队？",
        "讲个冷笑话，谁能告诉我答案：为什么蜜蜂会嗡嗡叫？",
        "讲个冷笑话，谁能告诉我答案：为什么蝴蝶会翩翩起舞？",
        "讲个冷笑话，谁能告诉我答案：为什么狗会追追风？",
        "讲个冷笑话，谁能告诉我答案：为什么鸡会啄啄地？",
        "讲个冷笑话，谁能告诉我答案：为什么猪会滚滚泥？",
        "讲个冷笑话，谁能告诉我答案：为什么鹿会喝喝水？",
        "讲个冷笑话，谁能告诉我答案：为什么蛇会吐吐舌头？",
        "讲个冷笑话，谁能告诉我答案：为什么马会踏踏地？",
        "讲个冷笑话，谁能告诉我答案：为什么熊会爬爬树？",
        "讲个冷笑话，谁能告诉我答案：为什么狼会找找食？",
        "讲个冷笑话，谁能告诉我答案：为什么鹅会游游泳？",
        "讲个冷笑话，谁能告诉我答案：为什么鸭子会嘎嘎笑？",
        "讲个冷笑话，谁能告诉我答案：为什么乌龟会缩缩头？",
        "讲个冷笑话，谁能告诉我答案：为什么老鼠会钻钻洞？",
        "讲个冷笑话，谁能告诉我答案：为什么猫会抓抓鼠？",
        "讲个冷笑话，谁能告诉我答案：为什么狗会汪汪吠？",
        "讲个冷笑话，谁能告诉我答案：为什么鸟会飞飞天？",
        "讲个冷笑话，谁能告诉我答案：为什么鱼会游游水？",
        "讲个冷笑话，谁能告诉我答案：为什么螃蟹会夹夹手？",
        "讲个冷笑话，谁能告诉我答案：为什么虾米会弹弹跳？",
        "讲个冷笑话，谁能告诉我答案：为什么蚂蚁会搬搬家？",
        "讲个冷笑话，谁能告诉我答案：为什么蜜蜂会采采蜜？",
        "讲个冷笑话，谁能告诉我答案：为什么蝴蝶会停停花？",
        "讲个冷笑话，谁能告诉我答案：为什么狗会闻闻味？",
        "讲个冷笑话，谁能告诉我答案：为什么鸡会下下蛋？",
        "讲个冷笑话，谁能告诉我答案：为什么猪会睡睡觉？",
        "讲个冷笑话，谁能告诉我答案：为什么鹿会看看路？",
        "讲个冷笑话，谁能告诉我答案：为什么蛇会躲躲藏？",
        "讲个冷笑话，谁能告诉我答案：为什么马会跑跑步？",
        "讲个冷笑话，谁能告诉我答案：为什么熊会找找蜂？",
    ]

    random_num = random.randint(0, 99)
    action.input(dongtai_huashu[random_num])
    print("已经编辑好话术")
    time.sleep(10)

    print("10秒后发送动态")
    time.sleep(10)
    Selector().type("TextView").text("发布").id(
        "com.immomo.momo:id/tv_send_txt"
    ).parent(1).click().find()

    print("动态已发送")


## ---------------------------------------------------进入群组发信息----------------------------------------------------------------------------


def group_faxinxi():
    ## 点击进入去看看
    print("正在点击去看看")
    time.sleep(3)
    Selector().path(
        "/FrameLayout/RecyclerView/FrameLayout/RecyclerView/FrameLayout/TextView"
    ).type("TextView").text("我的群组").parent(1).click().find_all()

    ## 进入群组
    # time.sleep(10)
    print("正在检索所有群组，十秒后执行下一步操作")
    num_gengduo = 10  # 10
    for i_num in range(num_gengduo):
        print("-", end="", flush=True)
        time.sleep(1)
    ######群组控件位置
    group_my = (
        Selector()
        .text("群组")
        .type("TextView")
        .path("/FrameLayout/ViewPager/ListView/LinearLayout/TextView")
        .parent(1)
        .brother(3)
        .find_all()
    )
    # print(group_my)

    def input_xinxi():

        # -----点击输入框消息---------
        time.sleep(5)
        Selector().path("/FrameLayout/LinearLayout/EditText").type("EditText").text(
            "请输入消息..."
        ).click().find_all()

        # -------输入信息-----------
        group_huashu = [
            "大家好",
            "都在干嘛呢",
            "见到你们很开心",
            "都有对象嘛",
            "cpdd",
            "想找个对象",
            "你们好呀，我比较内向",
            "想交个朋友",
            "哈哈",
            "想要花花",
            "谁是我的小可爱",
            "我喜欢喝可乐",
            "交个朋友吧",
            "好无聊啊",
            "今天都不知道要干嘛",
        ]
        time.sleep(3)
        random_group = random.randint(0, 14)
        action.input(group_huashu[random_group])
        print("已经编辑好话术,三秒后发送")

        # ---------点击发送---------
        time.sleep(3)
        Selector().path("/FrameLayout/LinearLayout/Button").type("Button").text(
            "发送"
        ).click().find_all()
        print("已经发送信息，十秒后返回")
        # ----------返回-------------
        time.sleep(5)
        action.Key.back()
        time.sleep(5)
        action.Key.back()

    ###----判断 group 是否是none type 对象 如果是 则退出群组--------------
    if isinstance(group_my, type(None)):
        print("当前未加入群组，5秒后退出")
        num_gengduo = 5  # 10
        for i_num in range(num_gengduo):
            print("-", end="", flush=True)
            time.sleep(1)
        Selector().text("附近群组").type("TextView").path(
            "/FrameLayout/TextView"
        ).brother(1).click().find_all()
    else:
        ###--------如果不是nonetype 对象说明是list 对象 那么 轮流打开群组 并且执行函数 input_xinxi --------------
        l_group_my = len(group_my)
        i_group_my = 0
        print("当前加入群组", l_group_my, "个")
        while i_group_my < l_group_my:
            time.sleep(3)
            group_my[i_group_my].click()
            input_xinxi()
            i_group_my += 1

        print("5秒后退出群组")
        num_gengduo = 5  # 10
        for i_num in range(num_gengduo):
            print("-", end="", flush=True)
            time.sleep(1)
        ##点击退出群组
        Selector().text("群组").type("TextView").brother(1).click().find_all()


#########################自动回复粉丝关注----------------------------------------------------
def fensihuiguan():
    print(randint_time_num1, "秒后进入粉丝组")
    num_fensi_group = randint_time_num1  # 10
    for i_num in range(num_fensi_group):
        print("-", end="", flush=True)
        time.sleep(1)

    ##点击进入粉丝群组
    Selector().text("粉丝").type("TextView").parent(1).click().find_all()
    print("十秒后自动关注")
    num_fensi_huiguan = 10  # 10
    for i_num in range(num_fensi_huiguan):
        print("-", end="", flush=True)
        time.sleep(1)

    ##点击回关
    list_not_huiguan = (
        Selector()
        .text("回关")
        .type("TextView")
        .clickable(True)
        .checkable(False)
        .checked(False)
        .editable(False)
        .find_all()
    )
    fensi_group_huadong = 0
    while fensi_group_huadong < 3:

        if isinstance(list_not_huiguan, type(None)):
            print("当前页无未关注，执行滑动")
            action.swipe(461, 1851, 487, 702, 3000)

        else:
            print("十秒后之执行关注")
            num_fensi_group = 10  # 10
            for i_num in range(num_fensi_group):
                print("-", end="", flush=True)
                time.sleep(1)

            i2_fensihuiguan = 0
            l_list_not_huiguan = len(list_not_huiguan)
            while i2_fensihuiguan < l_list_not_huiguan:

                list_not_huiguan[i2_fensihuiguan].click()
                action.swipe(461, 1851, 487, 702, 3000)
                i2_fensihuiguan += 1
        fensi_group_huadong += 1
    else:
        print("操作执行完毕，十秒后退出")
        num_fensi_group = 10  # 10
        for i_num in range(num_fensi_group):
            print("-", end="", flush=True)
            time.sleep(1)
        action.Key.back()

def into_xiangqi():
        print("十秒后进入象棋")
        num_fensi_group = 10  # 10
        for i_num in range(num_fensi_group):
            print("-", end="", flush=True)
            time.sleep(1)
        # 下滑
        action.swipe(461, 1851, 487, 702, 3000)
        time.sleep(5)
        # 点击游戏
        Selector().text("斗地主").type("TextView").parent(1).click().find()
        # 点击象棋
        time.sleep(10)
        path = R.res("/img/1.png")
        res = FindImages.find(path,confidence= 0.95)
        print(res)
        # 计算点击坐标
        rect_list = res['rect']
        rect_x = rect_list[0]
        rect_y = rect_list[1]
        rect_x1 = rect_list[2]
        rect_y1 = rect_list[3]
        click_x = (rect_x + rect_x1)/2
        click_y = (rect_y + rect_y1)/2
        action.click(click_x,click_y)

        # #创建一个房间
        print("等待十秒开始创建")
        time.sleep(10)
        path1 = R.res("/img/2.png")
        res1 = FindImages.find_sift(path1,confidence= 0.95)
        print(res1)
        # 计算点击坐标
        rect_list1 = res1['rect']
        rect_x_1 = rect_list1[0]
        rect_y_1 = rect_list1[1]
        rect_x1_1 = rect_list1[2]
        rect_y1_1 = rect_list1[3]
        click_x_1 = (rect_x_1 + rect_x1_1)/2
        click_y_1 = (rect_y_1 + rect_y1_1)/2
        action.click(click_x_1,click_y_1)

        #点击创建
        print("等待十秒创建房间")
        num_fensi_group = 10  # 10
        for i_num in range(num_fensi_group):
            print("-", end="", flush=True)
            time.sleep(1)
        # 文字识别创建 ，点击创建        
        Ots = Ocr.paddleocr_v2(rect =[57,506,1038,1837],pattern = '创建')
        if Ots:
            random_ot = random.choice(Ots)
            time.sleep(3)
            action.click(random_ot.x,random_ot.y)
            #每五十秒执行一次循环，一个小时之后跳出循环
            start_time = time.time()
            counter = 0
            while True:
                current_time = time.time()
                if current_time - start_time >= 3600:  # 一个小时后退出循环
                    break
                if counter < 72:  # 在一个小时内只执行72次循环
                    Ots1 = Ocr.paddleocr_v2(rect =[20,330,1064,1603],pattern = '准备')
                    if Ots1:
                        for oc1 in Ots1:
                            time.sleep(3)
                            action.click(oc1.x,oc1.y)
                    else:
                        print("已经准备")
                    counter += 1
                else:
                    break
                time.sleep(50)  # 每50秒执行一次循环
            #退出游戏房间
            path3 = R.res("/img/3.png")
            res3 = FindImages.find_all_template(path2,confidence= 0.95)
            print(res3)
            # 点击x计算点击坐标
            rect_list3 = res3['rect']
            rect_x_3 = rect_list3[0]
            rect_y_3 = rect_list3[1]
            rect_x1_3 = rect_list3[2]
            rect_y1_3 = rect_list3[3]
            click_x_3 = (rect_x_3 + rect_x1_3)/2
            click_y_3 = (rect_y_3 + rect_y1_3)/2
            action.click(click_x_3,click_y_3)

            #确定退出
            path4 = R.res("/img/4.png")
            res4 = FindImages.find_all_template(path4,rect= [707,1320,810,1377] ,confidence= 0.95)
            print(res4)
            # 计算点击坐标
            rect_list4 = res4['rect']
            rect_x_4 = rect_list4[0]
            rect_y_4 = rect_list4[1]
            rect_x1_4 = rect_list4[2]
            rect_y1_4 = rect_list4[3]
            click_x_4 = (rect_x_4 + rect_x1_4)/2
            click_y_4 = (rect_y_4 + rect_y1_4)/2
            action.click(click_x_4,click_y_4)

            ###退出到我的主页
            print("等待十秒退回主页")
            time.sleep(5)
            action.key.back()
            time.sleep(5)
            action.key.back()

            
            

        else:
            print("无创建按钮")
            print("等待十秒退回主页")
            time.sleep(5)
            action.key.back()
            time.sleep(5)
            action.key.back()




        ######留存，随机进入房间
        # Ots = Ocr.paddleocr_v2(rect =[36,257,1043,1721],confidence = 0.5,pattern = '象棋')
        # print("等待十秒进入房间")
        # time.sleep(10)
        # print(Ots)
        # print(type(Ots))
        # if Ots:
        #     random_ot = random.choice(Ots)
        #     time.sleep(3)
        #     action.click(random_ot.x,random_ot.y)




        #     action.Key.back()
        #     time.sleep(3)
        #     action.Key.back()

        # else:
        #     print("无房间,等待五秒退出")

        





###########################################-------------------返回，进入直播间------------------------###########################################
# 代码暂时搁置，留存下一次更新               #
###########################################


def kanzhibo():

    # 点击直播
    print("5秒后点击直播")
    num_gengduo = 5  # 10
    for i_num in range(num_gengduo):
        print("-", end="", flush=True)
        time.sleep(1)
    Selector().path("/FrameLayout/FrameLayout/TextView").type("TextView").text(
        "直播"
    ).id("com.immomo.momo:id/tab_item_tv_label").parent(1).click().find()

    print("等待十秒判断是否有广告")
    num_gengduo = 10  # 10
    for i_num in range(num_gengduo):
        print("-", end="", flush=True)
        time.sleep(1)

    ###----------判断是否有广告，如果有则关闭，如果没有则继续------------------
    ad_skips1 = (
        Selector()
        .text("知道了")
        .type("View")
        .path("/FrameLayout/WebView/WebView/View/View/View")
        .click()
        .find()
    )

    ad_skips2 = (
        Selector()
        .text("再想想")
        .type("TextView")
        .path("/FrameLayout/TextView")
        .find_all()
    )
    ###--------判断广告1---------------
    if isinstance(ad_skips1, type(None)):
        print("无广告1")

        ###-------判断广告2---------------
        if isinstance(ad_skips2, type(None)):
            print("无广告2")
        else:
            ad_skips2[0].click()

        print("5秒后打开直播")
        num_gengduo = 5  # 10
        for i_num in range(num_gengduo):
            print("-", end="", flush=True)
            time.sleep(1)
        ##随机打开直播
        open_zhibo = (
            Selector()
            .path("/FrameLayout/ViewPager/RelativeLayout/RecyclerView/RelativeLayout")
            .type("RelativeLayout")
            .id("com.immomo.momo:id/live_center_layout")
            .find_all()
        )
        l_open_zhibo = len(open_zhibo)
        random_zhibo_num = random.randint(0, l_open_zhibo - 1)
        open_zhibo[random_zhibo_num].click()

    else:
        time.sleep(5)
        ad_skips1[0].click()

        ###-------判断广告2---------------
        if isinstance(ad_skips2, type(None)):
            print("无广告2")
        else:
            ad_skips2[0].click()
        print("5秒后打开直播")

        num_gengduo = 5  # 10
        for i_num in range(num_gengduo):
            print("-", end="", flush=True)
            time.sleep(1)
        ##随机打开直播
        open_zhibo = (
            Selector()
            .path("/FrameLayout/ViewPager/RelativeLayout/RecyclerView/RelativeLayout")
            .type("RelativeLayout")
            .id("com.immomo.momo:id/live_center_layout")
            .find_all()
        )
        l_open_zhibo = len(open_zhibo)
        random_zhibo_num = random.randint(0, l_open_zhibo - 1)
        open_zhibo[random_zhibo_num].click()

    ## 关闭广告

    ## 打开下一个直播
    i_zhibo = 0
    while i_zhibo < 5:
        time.sleep(5)
        print("正在观看直播，两分钟后滑动到下一个")
        num_gengduo = 30  # 10          ###################  直播浏览时间
        for i_num in range(num_gengduo):
            print("-", end="", flush=True)
            time.sleep(1)

        ###判断直播广告 、关闭按钮
        liwu_ad = (
            Selector()
            .text("陌陌直播")
            .type("WebView")
            .visible(True)
            .focused(True)
            .focusable(True)
            .find_all()
        )

        close_zhibo_ad = (
            Selector()
            .text("陌陌直播")
            .type("WebView")
            .child(1)
            .child(1)
            .child(1)
            .child(1)
            .brother(2)
            .find_all()
        )
        close_zhibo_ad_fangqi = (
            Selector()
            .text("放弃")
            .type("View")
            .clickable(True)
            .checkable(False)
            .checked(False)
            .editable(False)
            .find_all()
        )

        zhubopaipai = (
            Selector()
            .text("普通回拍限时免费")
            .type("Button")
            .focusable(True)
            .visible(True)
            .find_all()
        )

        rengrantuichu = (
            Selector()
            .text("仍然退出")
            .type("TextView")
            .click()
            .visible(True)
            .focusable(True)
            .find_all()
        )

        huluefuchuang = (
            Selector()
            .text("忽略")
            .type("Button")
            .clickable(True)
            .checkable(False)
            .checked(False)
            .editable(False)
            .longClickable(False)
            .focusable(True)
            .focused(False)
            .find_all()
        )

        if isinstance(liwu_ad, type(None)):
            print("无礼物广告")

            if isinstance(close_zhibo_ad, type(None)):
                print("无连带键，无需退出")

                if isinstance(zhubopaipai, type(None)):
                    print("无拍拍无需回拍")

                else:
                    zhubopaipai[0].click()
            else:
                close_zhibo_ad[0].click()
                time.sleep(2)
                close_zhibo_ad_fangqi[0].click()
                if isinstance(zhubopaipai, type(None)):
                    print("无拍拍无需回拍")

                else:
                    zhubopaipai[0].click()

        else:
            action.Key.back()

            if isinstance(close_zhibo_ad, type(None)):
                print("无连带键，无需退出")

                if isinstance(zhubopaipai, type(None)):
                    print("无拍拍无需回拍")

                else:
                    zhubopaipai[0].click()
            else:
                close_zhibo_ad[0].click()
                time.sleep(2)
                close_zhibo_ad_fangqi[0].click()

                if isinstance(zhubopaipai, type(None)):
                    print("无拍拍无需回拍")
                else:

                    zhubopaipai[0].click()

        close_zhibo = (
            Selector()
            .id("com.immomo.momo:id/phone_live_iv_quit")
            .type("ImageView")
            .path("/FrameLayout/ImageView")
            .click()
            .find_all()
        )

        if isinstance(close_zhibo, type(None)):
            print("无关闭对象,执行下一步")
        else:
            close_zhibo[0].click()
            if isinstance(rengrantuichu, type(None)):
                print("直接退出")
            else:
                print("正在退出")
                rengrantuichu[0].click()
                print("已经退出")
        if isinstance(huluefuchuang, type(None)):
            print("无忽略弹窗")
        else:
            huluefuchuang[0].click()

        print("等待五秒打开下一个直播")
        num_gengduo = 5  # 10
        for i_num in range(num_gengduo):
            print("-", end="", flush=True)
            time.sleep(1)
        random_zhibo_num_1 = random.randint(0, l_open_zhibo - 1)
        open_zhibo[random_zhibo_num_1].click()
        i_zhibo += 1
        print("第", i_zhibo, "次滑动，共计五次")
    else:
        print("直播浏览完成")

    ## 退出直播后再随机打开一个直播
