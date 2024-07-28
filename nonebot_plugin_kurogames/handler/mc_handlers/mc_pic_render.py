import os
from jinja2 import Template
from playwright.async_api import async_playwright

async def mc_pic_render(data):
    data = {
        'roleName'          : data['roleName'],
        'roleId'            : data['roleId'],
        'serverName'        : data['serverName'],
        'energyData'        : data['energyData'],
        'livenessData'      : data['livenessData'],
        'battlePassData'    : data['battlePassData'],
        'refreshTime'       : data['refreshTime'],
        'roleList'          : data['roleList'],
        'calabashLevel'     : data['calabashLevel'],
        'baseCatch'         : data['baseCatch'],
        'strengthenCatch'   : data['strengthenCatch'],
        'catchQuality'      : data['catchQuality'],
        'cost'              : data['cost'],
        'maxCount'          : data['maxCount'],
        'unlockCount'       : data['unlockCount'],
        'phantomList'       : data['phantomList'],
        'challengeList'     : data['challengeList'],
        'baseData'          : data['baseData'],
        'exploreData'       : data['exploreData'],
    }

    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    rendered_template_path = os.path.join(static_dir, 'Outputs', 'mc_rendered_template.html')
    mc_result_path = os.path.join(static_dir, 'MCResult.html')

    with open(mc_result_path, 'r', encoding='utf-8') as file:
        template_str = file.read()
    template = Template(template_str)
    rendered_html = template.render(data)
    with open(rendered_template_path, 'w', encoding='utf-8') as file:
        file.write(rendered_html)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-gpu"])
        context = await browser.new_context()
        page = await context.new_page()

        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto(rendered_template_path)
        await page.evaluate('document.body.style.zoom = "500%"')
        await page.wait_for_load_state("networkidle")
        screenshot_binary = await page.screenshot(type="png", full_page=True)
        await page.close()
        await browser.close()

    return screenshot_binary

async def mc_explore_render(data):
    data = {
        'exploreData' : data,
    }

    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    rendered_template_path = os.path.join(static_dir, 'Outputs', 'exploration_template.html')
    mc_result_path = os.path.join(static_dir, 'Exploration.html')

    with open(mc_result_path, 'r', encoding='utf-8') as file:
        template_str = file.read()
    template = Template(template_str)
    rendered_html = template.render(data)
    with open(rendered_template_path, 'w', encoding='utf-8') as file:
        file.write(rendered_html)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-gpu"])
        context = await browser.new_context()
        page = await context.new_page()

        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto(rendered_template_path)
        await page.evaluate('document.body.style.zoom = "500%"')
        await page.wait_for_load_state("networkidle")
        screenshot_binary = await page.screenshot(type="png", full_page=True)
        await page.close()
        await browser.close()

    return screenshot_binary