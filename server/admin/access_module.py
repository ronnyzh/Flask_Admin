#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
Project: Flask_test
Filename: access_module.py
Author: ronnyzh
Date: 2020-03-04 12:43
Revision: $Revision$
Description: $Description$
"""

from define.define_consts import *
from public.public_func import getLang


class AccessObj(object):
    def __init__(self, tree, method, field, check=False):
        self.tree = tree
        self.method = method
        if method in ('GET', 'POST'):
            self.url = BACK_PRE + '/' + '/'.join(tree)
            self.accessTag = '%s:' % (method) + self.url
        else:
            self.url = BACK_PRE + '/' + str(tree)
            self.accessTag = ''
        self.field = field
        self.check = check

    def getTxt(self, lang):
        return getattr(lang, self.field)


#  总菜单权限  #
MENU_MODULES = (
    # 主菜单
    AccessObj(("menu"), None, 'MENU_PRIMARY_TXT', True),

    # 系统设置：支付设置、大厅更新设置
    AccessObj(("sys"), None, 'MENU_SYS_TXT'),
    AccessObj(("setting", "system"), 'GET', 'MENU_GAME_PAY_LIST_TXT'),
    AccessObj(("setting", "hotUpDateSetting"), 'GET', 'MENU_HOT_UPDATE_LIST_TXT'),

    # 游戏管理：游戏列表、广播列表
    AccessObj(("game"), None, 'MENU_GAME_TXT'),
    AccessObj(("game", "list"), 'GET', 'MENU_GAME_LIST_TXT'),
    AccessObj(("game", "broadList?broad_belone=HALL"), 'GET', 'MENU_GAME_BROAD_LIST_TXT'),

    # 信息公告管理：系统公告列表、广告列表
    AccessObj(("notic"), None, 'MENU_NOTIC_TXT'),
    AccessObj(("notic", "list"), 'GET', 'MENU_NOTIC_LIST_TXT'),
    AccessObj(("notic", "ad"), 'GET', 'MENU_NOTIC_AD_TXT'),

    # 商品管理：商品列表
    AccessObj(("goods"), None, 'MENU_GOODS_TXT'),
    AccessObj(("goods", "list"), 'GET', 'MENU_GOODS_LIST_TXT'),

    # 代理管理：下线代理关系、下线代理查看、玩家房间列表、代理密码重置
    AccessObj(("agent"), None, 'MENU_AGENT_TXT'),
    AccessObj(("agent", "list"), 'GET', 'MENU_AGENT_LIST_TXT'),
    AccessObj(("agent", "role/list"), 'GET', 'MENU_AGENT_ROLE_LIST_TXT'),
    AccessObj(("agent", "room/list"), 'GET', 'MENU_AGENT_ROOM_LIST_TXT'),
    AccessObj(("agent", "reset/pwd"), 'GET', 'MENU_AGENT_RESET_PWD_TXT'),

    # 会员管理：会员列表、会员在线、会员默认钻石记录、会员分享记录、会员钻石消耗、会员积分兑换记录、会员钻石/积分增减记录、GM列表
    AccessObj(("member"), None, 'MENU_MEMBER_TXT'),
    AccessObj(("member", "list"), 'GET', 'MENU_MEMBER_LIST_TXT'),
    AccessObj(("agent", "member/curOnline"), 'GET', 'MENU_AGENT_MEMBER_CURONLINE_TXT'),
    AccessObj(("member", "defaultCard"), 'GET', 'MENU_AGENT_MEMBER_DEFAULTCARD_TXT'),
    AccessObj(("member", "share"), 'GET', 'MENU_AGENT_MEMBER_SHARE_TXT'),
    AccessObj(("member", "dayUseCard"), 'GET', 'MENU_AGENT_MEMBER_DAYUSE_TXT'),
    AccessObj(("member", "gamePoint"), 'GET', 'MENU_MEMBER_SEARCH_GAMEPOINT_TXT'),
    AccessObj(("member", "compensate"), 'GET', 'MENU_MEMBER_COMPENSATE_TXT'),
    AccessObj(("member", "gm/list"), 'GET', 'MENU_MEMBER_GM_SET_TXT'),

    # 我的订单：商城售钻记录、售卖钻石记录（代理）
    AccessObj(("order"), None, 'MENU_ORDER_TXT'),
    AccessObj(("order", "wechat/record"), 'GET', 'MENU_ORDER_WECHAT_TXT'),
    AccessObj(("order", "sale/record"), 'GET', 'MENU_ORDER_SALE_RECORD_TXT'),

    # 比赛场 #
    # 比赛场：比赛设置、比赛列表
    AccessObj(("match"), None, 'MENU_PARTY_THREE', True),
    AccessObj(("match", 'list'), 'GET', 'MENU_MATCH_LIST'),
    AccessObj(("match", 'run/list'), 'GET', 'MENU_MATCH_RUN_LIST'),

    # 邮件系统 #
    # 邮件系统：发送邮件、邮件列表、附件领取记录
    AccessObj(("bag"), None, 'BAG_MODEL_TXT', True),
    AccessObj(("bag", "send/mail"), 'POST', 'BAG_SEND_MAIL'),
    AccessObj(("bag", "mail/list"), 'GET', 'MENU_NOTIC_MAIL_LIST_TXT'),
    AccessObj(("bag", "mail/enclosure"), 'GET', 'BAG_ENCLOSURE_MAIL'),

    # 数据统计 #
    # 数据统计：注册人数统计、活跃人数统计、代理活跃统计、每日数据统计、用户留存统计、游戏玩法统计、赛事数据统计、赛事玩家统计、总体数据
    AccessObj(("accounts"), None, 'MENU_ACCOUNTS_TXT', True),
    AccessObj(("statistics", "reg"), 'GET', 'MENU_STATISTICS_REG_TXT'),
    AccessObj(("statistics", "active"), 'GET', 'MENU_STATISTICS_ACTIVE_TXT'),
    AccessObj(("agent", "active"), 'GET', 'MENU_AGENT_ACTIVE_TXT'),
    AccessObj(("statistics", "daily"), 'GET', 'MENU_STATISTICS_DAILY_TXT'),
    AccessObj(("statistics", "user/save"), 'GET', 'MENU_STATISTICS_USER_SAVE_TXT'),
    AccessObj(("statistics", "game/play"), 'GET', 'MENU_STATISTICS_GAME_PLAY_TXT'),
    AccessObj(("statistics", "match"), 'GET', 'MENU_STATISTICS_MATCH_TXT'),
    AccessObj(("statistics", "match/player"), 'GET', 'MENU_STATISTICS_MATCH_PLAYER_TXT'),
    AccessObj(("statistics", "overall/data"), 'GET', 'MENU_STATISTICS_OVERALL_DATA_TXT'),

    # 订单/报表 #
    # 订单/报表：我的售钻报表、下线代理售钻报表、下线代理购钻报表、利润占成报表
    # AccessObj(("accounts"), None, 'MENU_REPORT_TXT', True),
    # AccessObj(("statistics", "saleReport"), 'GET', 'MENU_STATISTICS_SALEREPORT_TXT'),
    # AccessObj(("statistics", "allAgentSaleReport"), 'GET', 'MENU_STATISTICS_AGENT_SALEREPORT_TXT'),
    # AccessObj(("statistics", "allAgentBuyReport"), 'GET', 'MENU_STATISTICS_AGENT_BUYREPORT_TXT'),
    # AccessObj(("statistics", "rateReport"), 'GET', 'MENU_STATISTICS_RATEREPORT_TXT'),

    # 个人信息 #
    # 个人信息：密码修改、操作记录、登录日志
    AccessObj(("person"), None, 'MENU_PERSON_TXT', True),
    AccessObj(("self", "modifyPasswd"), 'GET', 'MENU_SELF_MODIFYPASSWD_TXT'),
    AccessObj(("self", "syslog"), 'GET', 'MENU_SELF_SYSLOG_TXT'),
    AccessObj(("self", "loginLog"), 'GET', 'MENU_SELF_LOGINLOG_TXT'),

)

