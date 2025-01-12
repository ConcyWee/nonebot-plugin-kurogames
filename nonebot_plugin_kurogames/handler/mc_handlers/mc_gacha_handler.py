import asyncio
from .mc_detail_handler import get_mc_gacha
from ..pns_dao import UserInfoManagement

manager = UserInfoManagement()
gacha_mapping = {
    "角色up"   : 1,
    "武器up"   : 2,
    "角色常驻"     : 3,
    "武器常驻"     : 4,
    "新手池"     : 5,
    "新手自选池" : 6
}
resident_roles = ["凌阳", "鉴心", "卡卡罗", "安可", "维里奈"]

async def gacha_analysis(qq_id, gacha_type):
    five_star_count    = 0
    up_five_star_count = 0

    data = manager._get_data(qq_id)
    if not data[7] or not data:
        return "请先录入抽卡数据码"
    result          = ''
    mc_id           = data[3]
    record_id       = data[7]
    server_id       = data[6]
    card_pool_type  = gacha_mapping.get(gacha_type, 3)
    try:
        gacha_data      = (await get_mc_gacha(mc_id, record_id, card_pool_type, server_id))['data']
    except:
        return "查询失败，数据可能已过期"
    first_five_star_index = None
    padded_draws = 0
    five_star_analysis = {}

    for i, item in enumerate(gacha_data):
        if item['qualityLevel'] == 5:
            if first_five_star_index is None:
                padded_draws = i
                first_five_star_index = i
            else:
                draws_after_last_star = sum(1 for entry in gacha_data[first_five_star_index+1:i] if entry['qualityLevel'] != 5) + 1
                five_star_analysis[gacha_data[first_five_star_index]['name'] + '-' + str(i)] = {
                    'draws_after': draws_after_last_star,
                    'time': gacha_data[first_five_star_index]['time']
                }
                first_five_star_index = i
    if first_five_star_index is None:
        padded_draws = i

    if first_five_star_index is not None:
        draws_after_last_star = sum(1 for entry in gacha_data[first_five_star_index+1:] if entry['qualityLevel'] != 5) + 1
        five_star_analysis[gacha_data[first_five_star_index]['name'] + '-' + str(i)] = {
            'draws_after': draws_after_last_star,
            'time': gacha_data[first_five_star_index]['time']
        }

    for name, info in five_star_analysis.items():
        if (card_pool_type == 1) and (name.split('-')[0] in resident_roles):
            result += f"{name.split('-')[0]}: {info['draws_after']} 抽 - 获得时间: {info['time']}（歪）\n"
            five_star_count += 1
        else:
            result += f"{name.split('-')[0]}: {info['draws_after']} 抽 - 获得时间: {info['time']}\n"
            five_star_count     += 1
            up_five_star_count  += 1

    result += "\n"

    gacha_count = len(gacha_data)
    if five_star_count != 0:
        each_five_star_cost    = gacha_count // five_star_count
        result += f"平均{each_five_star_cost}抽出金\n"
        if up_five_star_count != 0:
            each_up_five_star_cost = gacha_count // up_five_star_count
            if card_pool_type == 1 or card_pool_type == 2:
                result += f"平均{each_up_five_star_cost}抽获得一个当期up\n"
        else:
            each_up_five_star_cost = 114514 #哼哼哼啊啊啊啊啊啊啊啊啊啊
        luck_analyse           = await gacha_luck_analyse(each_up_five_star_cost)

        result += f"{luck_analyse}\n"
    else:
        result += f"暂时还没出金呦~\n"
    result += f"卡池已垫了{padded_draws} 抽"

    return result

async def gacha_luck_analyse(each_five_star_cost):
    if each_five_star_cost <= 10:
        return f"不是，哥们，你不许玩鸣潮！"
    if each_five_star_cost > 10  and each_five_star_cost <= 40:
        return f"我靠，海豹！"
    if each_five_star_cost > 40  and each_five_star_cost <= 60:
        return f"我靠，欧皇！"
    if each_five_star_cost > 60  and each_five_star_cost <= 70:
        return f"运气不错嘛"
    if each_five_star_cost > 70  and each_five_star_cost <= 100:
        return f"中规中矩"
    if each_five_star_cost > 100 and each_five_star_cost <= 130:
        return f"有点小非"
    if each_five_star_cost > 130 and each_five_star_cost <= 150:
        return f"发现了非酋"
    if each_five_star_cost > 150 and each_five_star_cost <= 160:
        return f"究极大非酋"
    if each_five_star_cost == 114514: #哼哼哼啊啊啊啊啊啊啊啊啊啊
        return f"还没抽到up呦~"