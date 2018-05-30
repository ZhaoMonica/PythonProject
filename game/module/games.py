#coding:utf-8
"""
游戏主程序,开始游戏KO模式
start()方法开始进行游戏
print_status()方法显示生命值状态信息
"""
# games.py 游戏：启动游戏->选主角色，选择出招，显示角色状态
import random
import time
from game.module import common
from game.module.people import Role
from game.files import attack_talk

def print_status(currobj, otherobj, attack_status):
    """
    根据攻击的结果输出生命值信息
    :param currobj:当前选中角色对象
    :param otherobj:对方角色
    :param attack_status:攻击的状态，True(攻击成功) False(攻击失败）
    :return:
    """
    # 显示对话
    if attack_status == True:
        slice = random.sample(attack_talk.attack_succ_msg, 1)
        time.sleep(0.8)
        currobj.talk(slice, currobj.types)
        #print(currobj._name, currobj._status, slice )
    else:
        slice1 = random.sample(attack_talk.attack_fail_msg, 1)
        #print(otherobj._name, otherobj._status , slice1)
        time.sleep(0.8)
        otherobj.talk(str(slice1), otherobj.types)
        time.sleep(0.8)
    #print('【', currobj._name , '】' , '生命值：',currobj._blood ,',【' ,otherobj._name,'】','生命值：',otherobj._blood)
    print("\033[46;1m【{curr}】生命值{life1}，【{other}】 生命值：{life2}\033[0m".format(curr= currobj._name ,
                                                                             life1=currobj._blood ,
                                                                             other=otherobj._name,
                                                                             life2=otherobj._blood))
def start():

    # print("请选择游戏角色，1-> 狄仁杰  2->李元芳  3->退出：")
    # 从配置文件获取角色信息
    # 实例化两个角色对象
    direnjie = Role(**(common.load_info('direnjie')))  # 传可变参数要加两个**
    liyuanfang = Role(**(common.load_info('liyuanfang')))
   # print(direnjie)
    flag = False
    while not flag:
        print("请选择角色：")
        #根据用户选择一个主角色
        choose = int(input("1-> 狄仁杰  2->李元芳  3->退出："))
        # print_status(currobj, otherobj, attack_status)
        if choose == 1:

            direnjie.is_main
            currobj = direnjie
            otherobj = liyuanfang
            currobj.types = 'L'
            otherobj.types = 'R'
            exit_flag = False
        if choose == 2:
             liyuanfang.is_main
             currobj = liyuanfang
             otherobj = direnjie
             currobj.types = 'L'
             otherobj.types = 'R'
             exit_flag = False
        if choose == 3:
            print('已退出游戏！')
            exit()
        if choose not in [1,2,3]:
            print("请重新选择英雄")
            continue
        flag = True

    liyuanfang.talk("大人，今天我又抓住了3个罪犯！",'L')
    time.sleep(0.8)
    direnjie.talk("那你就跟着他，看看他三入长安究竟是做什么。",'L')
    time.sleep(0.8)
    liyuanfang.talk("不是吧大人！那...狄大人，下个月的工资评定请对我温柔一点吧？！",'L')
    time.sleep(0.8)
    direnjie.talk("想评优先过了我这关吧，出招，让我看看你的能耐把！",'L')
    time.sleep(0.8)



    while not exit_flag:
    #主角色选择攻击招式
        shengmingzhi = currobj.choose_skill()

    #对手接招
        if otherobj.jiezhao(shengmingzhi, random.randint(0, 4)) == True:
            attack_status = True
            print_status(currobj, otherobj, attack_status)
        else:
            attack_status = False
            print_status(currobj, otherobj, attack_status)
        #time.sleep(1)

    #判断对手是否被干掉
        #print(otherobj.is_alive)
        if otherobj.is_alive == True:
        # 对手发招(自动)
            blool = otherobj.auto_skill()
        # 主角色接招
            currobj.jiezhao(blool, random.randint(0, 4))
        # 主角色活着吗?
            if currobj.is_alive == True:
                exit_flag == False
            else:
                 print("\033[1;31;0m \nGAME OVER You lost！\033[0m")
                 #print('Game over，You lost！！')
                 break
        else:
            print("\033[1;31;0m \nGAME OVER You win！\033[0m")
            #print('Game over,You win！！')
            break
