import json
from ..pns_dao import UserInfoManagement
from ..token_judgement import token_judgement
from .pns_detail_handler import get_punishing_account_info, get_mc_account_info

manager = UserInfoManagement()
async def pns_login_handler(user_id, data_content):

    if data_content == "":
        return("请输入战双token, 如：/战双登录 your_token")
    token_result = token_judgement(data_content)
    if token_result != "success":
        return token_result

    pns_info  = await get_punishing_account_info(json.loads(data_content)["data"]["token"])
    mc_info   = await get_mc_account_info(json.loads(data_content)["data"]["token"])

    pns_id    = None                          if (not pns_info["data"]) else pns_info["data"][0]["roleId"]
    mc_id     = None                          if (not mc_info["data"])  else mc_info ["data"][0]["roleId"]
    bbs_id    = pns_info["data"][0]["userId"] if pns_id                 else mc_info ["data"][0]["userId"]

    if pns_id or mc_id:
        data = {
            'bbsId': bbs_id,
            'userId': user_id,
            'pnsId': pns_id,
            'mcId': mc_id,
            'token': str(data_content),
            'serverId': '',
            'mcServerId': ''
        }
        if pns_id:
            data['serverId'] = pns_info["data"][0]["serverId"]
        if mc_id:
            data['mcServerId'] = mc_info["data"][0]["serverId"]
        
        if manager._get_data(user_id):
            try:
                manager._update_data(user_id, data)
            except Exception as e:
                return("更新数据失败: " + str(e))
            return("token更新成功！")
        else:
            try:
                manager._insert_data(user_id, data)
            except Exception as e:
                return("插入数据失败: " + str(e))
        return("token保存成功！")
    return("该账号暂未绑定任何游戏")

        


async def get_kuro_token(qq_id):
    result = manager._get_data(qq_id)
    return result