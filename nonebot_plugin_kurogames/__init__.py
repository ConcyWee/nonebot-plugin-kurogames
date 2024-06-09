from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment, Message, Bot, MessageEvent

import json
from .config import Config
from .Static.kuro_help import kuro_help
from .handler.pns_handlers.pns_data_handler import pns_data_handler
from .handler.pns_handlers.pns_login_handler import pns_login_handler, get_kuro_token
from .handler.pns_handlers.pns_detail_handler import kuro_sdk_login
from .handler.mc_handlers.mc_data_handler import mc_data_handler
from .handler.bbs_handlers.bbs_data_handler import daily_task

__plugin_meta__ = PluginMetadata(
    name="库洛游戏信息",
    description="一款库洛游戏角色信息插件",
    usage="发送“战双登录”注册，发送“战双”查询战双详情",
    type="application",
    homepage="https://github.com/ConcyWee/nonebot-plugin-kurogames",
    config=Config,
    supported_adapters={"nonebot.adapters.onebot.v11"},
)


punishing  = on_command("zssj", aliases={"战双详情", "zsxq", "我的战双卡片", "战双数据"}, priority=5)
pns_login  = on_command("pnslogin", aliases={"战双登陆","战双登录", "库洛登录", "库洛登陆", "鸣潮登录", "鸣潮登陆"}, priority=5)
pns_help   = on_command("pnshelp", aliases={"战双帮助", "库洛帮助", "鸣潮帮助"}, priority=5)
mingchao   = on_command("mcsj", aliases={"鸣潮详情", "mcxq", "我的鸣潮卡片", "鸣潮数据"}, priority=5)
kuro_daily = on_command("库洛签到", aliases={"战双签到", "鸣潮签到", "库街区每日", "库洛每日", "库街区签到"}, priority=5)

@pns_login.handle()
async def _(bot:Bot, event: MessageEvent, arg: Message = CommandArg()):
    user_id = event.get_user_id()
    data_content = arg.extract_plain_text()
    if data_content[0].isdigit() and data_content[-1].isdigit():
        data_content = await kuro_sdk_login(data_content.split(' ')[0], data_content.split(' ')[1])
        if isinstance(data_content, dict):
            data_content = json.dumps(data_content)
        else:
            await pns_login.finish(data_content)
    result = await pns_login_handler(user_id, data_content)
    await pns_login.finish(result)

@punishing.handle()
async def _(bot: Bot, event: MessageEvent):
    user_id = event.get_user_id()
    data_row = await get_kuro_token(user_id)
    if data_row:
        pic_result = await pns_data_handler(data_row)
        if isinstance(pic_result, str):
            await punishing.finish(MessageSegment.text(pic_result))
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
            await mingchao.finish(MessageSegment.text(pic_result))
        await mingchao.finish(MessageSegment.image(pic_result))
    else:
        await mingchao.finish("请先输入token")

@kuro_daily.handle()
async def _(bot: Bot, event: MessageEvent):
    user_id = event.get_user_id()
    data_row = await get_kuro_token(user_id)
    if data_row:
        daily_result = await daily_task(user_id, data_row)
        await kuro_daily.finish(MessageSegment.text(daily_result))
    else:
        await kuro_daily.finish("请先输入token")