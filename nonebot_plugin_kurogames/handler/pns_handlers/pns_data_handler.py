import json
import time
from .pns_detail_handler import getPunishingResource, get_monthly_resource, get_pns_game_account, get_punishing_account_info
from ..pns_dao import UserInfoManagement
from ..calculate_time_stamp import calculate_time_stamp
from .pns_pic_render import pic_generator

async def pns_data_handler(data_row):
    pns_result = {}
    user_token        = data_row[4] #获取token
    token_data        = json.loads(user_token)['data']['token']
    pns_detail        = getPunishingResource(token_data)
    pns_resource      = get_monthly_resource(pns_detail['data']['roleId'], token_data)
    pns_role_list     = get_punishing_account_info(token_data)
    pns_account       = get_pns_game_account(pns_detail['data']['roleId'], pns_detail['data']['serverId'], token_data)
    current_timestamp = int(time.time())


    pns_result['roleName']                    = pns_detail['data']['roleName']
    pns_result['level']                       = (str(pns_account['data']['pointAfter']) + "勋阶") if pns_account['data']['roleLevel'] == 120 else (str(pns_account['data']['roleLevel']) + "级")
    pns_result['server']                      = pns_account['data']['serverName'] + "服"
    pns_result['roleId']                      = pns_detail['data']['roleId']
    pns_result['roleScore']                   = pns_role_list['data'][0]['roleScore']
    pns_result['roleNum']                     = pns_role_list['data'][0]['roleNum']
    pns_result['fashionCollectionPercent']    = str(int(pns_role_list['data'][0]['fashionCollectionPercent'] * 100)) + '%'
    pns_result['actionValue']                 = pns_detail['data']['actionData']['value']
    pns_result['actionRefreshTimeStamp']      = calculate_time_stamp(pns_detail['data']['actionData']['refreshTimeStamp'], current_timestamp)
    pns_result['blackCardNum']                = pns_resource['data']['currentBlackCard']
    pns_result['developResourceNum']          = pns_resource['data']['currentDevelopResource']
    pns_result['bossRefreshTimeStamp']        = calculate_time_stamp(pns_detail['data']['bossData'][0]['refreshTimeStamp'],current_timestamp)
    pns_result['bossBlackCard']               = pns_detail['data']['bossData'][0]['value']
    pns_result['transfiniteNum']              = pns_detail['data']['bossData'][1]['value']
    pns_result['transfiniteRefreshTimeStamp'] = calculate_time_stamp(pns_detail['data']['bossData'][1]['refreshTimeStamp'], current_timestamp)
    pns_result['arenaRefreshTimeStamp']       = calculate_time_stamp(pns_detail['data']['bossData'][2]['refreshTimeStamp'], current_timestamp)
    pns_result['arenaBlackCard']              = pns_detail['data']['bossData'][2]['value']
    pns_result['strongHoldRate']              = pns_detail['data']['bossData'][3]['value']
    pns_result['strongHoldTimeStamp']         = calculate_time_stamp(pns_detail['data']['bossData'][3]['refreshTimeStamp'], current_timestamp)
    data_pic = await pic_generator(pns_result)
    return(data_pic)