async def kuro_help():
    help_detail = ""
    help_detail += "-发送“战双登录 token”登录(推荐)\n"
    help_detail += "  发送“战双登录 手机号 验证码”(用空格分隔)即可登录\n"
    help_detail += "  （不建议使用短信验证码，库街区只允许一处登录，使用该方式会导致无法使用库街区）\n"
    help_detail += "-发送“战双数据”即可查询战双信息\n"
    help_detail += "  （zssj、战双详情、zsxq、我的战双卡片、战双数据 皆可触发）\n"
    help_detail += "-发送“鸣潮数据”即可查询战双信息\n"
    help_detail += "  （鸣潮详情、mcxq、我的鸣潮卡片、鸣潮数据 皆可触发）\n"
    help_detail += "-发送“库洛签到”完成库街区每日任务\n"
    help_detail += "  （战双签到、鸣潮签到、库街区每日、库洛每日、库街区签到 皆可触发）\n"
    return help_detail