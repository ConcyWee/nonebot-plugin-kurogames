import json
import time
from .mc_detail_handler import *
from .mc_pic_render import *
from ..calculate_time_stamp import calculate_time_stamp
async def mc_data_handler(data_row):

    mc_result           = {}
    roleId              = data_row[3]
    serverId            = data_row[6]    
    token_data          = data_row[4]
    b_at                = data_row[8]
    did                 = data_row[9]
    # token_data          = data_row['data']['token'] # 测试用
    #沟槽的库洛，角色数据也得刷新👊😡
    await refresh_role_data(roleId, serverId, b_at, did)

    current_timestamp = int(time.time())
    
    mc_base_data        = await get_mc_base_data(roleId, serverId, b_at, did)
    mc_role_data        = await get_mc_role_data(roleId, serverId, b_at, did)
    mc_calabash_data    = await get_mc_calabash_data(roleId, serverId, b_at, did)
    mc_challange_data   = await get_mc_challenge_index(roleId, serverId, b_at, did)
    mc_explore_data     = await get_mc_explore_index(roleId, serverId, b_at, did)
    mc_data             = await get_mc_data(roleId, serverId, token_data, b_at, did)

    mc_calabash_data_data   = json.loads(mc_calabash_data['data'])
    mc_role_data_data       = json.loads(mc_role_data['data'])
    mc_challange_data_data  = json.loads(mc_challange_data['data'])
    mc_explore_data_data    = json.loads(mc_explore_data['data'])
    mc_base_data_data       = json.loads(mc_base_data['data'])
    mc_data_data            = mc_data['data']

    mc_result['roleName']           = mc_data_data['roleName']
    mc_result['roleId']             = roleId
    mc_result['serverName']         = '鸣潮'
    mc_result['energyData']         = mc_data_data['energyData']
    mc_result['livenessData']       = mc_data_data['livenessData']
    mc_result['battlePassData']     = mc_data_data['battlePassData']
    mc_result['refreshTime']        = calculate_time_stamp(mc_data_data['energyData']['refreshTimeStamp'], current_timestamp) if mc_data_data['energyData']['refreshTimeStamp'] != 0 else "体力已满"
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
    find_flag           = True
    roleId              = data_row[3]
    serverId            = data_row[6]
    token_data          = data_row[4]
    b_at                = data_row[8]
    did                 = data_row[9]
    
    await refresh_role_data(roleId, serverId, b_at, did)
    mc_explore_data     = await get_mc_explore_index(roleId, serverId, b_at, did)
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
    role_exist_flag     = role_id = False
    roleId              = data_row[3]
    serverId            = data_row[6]    
    token_data          = data_row[4]
    b_at                = data_row[8]
    did                 = data_row[9]
    # token_data          = data_row # 测试用

    await refresh_role_data(roleId, serverId, b_at, did)
    role_list = await get_mc_role_data(roleId, serverId, b_at, did)
    role_data = json.loads(role_list['data'])['roleList']
    for role in role_data:
        if (role['roleName'] == role_name) or (role_name in role['roleName'] and '漂泊者' in role_name):
            role_exist_flag = True
            role_id         = role['roleId']
    if not role_exist_flag:
        return "你还没有获得该角色哦~"
    role_detail = await get_mc_role_detail(roleId, serverId, role_id, b_at, did)
    print('角色数据请求成功')
    user_data   = await get_mc_base_data(roleId, serverId, b_at, did)
    print('用户数据请求成功')
    data_pic = await mc_role_detail_render(role_detail['data'], user_data['data'])
    print('图片数据生成成功')
    return data_pic

async def mc_tower_detail_handler(data_row):
    roleId              = data_row[3]
    serverId            = data_row[6]    
    token_data          = data_row[4]
    b_at                = data_row[8]
    did                 = data_row[9]
    # token_data          = data_row['data']['token'] # 测试用

    await refresh_role_data(roleId, serverId, b_at, did)
    tower_data = await get_mc_tower_detail(roleId, serverId, b_at, did)
    user_data   = await get_mc_base_data(roleId, serverId, b_at, did)
    data_pic = await mc_tower_render(json.loads(tower_data['data']), json.loads(user_data['data']))
    if not data_pic:
        return "当前逆境深塔暂未开启~"
    return data_pic
    
async def mc_slash_detail_handler(data_row):
    roleId              = data_row[3]
    serverId            = data_row[6]    
    token_data          = data_row[4]
    b_at                = data_row[8]
    did                 = data_row[9]
    # token_data          = data_row['data']['token'] # 测试用
    
    await refresh_role_data(roleId, serverId, b_at, did)
    tower_data = await get_mc_slash_detail(roleId, serverId, b_at, did)
    user_data   = await get_mc_base_data(roleId, serverId, b_at, did)
    data_pic = await mc_slash_render(json.loads(tower_data['data']), json.loads(user_data['data']))
    if not data_pic:
        return "当前冥歌海墟暂未开启~"
    return data_pic
    
