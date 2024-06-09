import json
from .bbs_detail_handler import *

async def daily_task(qq_id, data_row):
    i = success_count = 0
    bbs_id            = data_row[0]
    pns_id            = data_row[2]
    mc_id             = data_row[3]
    user_token        = data_row[4]
    server_id         = data_row[5]
    mc_server_id      = data_row[6]
    token_data        = json.loads(user_token)['data']['token']
    daily_result      = '用户' + qq_id + '\n'
    try:
        await bbs_sign_in(token_data)
        daily_result += '库街区签到成功！\n'
    except Exception as e:
        start_index = str(e).find("'msg': '") + len("'msg': '")
        end_index = str(e).find("'", start_index)
        msg = str(e)[start_index:end_index]
        daily_result += '库街区签到失败：' + msg + '\n'

    if pns_id:
        try:
            await game_sign_in('2', server_id, pns_id, bbs_id, token_data)
            daily_result += '战双签到成功！\n'
        except Exception as e:
            start_index = str(e).find("'msg': '") + len("'msg': '")
            end_index = str(e).find("'", start_index)
            msg = str(e)[start_index:end_index]
            daily_result += '战双签到失败：' + msg + '\n'
    if mc_id:
        try:
            await game_sign_in('3', mc_server_id, mc_id, bbs_id, token_data)
            daily_result += '鸣潮签到成功！\n'
        except Exception as e:
            start_index = str(e).find("'msg': '") + len("'msg': '")
            end_index = str(e).find("'", start_index)
            msg = str(e)[start_index:end_index]
            daily_result += '鸣潮签到失败：' + msg + '\n'

    articles = await get_article_list(token_data)
    artile_list = articles['data']['postList']

    while success_count < 5 and i < 5:
        if artile_list[i]['isLike'] == 0:
            try:
                a = await browse_article(artile_list[i]['postId'], token_data)
                a = await like_article(artile_list[i]['postId'], artile_list[i]['userId'], token_data)
                a = await share_article(token_data)
                success_count += 1
            except:
                pass
            finally:
                i += 1
    if success_count == 5:
        daily_result += '库街区日常任务执行成功\n'
    else:
        daily_result += '库街区日常任务失败，请重新触发或手动执行'

    return daily_result


            




