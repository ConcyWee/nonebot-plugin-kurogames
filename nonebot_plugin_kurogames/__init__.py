from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment, Message, Bot, MessageEvent

from .config import Config
from .Static.kuro_help import kuro_help
from .handler.pns_handlers.pns_data_handler import pns_data_handler
from .handler.pns_handlers.pns_login_handler import pns_login_handler, get_kuro_token
from .handler.mc_handlers.mc_data_handler import mc_data_handler

__plugin_meta__ = PluginMetadata(
    name="库洛游戏信息",
    description="一款库洛游戏角色信息插件",
    usage="发送“战双登录”注册，发送“战双”查询战双详情",
    type="application",
    homepage="https://github.com/ConcyWee/nonebot-plugin-kurogames",
    config=Config,
    supported_adapters={"nonebot.adapters.onebot.v11"},
)


punishing = on_command("pns", aliases={"战双","战双详情","zs"}, priority=5)
pns_login = on_command("pnslogin", aliases={"战双登陆","战双登录", "库洛登录", "库洛登陆", "鸣潮登录", "鸣潮登陆"}, priority=5)
pns_help  = on_command("pnshelp", aliases={"战双帮助", "库洛帮助", "鸣潮帮助"}, priority=5)
mingchao  = on_command("mc", aliases={"鸣潮", "鸣潮详情"}, priority=5)

@pns_login.handle()
async def _(bot:Bot, event: MessageEvent, arg: Message = CommandArg()):
    user_id = event.get_user_id()
    data_content = arg.extract_plain_text()
    result = await pns_login_handler(user_id, data_content)
    await pns_login.finish(result)

@punishing.handle()
async def _(bot: Bot, event: MessageEvent):
    user_id = event.get_user_id()
    data_row = await get_kuro_token(user_id)
    if data_row:
        pic_result = await pns_data_handler(data_row)
        if isinstance(pic_result, str):
            await punishing.finish(MessageSegment.at(user_id) + MessageSegment(pic_result))
        await punishing.finish(MessageSegment.image(pic_result))
    else:
        await punishing.finish("请先输入token")

@pns_help.handle()
async def _():
    help_datail = await kuro_help()
    await pns_help.finish(help_datail)

@mingchao.handle()
async def _(bot: Bot, event: MessageEvent):
    user_id = event.get_user_id()
    data_row = await get_kuro_token(user_id)
    if data_row:
        pic_result = await mc_data_handler(data_row)
        if isinstance(pic_result, str):
            await mingchao.finish(MessageSegment.at(user_id) + MessageSegment(pic_result))
        await mingchao.finish(MessageSegment.image(pic_result))
    else:
        await mingchao.finish("请先输入token")