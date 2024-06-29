import httpx
import json

header_data = {
        'osversion': 'Android',
        'devcode': 'A734EC22C2D3F93154BC2952A30ABF5A32F01753',
        'countryCode': 'CN',
        'pragma': 'no-cache',
        'cache-control': 'no-cache',
        'accept': 'application/json, text/plain, */*',
        'model': '2201122C',
        'source': 'android',
        'lang': 'zh-Hans',
        'version': '2.1.0',
        'versionCode': '2100',
        'token': '',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'x-requested-with': 'com.kurogame.kjq',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'okhttp/3.10.0',
    }

async def refresh_role_data(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/roleBox/aki/refreshData'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
        'roleId' : roleId,
        'serverId': serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_resource(token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/widget/game3/refresh'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
        'type': 2,
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_role_data(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/roleBox/aki/roleData'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
        'roleId' : roleId,
        'serverId': serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_calabash_data(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/roleBox/aki/calabashData'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
        'roleId' : roleId,
        'serverId': serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_challenge_index(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/roleBox/aki/challengeIndex'
    header_data['token'] = token
    form_data = {
        'gameId' : 3,
        'roleId' : roleId,
        'serverId' : serverId,
        'countryCode' : 1
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_base_data(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/roleBox/aki/baseData'
    header_data['token'] = token
    form_data = {
        'gameId' : 3,
        'roleId' : roleId,
        'serverId' : serverId
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_explore_index(roleId, serverId, token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/roleBox/aki/exploreIndex'
    header_data['token'] = token
    form_data = {
        'gameId' : 3,
        'roleId' : roleId,
        'serverId' : serverId,
        'countryCode' : 1
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_mc_role(token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/role/list'
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


async def do_fetch(url, header, data):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=header, data=data)
            if not (response.status_code == 200 or (response.status_code == 0 and response.json.get('message') == 'success')):
                raise Exception('fetch error: ', response.status_code, response.reason_phrase)
            else:
                rsp = response.json()

                if rsp.get('code') == 200 or rsp.get('message') == "success":
                    return rsp
                else:
                    raise Exception('api error:', rsp)
        except Exception as e:
            raise Exception('fetch error: '+ str(e))