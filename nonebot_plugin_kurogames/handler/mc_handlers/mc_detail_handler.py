import httpx
import json
import base64
from Crypto.Cipher import AES

header_data = {
        'source': 'android',
        'osVersion': '35',
        'countryCode': 'CN',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'model': '2201122C',
        'source': 'android',
        'lang': 'zh-Hans',
        'version': '2.5.1',
        'versionCode': '2510',
        'token': '',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'x-requested-with': 'com.kurogame.kjq',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'okhttp/3.11.0',
    }

async def refresh_role_data(roleId, serverId, token):
    bat = await request_token(roleId, serverId, token)
    b_at = json.loads(bat['data'])['accessToken']
    REFRESH_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/refreshData'
    header_data['token'] = token
    header_data['b-at'] = b_at
    form_data = {
        'gameId': 3,
        'roleId' : roleId,
        'serverId': serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_resource(token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/widget/game3/refresh' #gamer，没改到aki
    header_data['token'] = token
    form_data = {
        'gameId': 3,
        'type': 2,
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_role_data(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/roleData'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
        'roleId' : roleId,
        'serverId': serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_calabash_data(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/calabashData'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
        'roleId' : roleId,
        'serverId': serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_challenge_index(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/challengeDetails'
    header_data['token'] = token
    form_data = {
        'gameId' : 3,
        'roleId' : roleId,
        'serverId' : serverId,
        'countryCode' : 1
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_base_data(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/baseData'
    header_data['token'] = token
    form_data = {
        'gameId' : 3,
        'roleId' : roleId,
        'serverId' : serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_explore_index(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/exploreIndex'
    header_data['token'] = token
    form_data = {
        'gameId' : 3,
        'roleId' : roleId,
        'serverId' : serverId,
        'countryCode' : 1
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_role(token):
    REFRESH_URL = 'https://api.kurobbs.com/aki/role/list'
    header_data['token'] = token
    form_data = {
        'gameId' : 3
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_gacha(usr_id, record_id, card_pool_type, server_id):
    gacha_header_data = header_data.copy()
    GACHA_URL = 'https://gmserver-api.aki-game2.com/gacha/record/query'
    gacha_header_data['content-type'] = 'application/json;charset=UTF-8'
    form_data = {
        'playerId'      : usr_id,
        'serverId'      : server_id,
        'languageCode'  : 'zh-Hans',
        'recordId'      : record_id,
        'cardPoolType'  : card_pool_type
    }
    form_data_json = json.dumps(form_data)
    return await do_fetch(GACHA_URL, gacha_header_data, form_data_json)

async def get_mc_role_detail(usr_id, server_id, role_id, token):
    ROLE_DETAIL_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/getRoleDetail'
    header_data['token'] = token
    form_data = {
        'gameId'    : 3,
        'roleId'    : usr_id,
        'serverId'  : server_id,
        'id'        : role_id
    }
    return await do_fetch(ROLE_DETAIL_URL, header_data, form_data)

async def get_mc_tower_detail(usr_id, server_id, token):
    TOWER_DETAIL_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/towerDataDetail'
    header_data['token'] = token
    form_data = {
        'gameId'    : 3,
        'roleId'    : usr_id,
        'serverId'  : server_id
    }
    return await do_fetch(TOWER_DETAIL_URL, header_data, form_data)


async def get_mc_slash_detail(role_id, server_id, token):
    SLASH_DETAIL_URL = 'https://api.kurobbs.com/aki/roleBox/akiBox/slashDetail'
    header_data['token'] = token
    form_data = {
        'roleId'    : role_id,
        'serverId'  : server_id,
    }
    return await do_fetch(SLASH_DETAIL_URL, header_data, form_data)

async def request_token(role_id, server_id,token):
    REQUEST_URL = 'https://api.kurobbs.com/aki/roleBox/requestToken'
    header_data['token'] = token
    form_data = {
        'roleId'    : role_id,
        'serverId'  : server_id
    }
    return await do_fetch(REQUEST_URL, header_data, form_data)

async def do_fetch(url, header, data):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=header, data=data)
            #沟槽的库洛，10902是柠檬什么code🫵😡
            if not (response.status_code == 200 or response.status_code == 10902 or (
                    response.status_code == 0 and response.json().get('message') == 'success')):
                raise Exception('fetch error: ', response.status_code, response.reason_phrase)
            else:
                rsp = response.json()
                # 解密数据
                if 'data' in rsp:
                    encrypted_data = rsp['data']
                    # print(f"Encrypted data: {encrypted_data}")  # 调试信息

                    if isinstance(encrypted_data, dict):
                        # print("encrypted_data is a dict. Please check the structure.")
                        return rsp  # 或者你可以根据需要处理字典

                    # 尝试解密数据
                    decrypted_data = await decrypt_data(encrypted_data)

                    # 仅在解密成功时更新 rsp['data']
                    if isinstance(decrypted_data, dict):  # 检查解密结果是否为字典
                        rsp['data'] = decrypted_data
                if rsp.get('code') == 200 or rsp.get('code') == 10902 or rsp.get('message') == "success":
                    return rsp
                else:
                    raise Exception('api error:', rsp)
        except Exception as e:
            raise Exception('fetch error: ' + str(e))


async def decrypt_data(value):
    """
    :param value:加密数据
    :return:解密结果
    """
    key = base64.b64decode("XSNLFgNCth8j8oJI3cNIdw==")

    try:
        # 尝试解码和解密
        encrypted = base64.b64decode(value)

        # AES-128-ECB模式
        cipher = AES.new(key, AES.MODE_ECB)
        decrypted = cipher.decrypt(encrypted)

        # 去除填充并解析 JSON
        padding_length = decrypted[-1]
        decrypted = decrypted[:-padding_length]

        return json.loads(decrypted.decode('utf-8'))

    except Exception as e:
        # print(f": {e}, 返回原始内容")
        return value  # 返回原始内容
