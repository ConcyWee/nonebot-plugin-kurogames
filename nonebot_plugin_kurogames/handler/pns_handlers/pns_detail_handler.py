import httpx

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

def getPunishingResource(token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/widget/game2/refresh'
    header_data['token'] = token
    form_data = {
        'gameId': 2,
        'type': 2,
    }

    try:
        result = do_fetch(REFRESH_URL, header_data, form_data)
    except Exception as e:
        raise e
    return result

def get_punishing_account_info(token):
    PNS_INFO_URL = 'https://api.kurobbs.com/gamer/role/list'
    header_data['token'] = token
    form_data = {
        'gameId': 2,
    }

    try:
        result = do_fetch(PNS_INFO_URL, header_data, form_data)
    except Exception as e:
        raise e
    return result

def get_mc_account_info(token):

    MC_INFO_URL = 'https://api.kurobbs.com/gamer/role/list'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
    }

    try:
        result = do_fetch(MC_INFO_URL, header_data, form_data)
    except Exception as e:
        raise e
    return result

def get_monthly_resource(roleId, token):
    MONTHLY_RESOURCE_URL = 'https://api.kurobbs.com/gamer/resource/month'
    header_data['token'] = token
    form_data = {
        'roleId': roleId,
    }
    try:
        result = do_fetch(MONTHLY_RESOURCE_URL, header_data, form_data)
    except Exception as e:
        raise e
    return result

def get_pns_game_account(roleId, serverId, token):
    GAME_ACCOUNT_URL = 'https://api.kurobbs.com/gamer/roleBox/gameAccount'
    header_data['token'] = token
    form_data = {
        'gameId' : 2,
        'roleId' : roleId,
        'serverId' : serverId,
    }
    try:
        result = do_fetch(GAME_ACCOUNT_URL, header_data, form_data)
    except Exception as e:
        raise e
    return result

def do_fetch(url, header, data):
    try:
        response = httpx.post(url, headers=header, data=data)
        if not (response.status_code == 200):
            raise Exception('fetch error: ', response.status_code, response.reason_phrase)
        else:
            rsp = response.json()

            if rsp.get('code') == 200:
                result = rsp
            else:
                raise Exception('api error:', rsp)
    except Exception as e:
        raise Exception('fetch error: '+ str(e))
    return result
