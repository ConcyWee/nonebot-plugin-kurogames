import json
import time
from .pns_detail_handler import *
from ..calculate_time_stamp import calculate_time_stamp
from .pns_pic_render import pic_generator

async def pns_data_handler(data_row):
    pns_result = {}
    user_token        = data_row[4]
    token_data        = json.loads(user_token)['data']['token']
    try:
        pns_detail    = await get_punishing_resource(token_data)
    except:
        return "还没有设置战双角色哦~请点击打开库街区App在【我的】页面中设置角色"
    pns_resource      = await get_monthly_resource(pns_detail['data']['roleId'], token_data)
    pns_role_list     = await get_punishing_account_info(token_data)
    pns_account       = await get_pns_game_account(pns_detail['data']['roleId'], pns_detail['data']['serverId'], token_data)
    current_timestamp = int(time.time())


    pns_result['roleName']                    = pns_detail['data']['roleName']
    pns_result['level']                       = (str(pns_account['data']['rank']) + "勋阶") if pns_account['data']['level'] == 120 else (str(pns_account['data']['level']) + "级")
    pns_result['server']                      = pns_account['data']['serverName'] + "服"
    pns_result['roleId']                      = pns_detail['data']['roleId']
    pns_result['roleScore']                   = pns_role_list['data'][0]['roleScore']
    pns_result['roleNum']                     = pns_role_list['data'][0]['roleNum']
    pns_result['fashionCollectionPercent']    = str(int(pns_role_list['data'][0]['fashionCollectionPercent'] * 100)) + '%'
    pns_result['actionValue']                 = pns_detail['data']['actionData']['value']
    pns_result['actionRefreshTimeStamp']      = calculate_time_stamp(pns_detail['data']['actionData']['refreshTimeStamp'], current_timestamp) if pns_detail['data']['actionData']['refreshTimeStamp'] != 0 else "血清已满"
    pns_result['blackCardNum']                = pns_resource['data']['currentBlackCard']
    pns_result['developResourceNum']          = pns_resource['data']['currentDevelopResource']
    pns_result['roleDevelopNum']              = pns_resource['data']['currentDevelopResourceDetailed']['roleDevelopNum']
    pns_result['weaponDevelopNum']            = pns_resource['data']['currentDevelopResourceDetailed']['weaponDevelopNum']
    pns_result['assistDevelopNum']            = pns_resource['data']['currentDevelopResourceDetailed']['assistDevelopNum']
    pns_result['baseRoleNum']                 = pns_resource['data']['currentDevelopResourceDetailed']['baseRoleNum']
    pns_result['baseWeaponNum']               = pns_resource['data']['currentDevelopResourceDetailed']['baseWeaponNum']
    pns_result['bossRefreshTimeStamp']        = calculate_time_stamp(pns_detail['data']['bossData'][0]['refreshTimeStamp'],current_timestamp) if pns_detail['data']['bossData'][0]['refreshTimeStamp'] != None else "非战斗期"
    pns_result['bossBlackCard']               = pns_detail['data']['bossData'][0]['value']
    pns_result['transfiniteNum']              = pns_detail['data']['bossData'][1]['value']
    pns_result['transfiniteRefreshTimeStamp'] = calculate_time_stamp(pns_detail['data']['bossData'][1]['refreshTimeStamp'], current_timestamp) if pns_detail['data']['bossData'][1]['refreshTimeStamp'] != None else "非战斗期"
    pns_result['arenaRefreshTimeStamp']       = calculate_time_stamp(pns_detail['data']['bossData'][2]['refreshTimeStamp'], current_timestamp) if pns_detail['data']['bossData'][2]['refreshTimeStamp'] != None else "非战斗期"
    pns_result['arenaBlackCard']              = pns_detail['data']['bossData'][2]['value']
    pns_result['strongHoldRate']              = pns_detail['data']['bossData'][3]['value']
    pns_result['strongHoldTimeStamp']         = calculate_time_stamp(pns_detail['data']['bossData'][3]['refreshTimeStamp'], current_timestamp) if pns_detail['data']['bossData'][3]['refreshTimeStamp'] != None else "非战斗期"
    data_pic = await pic_generator(pns_result)
    return(data_pic)