import os
async def kuro_help_pic():
    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    help_pic_path = os.path.join(static_dir, 'Pics', 'help_pics', 'HELP_PIC.png')
    with open(help_pic_path, 'rb') as file:
        help_pic = file.read()
    return help_pic

async def kuro_help_text():
    help_text = ""
    help_text += "链接1(token获取教程)：\n"
    help_text += "https://docs.qq.com/doc/DZW9SQ294SnhlbkFw\n"
    help_text += "链接2(卡池ID获取教程)：\n"
    help_text += "https://docs.qq.com/doc/DZUVHeVRHekxRbm9y\n"

    return help_text