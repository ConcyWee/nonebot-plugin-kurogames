import os
import json
from jinja2 import Template
from playwright.async_api import async_playwright

async def html_render(file_path, rendered_template_path, data, width, height, zoom_size):
    with open(file_path, 'r', encoding='utf-8') as file:
        template_str = file.read()
    template = Template(template_str)
    rendered_html = template.render(data)
    with open(rendered_template_path, 'w', encoding='utf-8') as file:
        file.write(rendered_html)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-gpu"])
        context = await browser.new_context()
        page = await context.new_page()

        await page.set_viewport_size({"width": width, "height": height})
        url = f'file://{os.path.abspath(rendered_template_path)}'
        await page.goto(url)
        await page.evaluate('document.body.style.zoom = "' + zoom_size + '%"')
        await page.wait_for_load_state("networkidle")
        screenshot_binary = await page.screenshot(type="png", full_page=True)
        await page.close()
        await browser.close()
    return screenshot_binary

async def mc_pic_render(data):
    max_difficulties = {}
    for challengeId, items in data['challengeInfo'].items():
        for item in items:
            if item['passTime'] != 0:
                boss_name = item['bossName']
                if boss_name not in max_difficulties or item['difficulty'] > max_difficulties[boss_name]['difficulty']:
                    max_difficulties[boss_name] = item 
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
        'challengeInfo'     : max_difficulties,
        'baseData'          : data['baseData'],
        'exploreData'       : data['exploreData'],
    }

    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    rendered_template_path = os.path.join(static_dir, 'Outputs', 'mc_rendered_template.html')
    mc_result_path = os.path.join(static_dir, 'MCResult.html')

    result = await html_render(mc_result_path, rendered_template_path, data, 1920, 1080, '500')
    return result

async def mc_explore_render(data):
    data = {
        'exploreData' : data
    }

    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    rendered_template_path = os.path.join(static_dir, 'Outputs', 'exploration_template.html')
    mc_result_path = os.path.join(static_dir, 'Exploration.html')

    result = await html_render(mc_result_path, rendered_template_path, data, 1920, 1080, '500')
    return result

async def mc_role_detail_render(data, user_data):
    chainList = 6
    data = json.loads(data)
    user_data = json.loads(user_data)
    for chain in data['chainList']:
        if  chain['unlocked'] == False:
            chainList = chain['order'] - 1
            break
    data = {
        'userName'          : user_data['name'],
        'userId'            : user_data['id'],
        'roleName'          : data['role']['roleName'],
        'rolePic'           : data['role']['rolePicUrl'],
        'starLevel'         : data['role']['starLevel'],
        'roleBreach'        : data['role']['breach'],
        'attributeName'     : data['role']['attributeName'],
        'level'             : data['level'],
        'chainList'         : chainList,
        'weaponName'        : data['weaponData']['weapon']['weaponName'],
        'weaponPic'         : data['weaponData']['weapon']['weaponIcon'],
        'weaponLevel'       : data['weaponData']['level'],
        'weaponStarLevel'   : data['weaponData']['weapon']['weaponStarLevel'],
        'weaponBreach'      : data['weaponData']['breach'],
        'weaponEffectName'  : data['weaponData']['weapon']['weaponEffectName'],
        'weaponEffectDesc'  : data['weaponData']['weapon']['effectDescription'],
        'weaponResonLevel'  : data['weaponData']['resonLevel'],
        'phantomData'       : data['phantomData']['equipPhantomList'] if data['phantomData']['cost'] != 0 else [],
        'skillList'         : data['skillList']
    }

    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    rendered_template_path = os.path.join(static_dir, 'Outputs', 'mc_role_detail_template.html')
    mc_result_path = os.path.join(static_dir, 'RoleDetail.html')
    
    result = await html_render(mc_result_path, rendered_template_path, data, 1920, 1080, '500')
    return result

async def mc_tower_render(data, user_data):
    difficultyListLen = len(data['difficultyList'])
    if difficultyListLen < 3:
        return False
    data = {
        'userName'          : user_data['name'],
        'userId'            : user_data['id'],
        'towerData'         : data['difficultyList'][3]['towerAreaList']
    }

    parent_parent_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    static_dir = os.path.join(parent_parent_dir, 'Static')
    rendered_template_path = os.path.join(static_dir, 'Outputs', 'mc_tower_detail_template.html')
    mc_result_path = os.path.join(static_dir, 'TowerDetail.html')

    result = await html_render(mc_result_path, rendered_template_path, data, 1920, 1080, '300')
    return result

