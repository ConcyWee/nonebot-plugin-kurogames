import re
from ..pns_dao import UserInfoManagement


manager = UserInfoManagement()
hex_pattern = re.compile(r'\b[a-z0-9]{32}\b')
async def mc_gacha_login_handler(qq_id, gacha_id):
    if hex_pattern.match(gacha_id):
        if manager._get_data(qq_id):
            manager._update_gacha_info(qq_id, gacha_id)
            return "更新卡池ID成功"
        else:
            return "请先输入库街区token"
    elif "record_id=" in gacha_id:
        start_index = gacha_id.find("record_id=")
        result = gacha_id[start_index + len("record_id="):start_index + len("record_id=") + 32]
        print(result)
        if manager._get_data(qq_id):
            manager._update_gacha_info(qq_id, result)
            return "更新卡池ID成功"
        else:
            return "请先输入库街区token"
    
    return "数据码格式有误"