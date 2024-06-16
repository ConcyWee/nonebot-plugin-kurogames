import os
import requests
import json

# 定义存储文件路径
cache_file_path = "image_cache.json"

# 创建一个字典用于保存已下载的图片文件路径
image_cache = {}

# 加载本地缓存文件
if os.path.exists(cache_file_path):
    with open(cache_file_path, "r") as f:
        image_cache = json.load(f)


def save_cache_to_file(cache, file_path):
    with open(file_path, "w") as f:
        json.dump(cache, f)

def get_image(role_name, role_icon_url):
    # 检查字典中是否存在对应的文件路径
    if role_name in image_cache:
        # 如果存在，则直接使用本地文件
        image_path = image_cache[role_name]
    else:
        # 如果不存在，则下载图片并保存到本地
        response = requests.get(role_icon_url)
        if response.status_code == 200:
            # 生成本地文件路径
            image_filename = f"{role_name}.png"
            image_path = os.path.join("image_cache", image_filename)
            # 保存图片到本地
            with open(image_path, "wb") as f:
                f.write(response.content)
            # 将文件路径添加到字典中
            image_cache[role_name] = image_path
            # 保存字典到本地文件
            save_cache_to_file(image_cache, cache_file_path)
        else:
            # 请求失败，返回空路径
            image_path = ""

    return image_path

# 测试代码
json_data = [
    {
        "roleId": 1402,
        "level": 40,
        "roleName": "秧秧",
        "roleIconUrl": "https://web-static.kurobbs.com/adminConfig/27/role_icon/1716031170021.png",
        "rolePicUrl": "https://web-static.kurobbs.com/adminConfig/27/role_pic/1716384481195.png",
        "starLevel": 4,
        "attributeId": 4,
        "attributeName": "气动",
        "weaponTypeId": 2,
        "weaponTypeName": "迅刀",
        "acronym": "yy",
        "mapRoleId": None
    },
    {
        "roleId": 1202,
        "level": 40,
        "roleName": "炽霞",
        "roleIconUrl": "https://web-static.kurobbs.com/adminConfig/27/role_icon/1716031234646.png",
        "rolePicUrl": "https://web-static.kurobbs.com/adminConfig/27/role_pic/1716384656257.png",
        "starLevel": 4,
        "attributeId": 2,
        "attributeName": "热熔",
        "weaponTypeId": 3,
        "weaponTypeName": "佩枪",
        "acronym": "cx",
        "mapRoleId": None
    }
]

for data in json_data:
    role_name = data["roleName"]
    role_icon_url = data["roleIconUrl"]
    image_path = get_image(role_name, role_icon_url)
    print(f"Role Name: {role_name}")
    print(f"Image Path: {image_path}")
    print()
