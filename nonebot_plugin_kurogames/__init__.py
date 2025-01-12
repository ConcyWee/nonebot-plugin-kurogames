from nonebot import on_command
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.adapters.onebot.v11 import MessageSegment, Message, Bot, MessageEvent

import json
from .config import Config
from .Static.kuro_help import *
from .handler.pns_handlers.pns_data_handler import pns_data_handler
from .handler.pns_handlers.pns_login_handler import pns_login_handler, get_kuro_token
from .handler.pns_handlers.pns_detail_handler import kuro_sdk_login
from .handler.mc_handlers.mc_data_handler import *
from .handler.bbs_handlers.bbs_data_handler import daily_task
from .handler.mc_handlers.mc_gacha_login_handler import *
from .handler.mc_handlers.mc_gacha_handler import gacha_analysis

__plugin_meta__ = PluginMetadata(
    name="库洛游戏信息",
    description="一款库洛游戏角色信息插件",
    usage="发送“战双登录”注册，发送“战双”查询战双详情",
    type="application",
    homepage="https://github.com/ConcyWee/nonebot-plugin-kurogames",
    config=Config,
    supported_adapters={"nonebot.adapters.onebot.v11"},
)


punishing      = on_command("zssj",         aliases={"战双详情", "zsxq", "我的战双卡片", "战双数据"}, priority=5)
kuro_login     = on_command("pnslogin",     aliases={"战双登陆","战双登录", "库洛登录", "库洛登陆", "鸣潮登录", "鸣潮登陆"}, priority=5)
pns_help       = on_command("pnshelp",      aliases={"战双帮助", "库洛帮助", "鸣潮帮助"}, priority=5)
mingchao       = on_command("mcsj",         aliases={"鸣潮详情", "mcxq", "我的鸣潮卡片", "鸣潮数据"}, priority=5)
kuro_daily     = on_command("库洛签到",      aliases={"战双签到", "鸣潮签到", "库街区每日", "库洛每日", "库街区签到"}, priority=5)
mc_gacha       = on_command("鸣潮抽卡分析",  aliases={"鸣潮抽卡记录", "鸣潮抽卡历史", "鸣潮抽卡详情", "鸣潮抽卡数据"}, priority=5)
mc_gacha_login = on_command("鸣潮数据码录入", aliases={"鸣潮抽卡录入", "鸣潮抽卡登陆", "鸣潮抽卡登录"}, priority=5)
mc_explore     = on_command("鸣潮探索数据",   aliases={"鸣潮探索详情", "鸣潮地图数据", "鸣潮地图详情", "鸣潮探索进度"}, priority=5)
mc_role_detail = on_command("鸣潮角色面板",   aliases={"鸣潮角色详情", "鸣潮角色数据"}, priority=5)
mc_tower_detail= on_command("鸣潮深渊详情",  aliases={"鸣潮深渊数据", "逆境深塔详情", "逆境深塔数据", "鸣潮逆境深塔详情", "鸣潮逆境深塔数据"}, priority=5)

@kuro_login.handle()
async def _(bot:Bot, event: MessageEvent, arg: Message = CommandArg()):
    user_id = event.get_user_id()
    data_content = arg.extract_plain_text()
    if data_content:
        if data_content[0].isdigit() and data_content[-1].isdigit():
            data_content = await kuro_sdk_login(data_content.split(' ')[0], data_content.split(' ')[1])
            if isinstance(data_content, dict):
                data_content = json.dumps(data_content)
            else:
                await kuro_login.finish(data_content)
        result = await pns_login_handler(user_id, data_content)
    else:
        result = "请输入token"
    await kuro_login.finish(result)

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
    help_pic = await kuro_help_pic()
    help_txt = await kuro_help_text()
    await pns_help.finish(MessageSegment.image(help_pic) + MessageSegment.text(help_txt))

@mingchao.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    user_id = event.get_user_id()
    if args:
        for arg in args:
            if arg.type == "at":
                user_id = arg.data.get("qq", "")
    data_row = await get_kuro_token(user_id)
    if data_row:
        pic_result = await mc_data_handler(data_row)
        if isinstance(pic_result, str):
            await mingchao.finish(MessageSegment.text(pic_result))
        await mingchao.finish(MessageSegment.image(pic_result))
    else:
        await mingchao.finish("当前用户信息未录入，请先录入token")

@kuro_daily.handle()
async def _(bot: Bot, event: MessageEvent):
    user_id = event.get_user_id()
    data_row = await get_kuro_token(user_id)
    if data_row:
        daily_result = await daily_task(user_id, data_row)
        await kuro_daily.finish(MessageSegment.text(daily_result))
    else:
        await kuro_daily.finish("当前用户信息未录入，请先录入token")

@mc_gacha_login.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    qq_id = event.get_user_id()
    gacha_id = args.extract_plain_text()
    result = await mc_gacha_login_handler(qq_id, gacha_id)
    await mc_gacha_login.finish(result)

@mc_gacha.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    qq_id = event.get_user_id()
    if args:
        for arg in args:
            if arg.type == "at":
                qq_id = arg.data.get("qq", "")
            else:
                gacha_type = args.extract_plain_text().strip()
    if gacha_type in ["角色常驻", "武器常驻", "角色up", "武器up", "新手池", "新手自选池"]:
        result = await gacha_analysis(qq_id, gacha_type)
    else:
        await mc_gacha.finish("请输入正确的抽卡类型\n角色常驻, 武器常驻, 角色up, 武器up, 新手池, 新手自选池")
    await mc_gacha.finish(result)

@mc_explore.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    user_id = event.get_user_id()
    if args:
        for arg in args:
            if arg.type == "at":
                user_id = arg.data.get("qq", "")
            elif args.extract_plain_text():
                area_name = args.extract_plain_text()
    else:
        await mc_explore.finish("请输入地区名称，例如：/鸣潮探索数据 黎那汐塔")
                
    data_row = await get_kuro_token(user_id)
    if data_row:
        pic_result = await mc_explore_detail_handler(data_row, area_name)
        if isinstance(pic_result, str):
            await mc_explore.finish(MessageSegment.text(pic_result))
        await mc_explore.finish(MessageSegment.image(pic_result))
    else:
        await mc_explore.finish("当前用户信息未录入，请先录入token")

@mc_role_detail.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    user_id = event.get_user_id()
    if args:
        for arg in args:
            if arg.type == "at":
                user_id = arg.data.get("qq", "")
    data_row = await get_kuro_token(user_id)
    if data_row:
        if args:
            role_name = args.extract_plain_text()
            pic_result = await mc_role_detail_handler(data_row, role_name)
        else:
            await mc_role_detail.finish("请输入要查询的角色，例如：/鸣潮角色数据 长离")
        if isinstance(pic_result, str):
            await mc_role_detail.finish(MessageSegment.text(pic_result))
        else:
            await mc_role_detail.finish(MessageSegment.image(pic_result))
    else:
        await mc_role_detail.finish("当前用户信息未录入，请先录入token")

@mc_tower_detail.handle()
async def _(bot: Bot, event: MessageEvent, args: Message = CommandArg()):
    user_id = event.get_user_id()
    if args:
        for arg in args:
            if arg.type == "at":
                user_id = arg.data.get("qq", "")
    data_row = await get_kuro_token(user_id)
    if data_row:
        result = await mc_tower_detail_handler(data_row)
        if isinstance(result, str):
           await mc_tower_detail.finish(MessageSegment.text(result))
        else:
           await mc_tower_detail.finish(MessageSegment.image(result))
    else:
        await mc_tower_detail.finish("请先输入token")