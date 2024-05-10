import json

def token_judgement(token):
    try:
        data_dict = json.loads(token)
    except ValueError as e:
        return "错误: token格式错误"
    required_keys = ["code", "data", "msg", "success"]
    for key in required_keys:
        if key not in data_dict:
            return f"缺少关键字段: {key}"
        
    data_dict_data = data_dict.get("data")
    if "token" not in data_dict_data:
        return "缺少关键字段: code.token"
    return "success"