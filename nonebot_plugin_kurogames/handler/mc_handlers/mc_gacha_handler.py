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
async def gacha_analysis(qq_id, gacha_type):
    data = manager._get_data(qq_id)
    if not data[7] or not data:
        return "请先录入抽卡数据码"
    result          = ''
    mc_id           = data[3]
    record_id       = data[7]
    server_id       = data[6]
    card_pool_type  = gacha_mapping.get(gacha_type, 3)
    gacha_data      = (await get_mc_gacha(mc_id, record_id, card_pool_type, server_id))['data']

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
                five_star_analysis[gacha_data[first_five_star_index]['name']] = {
                    'draws_after': draws_after_last_star,
                    'time': gacha_data[first_five_star_index]['time']
                }
                first_five_star_index = i
    if first_five_star_index is None:
        padded_draws = i

    if first_five_star_index is not None:
        draws_after_last_star = sum(1 for entry in gacha_data[first_five_star_index+1:] if entry['qualityLevel'] != 5) + 1
        five_star_analysis[gacha_data[first_five_star_index]['name']] = {
            'draws_after': draws_after_last_star,
            'time': gacha_data[first_five_star_index]['time']
        }

    print(f"卡池已垫的次数为: {padded_draws} 抽")
    for name, info in five_star_analysis.items():
        result += f"{name}: {info['draws_after']} 抽 - 获得时间: {info['time']}\n"
    result += f"卡池已垫了{padded_draws} 抽\n"
    return result
