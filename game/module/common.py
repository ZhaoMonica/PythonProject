#coding:utf-8
"""
公共类模块
"""
import os
import json
import time
import xml.etree.ElementTree as ET
from game.conf import setting

def load_info(uname):
    """
    根据输入名字获取用户的基本信息
    :param uname: 用户名，必须和xml中的key一样
    :return:
    """
    users = setting.ROLE_FILE
    _return_dict = {}
    #打开xml文档
    fobj = ET.parse(users)
    # 获得root节点
    root = fobj.getroot()
    for child in root:
        if child.tag == "user" and child.attrib["key"] == uname:
            for elements in child:
                _return_dict[elements.tag] = elements.text

    return _return_dict

def load_begin():
    """
    打印游戏的背景，从文件中逐行读取文件并打印
    :return:
    """
    # with open('/files/drama', 'r', encoding='utf-8') as f:
    #     for eachline in f:
    #     # print(eachline)
    #       f.readlines()
    with open(r'D:\Game\game\files\drama', 'r', encoding='utf-8') as f:
        for i in f:
            print(i)
            time.sleep(0.5)


def format_info(name_dict):
    """
    将从xml中获取的角色字典信息格式化为str类型，用于填充人物介绍模板
    :param name_dict:角色信息字典
    :return:填充完的模板数据
    """
    information = """
                姓名：{name}
                职称：{alias}
                血量：{blood}
                蓝条：{bluebuff}
                武器：{sword}
                简介：{introduce}
                功夫：{kongfu}
                """
    info = information.format(name = name_dict['name'],
                       alias = name_dict['alias'],
                       blood = name_dict['blood'],
                       bluebuff = name_dict['bluebuff'],
                       sword = name_dict['sword'],
                       introduce = name_dict['introduce'],
                       kongfu = ",".join(list(json.loads(name_dict["kongfu"]).keys())))
    return info

#     '{0:''>10}'.format(10)  ##右对齐
#     jsoninfo = json.dumps(name_dict)  # 输出str类型
#     print(jsoninfo)
# # load_info("direnjie")