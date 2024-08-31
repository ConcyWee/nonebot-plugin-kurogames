import json
import time
from .mc_detail_handler import *
from .mc_pic_render import *
from ..calculate_time_stamp import calculate_time_stamp
async def mc_data_handler(data_row):

    mc_result           = {}
    user_token          = data_row[4]
    token_data          = json.loads(user_token)['data']['token']
    # token_data          = data_row['data']['token'] # 测试用
    try:
        mc_detail           = await get_mc_resource(token_data)
    except:
        return "还没有设置鸣潮角色哦~请点击打开库街区App在【我的】页面中设置角色"
    
    #沟槽的库洛，角色数据也得刷新👊😡
    await refresh_role_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)

    current_timestamp = int(time.time())
    
    mc_base_data        = await get_mc_base_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    mc_role_data        = await get_mc_role_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    mc_calabash_data    = await get_mc_calabash_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    mc_challange_data   = await get_mc_challenge_index(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    mc_explore_data     = await get_mc_explore_index(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)

    mc_result['roleName']           = mc_detail['data']['roleName']
    mc_result['roleId']             = mc_detail['data']['roleId']
    mc_result['serverName']         = mc_detail['data']['serverName']
    mc_result['energyData']         = mc_detail['data']['energyData']
    mc_result['livenessData']       = mc_detail['data']['livenessData']
    mc_result['battlePassData']     = mc_detail['data']['battlePassData']
    mc_result['refreshTime']        = calculate_time_stamp(mc_detail['data']['energyData']['refreshTimeStamp'], current_timestamp) if mc_detail['data']['energyData']['refreshTimeStamp'] != 0 else "体力已满"
    mc_result['roleList']           = mc_role_data['data']['roleList']
    mc_result['calabashLevel']      = mc_calabash_data['data']['level']
    mc_result['baseCatch']          = mc_calabash_data['data']['baseCatch']
    mc_result['strengthenCatch']    = mc_calabash_data['data']['strengthenCatch']
    mc_result['catchQuality']       = mc_calabash_data['data']['catchQuality']
    mc_result['cost']               = mc_calabash_data['data']['cost']
    mc_result['maxCount']           = mc_calabash_data['data']['maxCount']
    mc_result['unlockCount']        = mc_calabash_data['data']['unlockCount']
    mc_result['phantomList']        = mc_calabash_data['data']['phantomList']
    mc_result['challengeList']      = mc_challange_data['data']['indexList']
    mc_result['baseData']           = mc_base_data['data']
    mc_result['exploreData']        = mc_explore_data['data']

    data_pic = await mc_pic_render(mc_result)   
    return data_pic

async def mc_explore_detail_handler(data_row):
    mc_result           = {}
    user_token          = data_row[4]
    token_data          = json.loads(user_token)['data']['token']
    try:
        mc_detail       = await get_mc_resource(token_data)
    except:
        return "还没有设置鸣潮角色哦~请点击打开库街区App在【我的】页面中设置角色"
    mc_explore_data     = await get_mc_explore_index(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    
    data_pic            = await mc_explore_render(mc_explore_data['data'])
    return data_pic

async def mc_role_detail_handler(data_row, role_name : str):
    mc_result           = {}
    role_exist_flag     = role_id = False
    user_token          = data_row[4]
    token_data          = json.loads(user_token)['data']['token']
    # token_data          = data_row['data']['token'] # 测试用
    try:
        mc_detail       = await get_mc_resource(token_data)
    except:
        return "还没有设置鸣潮角色哦~请点击打开库街区App在【我的】页面中设置角色"
    
    role_list = await get_mc_role_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    role_data = role_list['data']['roleList']
    for role in role_data:
        if (role['roleName'] == role_name) or (role_name in role['roleName'] and '漂泊者' in role_name):
            role_exist_flag = True
            role_id         = role['roleId']
    if not role_exist_flag:
        return "你还没有获得该角色哦~"
    role_detail = await get_mc_role_detail(mc_detail['data']['roleId'], mc_detail['data']['serverId'], role_id, token_data)
    user_data   = await get_mc_base_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)

    data_pic = await mc_role_detail_render(role_detail['data'], user_data['data'])
    return data_pic
