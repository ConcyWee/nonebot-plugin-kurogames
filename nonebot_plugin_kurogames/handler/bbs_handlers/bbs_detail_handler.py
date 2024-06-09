import httpx
import datetime

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

async def game_sign_in(game_id, server_id, role_id, bbs_id, token):
    SIGN_URL = 'https://api.kurobbs.com/encourage/signIn/v2'
    header_data['token'] = token
    form_data = {
        'gameId': game_id,
        'serverId': server_id,
        'roleId': role_id,
        'userId': bbs_id,
        'reqMonth': datetime.datetime.now().strftime("%m")
    }
    return await do_fetch(SIGN_URL, header_data, form_data)

async def bbs_sign_in(token):
    SIGN_URL = 'https://api.kurobbs.com/user/signIn'
    header_data['token'] = token
    form_data = {
        'gameId': 2
    }
    return await do_fetch(SIGN_URL, header_data, form_data)

async def get_article_list(token):
    LIST_URL = 'https://api.kurobbs.com/forum/list'
    header_data['token'] = token
    form_data = {
        'forumId': 10,
        'gameId': 3,
        'pageIndex': 1,
        'pageSize': 10,
        'searchType': 1,
        'timeType': 0,
        'topicId': 0
    }
    return await do_fetch(LIST_URL, header_data, form_data)

async def like_article(article_id, author_id, token):
    LIKE_URL = 'https://api.kurobbs.com/forum/like'
    header_data['token'] = token
    form_data = {
        'forumId': 10,
        'gameId': 3,
        'likeType': 1,
        'operateType': 1,
        'postCommentId': 0,
        'postId': article_id,
        'postType': 1,
        'toUserId': author_id
    }
    return await do_fetch(LIKE_URL, header_data, form_data)

async def share_article(token):
    SHARE_URL= 'https://api.kurobbs.com/encourage/level/shareTask'
    header_data['token'] = token
    form_data = {
        'gameId': 3
    }
    return await do_fetch(SHARE_URL, header_data, form_data)

async def browse_article(article_id, token):
    BROWSE_URL = 'https://api.kurobbs.com/forum/getPostDetail'
    header_data['token'] = token
    form_data = {
        'isOnlyPublisher': 0,
        'postId': article_id,
        'showOrderType': 2
    }
    return await do_fetch(BROWSE_URL, header_data, form_data)

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
