# __init__.py 为初始化加载文件

# 导入系统资源模块
from ascript.android.system import R

# 导入动作模块
from ascript.android import action

# 导入节点检索模块
from ascript.android import node

# 导入图色检索模块
from ascript.android import screen
from .hanshu import *

shaixuanfujin()

time.sleep(3)

head_i = 0
while head_i < 50:
    dianjitouxiang()
    time.sleep(3)
    action.swipe(423, 1924, 482, 804, 3000)
    head_i += 1
