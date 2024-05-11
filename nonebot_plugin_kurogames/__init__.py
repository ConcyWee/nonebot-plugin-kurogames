from nonebot import on_command
from nonebot.plugin import PluginMetadata
from nonebot.adapters import Event, Message
from nonebot.params import CommandArg
from .handler.pns_handlers.pns_data_handler import pns_data_handler
from .handler.pns_handlers.pns_login_handler import pns_login_handler, get_kuro_token
from nonebot.adapters.onebot.v11 import MessageSegment


plugin_meta = PluginMetadata(
    name="库洛游戏信息",
    description="一款库洛游戏角色信息插件",
    usage="发送“战双登录”",
    type="application",
    homepage="https://github.com/ConcyWee/nonebot-plugin-kurogames",
    config=None,
    supported_adapters=None
)


punishing = on_command("pns", aliases={"战双","战双详情"}, priority=5)
pns_login = on_command("pnslogin", aliases={"战双登陆","战双登录"}, priority=5)


@pns_login.handle()
async def _(event: Event, arg: Message = CommandArg()):
    user_id = event.get_user_id()
    data_content = arg.extract_plain_text()
    result = pns_login_handler(user_id, data_content)
    await pns_login.finish(result)

@punishing.handle()
async def _(event: Event):
    user_id = event.get_user_id()
    data_row = get_kuro_token(user_id)
    if data_row:
        pic_result = await pns_data_handler(data_row)
        await punishing.finish(MessageSegment.image(pic_result))
    else:
        await punishing.finish("请先输入token")