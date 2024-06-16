from nonebot import require
require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler

KURO_SIGN_IN = 1
PNS_ENERGY   = 2
MC_ENERGY    = 3
async def create_scheduler(user_id, group_id, scheduler_type, trigger_time):
    if scheduler_type == KURO_SIGN_IN:
        scheduler.add_job('run_every_day', "cron", hour=trigger_time, args=[user_id, group_id])
    elif scheduler_type == PNS_ENERGY:
        scheduler.add_job('run_every_day', "cron", hour=trigger_time, args=[user_id, group_id])
    return True