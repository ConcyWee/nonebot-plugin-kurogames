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
        mc_detail = await get_mc_resource(token_data)
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

    mc_calabash_data_data   = json.loads(mc_calabash_data['data'])
    mc_role_data_data       = json.loads(mc_role_data['data'])
    mc_challange_data_data  = json.loads(mc_challange_data['data'])
    mc_explore_data_data    = json.loads(mc_explore_data['data'])
    mc_base_data_data       = json.loads(mc_base_data['data'])
    
    mc_result['roleName']           = mc_detail['data']['roleName']
    mc_result['roleId']             = mc_detail['data']['roleId']
    mc_result['serverName']         = mc_detail['data']['serverName']
    mc_result['energyData']         = mc_detail['data']['energyData']
    mc_result['livenessData']       = mc_detail['data']['livenessData']
    mc_result['battlePassData']     = mc_detail['data']['battlePassData']
    mc_result['refreshTime']        = calculate_time_stamp(mc_detail['data']['energyData']['refreshTimeStamp'], current_timestamp) if mc_detail['data']['energyData']['refreshTimeStamp'] != 0 else "体力已满"
    mc_result['roleList']           = mc_role_data_data['roleList']
    mc_result['calabashLevel']      = mc_calabash_data_data['level']
    mc_result['baseCatch']          = mc_calabash_data_data['baseCatch']
    mc_result['strengthenCatch']    = mc_calabash_data_data['strengthenCatch']
    mc_result['catchQuality']       = mc_calabash_data_data['catchQuality']
    mc_result['cost']               = mc_calabash_data_data['cost']
    mc_result['maxCount']           = mc_calabash_data_data['maxCount']
    mc_result['unlockCount']        = mc_calabash_data_data['unlockCount']
    mc_result['phantomList']        = mc_calabash_data_data['phantomList']
    mc_result['challengeInfo']      = mc_challange_data_data['challengeInfo']
    mc_result['baseData']           = mc_base_data_data
    mc_result['exploreData']        = mc_explore_data_data['exploreList']

    data_pic = await mc_pic_render(mc_result)
    return data_pic

async def mc_explore_detail_handler(data_row, area_name):
    mc_result           = {}
    user_token          = data_row[4]
    find_flag           = True
    token_data          = json.loads(user_token)['data']['token']
    try:
        mc_detail       = await get_mc_resource(token_data)
    except:
        return "还没有设置鸣潮角色哦~请点击打开库街区App在【我的】页面中设置角色"
    await refresh_role_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    mc_explore_data     = await get_mc_explore_index(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    temp_data = json.loads(mc_explore_data['data'])
    for area in temp_data['exploreList']:
        if area_name.strip() == area['country']['countryName']:
            current_explore_data = area
            find_flag = False
    if find_flag:
        return "未找到该地区名，请检查您的输入"
    data_pic            = await mc_explore_render(current_explore_data)
    return data_pic

async def mc_role_detail_handler(data_row, role_name : str):
    mc_result           = {}
    role_exist_flag     = role_id = False
    user_token          = data_row[4]
    token_data          = json.loads(user_token)['data']['token']
    # token_data          = data_row # 测试用
    try:
        mc_detail       = await get_mc_resource(token_data)
    except:
        return "还没有设置鸣潮角色哦~请点击打开库街区App在【我的】页面中设置角色"
    
    await refresh_role_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    role_list = await get_mc_role_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    role_data = json.loads(role_list['data'])['roleList']
    for role in role_data:
        if (role['roleName'] == role_name) or (role_name in role['roleName'] and '漂泊者' in role_name):
            role_exist_flag = True
            role_id         = role['roleId']
    if not role_exist_flag:
        return "你还没有获得该角色哦~"
    role_detail = await get_mc_role_detail(mc_detail['data']['roleId'], mc_detail['data']['serverId'], role_id, token_data)
    print('角色数据请求成功')
    user_data   = await get_mc_base_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    print('用户数据请求成功')
    data_pic = await mc_role_detail_render(role_detail['data'], user_data['data'])
    print('图片数据生成成功')
    return data_pic

async def mc_tower_detail_handler(data_row):
    mc_result           = {}
    user_token          = data_row[4]
    token_data          = json.loads(user_token)['data']['token']
    # token_data          = data_row['data']['token'] # 测试用
    try:
        mc_detail       = await get_mc_resource(token_data)
    except:
        return "还没有设置鸣潮角色哦~请点击打开库街区App在【我的】页面中设置角色"
    await refresh_role_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    tower_data = await get_mc_tower_detail(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    user_data   = await get_mc_base_data(mc_detail['data']['roleId'], mc_detail['data']['serverId'], token_data)
    data_pic = await mc_tower_render(json.loads(tower_data['data']), json.loads(user_data['data']))
    if not data_pic:
        return "当前逆境深塔暂未开启~"
    return data_pic
    
