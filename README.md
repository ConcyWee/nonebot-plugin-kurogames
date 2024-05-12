<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-kurogames

_✨ 一款库洛游戏数据详情 谢比螺六~ ✨_


<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/ConcyWee/nonebot-plugin-kurogames.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-kurogames">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-kurogames.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

输入命令即可查询库洛游戏数据详情
token的获取方法请自行查找呦~
token格式如下所示
![image](https://github.com/ConcyWee/nonebot-plugin-kurogames/assets/36001297/1fc32ace-cca4-4ddc-bda4-7ed4f9054848)

## ❗ 宇宙安全声明
本插件仅提供库洛游戏的账号数据查询，并不会保存您的用户名和密码，但会保存获取到的账号 token! 如果您的账号出现封禁, 被盗等处罚与本插件无关. 使用即视为您阅读并同意以上条款!

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-kurogames

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-kurogames
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-kurogames
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-kurogames
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-kurogames
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_kurogames"]

</details>

## ⚙️ 配置

插件中包含playwright，首次使用可能需手动执行 playwright install

## 📝 画饼

- [ ] 增加鸣潮游戏详情查询
- [ ] 自定义背景图片
- [ ] 战双血清回满提前提醒

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 战双登录 token | 群员 | 否 | 群聊 | 登录库街账号 |
| 战双 | 群员 | 否 | 群聊 | 获取战双当前数据 |
### 效果图
如果有效果图的话
![IMG_20240510_185129](https://github.com/ConcyWee/nonebot-plugin-kurogames/assets/36001297/f4869d8e-1e03-4ae6-b95f-632db9f521ae)
![IMG_20240510_185200](https://github.com/ConcyWee/nonebot-plugin-kurogames/assets/36001297/0ad515f3-cfc2-4ab6-a433-3056c944d754)
