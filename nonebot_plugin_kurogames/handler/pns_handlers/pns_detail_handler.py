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
        'version': '2.2.0',
        'versionCode': '2200',
        'token': '',
        'distinct_id' : 'e311206c-57d9-41bc-94ba-2555f9124837',
        'content-type': 'application/x-www-form-urlencoded; charset=utf-8',
        'x-requested-with': 'com.kurogame.kjq',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'user-agent': 'okhttp/3.11.0',
    }

async def kuro_sdk_login(mobile, code):
    LOGIN_URL = 'https://api.kurobbs.com/user/sdkLogin'
    form_data = {
        'code': code,
        'devCode': 'A734EC22C2D3F93154BC2952A30ABF5A32F01753',
        'gameList': '',
        'mobile': mobile
    }
    try:
        return await do_fetch(LOGIN_URL, header_data, form_data)
    except Exception as e:
        start_index = str(e).find("'msg': '") + len("'msg': '")
        end_index = str(e).find("'", start_index)
        msg = str(e)[start_index:end_index]
        return msg

async def get_punishing_resource(token):
    REFRESH_URL = 'https://api.kurobbs.com/gamer/widget/game2/refresh'
    # REFRESH_URL = 'https://api.kurobbs.com/haru/roleBox/refreshData'
    header_data['token'] = token
    form_data = {
        'gameId': 2,
        'type': 2,
    }
    return await do_fetch(REFRESH_URL, header_data, form_data)

async def get_punishing_account_info(token):
    PNS_INFO_URL = 'https://api.kurobbs.com/gamer/role/list'
    header_data['token'] = token
    form_data = {
        'gameId': 2,
    }
    return await do_fetch(PNS_INFO_URL, header_data, form_data)

async def get_mc_account_info(token):

    MC_INFO_URL = 'https://api.kurobbs.com/gamer/role/list'
    header_data['token'] = token
    form_data = {
        'gameId': 3,
    }

    return await do_fetch(MC_INFO_URL, header_data, form_data)

async def get_monthly_resource(roleId, token):
    MONTHLY_RESOURCE_URL = 'https://api.kurobbs.com/gamer/resource/month'
    header_data['token'] = token
    form_data = {
        'roleId': roleId,
    }
    return await do_fetch(MONTHLY_RESOURCE_URL, header_data, form_data)

async def get_pns_game_account(roleId, serverId, token):
    # GAME_ACCOUNT_URL = 'https://api.kurobbs.com/gamer/roleBox/gameAccount'
    GAME_ACCOUNT_URL = 'https://api.kurobbs.com/haru/roleBox/accountData'
    header_data['token'] = token
    form_data = {
        'gameId' : 2,
        'roleId' : roleId,
        'serverId' : serverId,
    }
    return await do_fetch(GAME_ACCOUNT_URL, header_data, form_data)

async def do_fetch(url, header, data):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=header, data=data)
            if not (response.status_code == 200):
                raise Exception('fetch error: ', response.status_code, response.reason_phrase)
            else:
                rsp = response.json()

                if rsp.get('code') == 200:
                    return rsp
                else:
                    raise Exception('api error:', rsp)
        except Exception as e:
            raise Exception('fetch error: '+ str(e))
