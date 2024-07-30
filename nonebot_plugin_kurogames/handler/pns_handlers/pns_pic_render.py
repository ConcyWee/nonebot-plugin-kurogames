import os
from jinja2 import Template
from playwright.async_api import async_playwright

async def pic_generator(data):
    data = {
        'roleName'                    : data['roleName'],
        'level'                       : data['level'],
        'server'                      : data['server'],
        'roleId'                      : data['roleId'],
        'roleScore'                   : data['roleScore'],
        'roleNum'                     : data['roleNum'],
        'fashionCollectionPercent'    : data['fashionCollectionPercent'],
        'actionValue'                 : data['actionValue'],
        'actionRefreshTimeStamp'      : data['actionRefreshTimeStamp'],
        'blackCardNum'                : data['blackCardNum'],
        'developResourceNum'          : data['developResourceNum'],
        'bossRefreshTimeStamp'        : data['bossRefreshTimeStamp'],
        'bossBlackCard'               : data['bossBlackCard'],
        'transfiniteNum'              : data['transfiniteNum'],
        'transfiniteRefreshTimeStamp' : data['transfiniteRefreshTimeStamp'],
        'arenaRefreshTimeStamp'       : data['arenaRefreshTimeStamp'],
        'arenaBlackCard'              : data['arenaBlackCard'],
        'strongHoldRate'              : data['strongHoldRate'],
        'strongHoldTimeStamp'         : data['strongHoldTimeStamp'],
        'roleDevelopNum'              : data['roleDevelopNum'],
        'weaponDevelopNum'            : data['weaponDevelopNum'],
        'assistDevelopNum'            : data['assistDevelopNum'],
        'baseRoleNum'                 : data['baseRoleNum'],
        'baseWeaponNum'               : data['baseWeaponNum'],
    }


    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    rendered_template_path = os.path.join(static_dir, 'Outputs', 'rendered_template.html')
    pns_result_path = os.path.join(static_dir, 'PNSResult.html')
    
    with open(pns_result_path, 'r', encoding='utf-8') as file:
        template_str = file.read()
    template = Template(template_str)
    rendered_html = template.render(data)
    with open(rendered_template_path, 'w', encoding='utf-8') as file:
        file.write(rendered_html)

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-gpu"])
        context = await browser.new_context()
        page = await context.new_page()


        await page.set_viewport_size({"width": 1080, "height": 1920})
        url = f'file://{os.path.abspath(rendered_template_path)}'
        await page.goto(url)
        await page.wait_for_load_state("networkidle")
        screenshot_binary = await page.screenshot(type="png")
        await page.close()
        await browser.close()
    
    return screenshot_binary
