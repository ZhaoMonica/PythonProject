# coding:utf-8
"""
主程序文件,选择菜单
"""
from game.conf import setting
from game.conf import templates
from game.module import games
from game.module import common
import sys

if __name__ == '__main__':
    print(templates.GAME_MENU)
    exit_flags = False  #退出标志
    while not exit_flags:
        func = int(input("请选择功能编号：[1-4]"))
        if func not in (1 , 2, 3, 4):
            print('重新选择')
            continue

        if func == 4:
            exit_flags = True
            continue

        if func == 1:
            print(templates.GAME_TITLE.format(currole = "",appoment= ""))
            common.load_begin()

        if func == 2:

            #print(templates.ROLE_INFO)  # 怎么用？
            #dir_di = common.load_info("direnjie")# name_dict:角色信息字典,如dir_di;dir_li是一个字典
            #di = common.format_info(dir_di)
            #print(di)
            # 参数不一致怎么处理？
            dir_li = common.load_info("liyuanfang")  # name_dict:角色信息字典,如dir_di;dir_li是一个字典
            #li = common.format_info(dir_li)
            #print(templates.ROLE_INFO.format(di=di_str, li=li_str))

            di_str = common.format_info(common.load_info("direnjie"))
            li_str = common.format_info(common.load_info("liyuanfang"))
            #嵌入模版
            print(templates.ROLE_INFO.format(di=di_str, li=li_str))
            #print(li)
            # for k in dir_di:
            #     print(k.keys, k.values)
            # dir_li = common.load_info("liyuanfang")
            # print(templates.ROLE_INFO.format(currole="dir_li", appoment=""))

        if func == 3:
            games.start()





