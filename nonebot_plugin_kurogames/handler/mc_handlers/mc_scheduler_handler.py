from nonebot import require

require("nonebot_plugin_apscheduler")

from nonebot_plugin_apscheduler import scheduler

def run_every_day(arg1: int, arg2: int):
    pass

scheduler.add_job(
    run_every_day, "interval", days=1, id="job_1", args=[1], arg2=[2]
)