#coding:utf-8
"""
角色类模块
"""

import json
import time
import random
# 个人角色信息，接招，出招，与另一角色对话，主角色，非主角色，生存状态
class Role(object):

    def __init__(self, **kwargs):
        self._x = True
        self._name = kwargs['name']
        self._blood = kwargs['blood']
        # self._status = ["大吼一声",大叫一声 ]
        self._status = "大吼一声"
        self._kongfu = list(json.loads(kwargs["kongfu"]).keys())
        self._kongfuzhi = list(json.loads(kwargs["kongfu"]).values())
        # self._kongfu = eval(kwargs['kongfu'])
        #self._skills = eval(kwargs['skills'])


        # {1: '谍影重重', 2: '无间锋刃',3: '刃遁', 4: '凝神归元',5: '退出'}
        #self._is_live = True

        """
        构造函数,传入参数为一个字典
        :param kwargs:用户信息字典
        :return:
        """
    # 不需要初始化
    def jiezhao(self, blood, rnum):
        """
        接招函数，如果数字命中则减血,否则为命中
        :param blood: 命中后扣的生命值
        :param rnum: 随机数，如果随机数==1则命中
        :return: 是否命中
        """

        if rnum == 1:
            self._blood = int(self._blood) - blood
            if 180 < self._blood <= 200:
                self._status = "大吼一声"
            if 100 < self._blood <= 180:
                self._status = '大叫一声'
            if 50 < self._blood<= 100:
                self._status = '气血不足'
            if 0 < self._blood <= 50:
                self._status = '奄奄一息'
           # print(self._name)
            print("\033[31;1m {name}躲闪不急,被刺中一刀!\033[0m".format(name=self._name))
            return True
        else:
            print("\033[33;1m {name}一个闪现,躲过了一劫。\033[0m".format(name=self._name))
            return False

            # blood = int(self.blood)

			#


    def talk(self, talkmsg, types):
        """
        对白说函数
        :param types: 显示的类型, L 左边显示 R： 右边显示
        :param talkmsg:说的内容
        :return: 返回完整对话信息
        """


        # if types == 'L':
        #     time.sleep(0.8)
        #     print(self._name ,'【', self._status ,'】',talkmsg)
        # elif types == 'R':
        #     time.sleep(0.8)
        #     print(talkmsg.rjust(70) + self._name,'【', self._status ,'】' )

        show_msg = "{user}[{status}]: {msg} ".format(user=self._name,
                                                     status=self._status,
                                                     msg= talkmsg)
        if types == "L":
            print(("\033[1;31m{0}\033[0m;".format(show_msg)).ljust(150, ' '))
        if types == "R":
            print(("\033[1;30m{0}\033[0m;".format(show_msg)).rjust(100, ' '))
        time.sleep(1)


    def choose_skill(self):
        """
        选择技能、返回技能的攻击值
        :return: 技能攻击值
        """
        print('(', self._name, ')', end='')

        if self.is_main == True:
            time.sleep(0.8)
            skill = int(input("\033[33;1m({4})请选择招式[ 1:{0}, 2:{1},3:{2},4:{3}，5：退出]:\033[0m".format(self._kongfu[0],
                                                                                                    self._kongfu[1],
                                                                                                    self._kongfu[2],
                                                                                                    self._kongfu[3],
                                                                                                    self._name)))

            # print("请选择招式","[1:",self._kongfu[0]," 2:",self._kongfu[1],"3:",self._kongfu[2],"4:",self._kongfu[3]," 5:退出]:",end= '')
           # skill = int(input())
            if skill == 1:
                return self._kongfuzhi[0]
            elif skill == 2:
                return self._kongfuzhi[1]
            elif skill == 3:
                return self._kongfuzhi[2]
            elif skill == 4:
                return self._kongfuzhi[3]
            elif skill == 5:
                print('退出游戏！')
                exit()
        # elif self._name == 'liyuanfang':
        #     skill = int(input("请选择招式[1:谍影重重 2:无间锋刃 3:刃遁 4:凝神归元 5:退出]:"))
        #     if skill == 1:
        #         return 50
        #     elif skill == 2:
        #         return 60
        #     elif skill == 3:
        #         return 45
        #     elif skill == 4:
        #         return 50
        #     elif skill == 5:
        #         exit()




    @property
    def is_main(self):
        """
        设置角色为主角色属性，设置后主角色的对话信息显示在左边
        :return:
        """
        # return self.types == 'L'
        return self._x

    def auto_skill(self):
        """
        设置主角色后的另一个角色将采用自动获取招式并攻击，此模块用来随机获取招式
        :return: 返回招式的攻击值
        """
        #list = ['迅捷', '逃脱', '无间锋刃', '王朝密令']
        # zip1 = zip(self._kongfu, self._kongfuzhi)
        num1 = random.randint(0, 3)
        time.sleep(0.8)
        print(("\n\033[1;34m 看招! {0} 发起一个 【{1}】 大招!\033[0m;".format(self._name, self._kongfu[num1])).rjust(100, ' '))
        # print(self._name, '发起了 【', self._kongfu[num1], '】的大招！')
        return self._kongfuzhi[num1]

    @property
    def is_alive(self):
        """
        判断角色对象是否还有生命值。
        :return: 角色对象的blood值小于等于0 表示角色完蛋了,返回False，否则返回True
        """
        if int(self._blood) <= 0:
            return False
        else:
            return True

