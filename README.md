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
所需的token须为库街区app获取，网页的token不可以哦~  
可以用抓包软件抓取sdkLogin的包，具体获取方法请参考文档：https://docs.qq.com/doc/DZW9SQ294SnhlbkFw  
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
| 配置项 | 必填 | 说明 |
|:-----:|:----:|:----:|
| kuro_db_path | 否 | 配置数据库路径，例如 "D:\kurogames"(如不填写则默认保存位置为/data/kurogames) |

## 📝 画饼

- [x] 增加鸣潮游戏详情查询
- [x] 增加短信登录功能
- [x] 库街区签到
- [x] 增加鸣潮查询指定人的数据
- [x] 增加鸣潮抽卡数据分析
- [x] 增加鸣潮地图探索进度查询
- [x] 增加鸣潮角色详情查询
- [x] 增加逆境深塔挑战详情查询
- [ ] 自定义背景图片
- [ ] 战双以及鸣潮体力回满提前提醒（搁置好久了）

## 🎉 使用

### 指令表

| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| 库洛登录 token | 群员 | 否 | 群聊 | 登录库街区账号 |
| 库洛登录 验证码 | 群员 | 否 | 群聊 | 登录库街区账号 |
| 库洛签到 | 群员 | 否 | 群聊 | 完成库街区每日任务以及游戏签到 |
| 战双数据 | 群员 | 否 | 群聊 | 获取战双当前数据 |
| 鸣潮数据 | 群员 | 否 | 群聊 | 获取鸣潮当前数据 |
| 鸣潮探索数据 | 群员 | 否 | 群聊 | 获取鸣潮当前地图探索进度 |
| 鸣潮角色详情 角色名 | 群员 | 否 | 群聊 | 查看指定角色的装备详情 |
| 逆境深塔详情 | 群员 | 否 | 群聊 | 查询逆境深塔数据详情 |
| 库洛帮助 | 群员 | 否 | 群聊 | 查看本插件使用帮助 |

### 效果图

#### 战双：
<details>
  
![IMG_20240610_204654](https://github.com/ConcyWee/nonebot-plugin-kurogames/assets/36001297/91b9203c-18a4-4e65-bd29-dde8ff901356)

![a983f0b88c19bfb57ab2c948bd73e80a](https://github.com/user-attachments/assets/1c1845f6-304a-41bb-a6c8-ad200727bc32)

</details>

#### 鸣潮：
<details>
  
![199342ecfe749534ba395f712f739da1](https://github.com/user-attachments/assets/e80c70cd-35d4-40cc-9033-5e8e149b4ab5)

![1717680630759](https://github.com/ConcyWee/nonebot-plugin-kurogames/assets/36001297/ae3c91f5-a87f-4521-9ada-ea804d9834df)

</details>

## 🦜 更新日志

### 2025.01.14

- 修复鸣潮探索数据不更新的问题

### 2025.01.12（加更）

- 修改了部分接口地址，预计库洛过不久也会改过去（）
- 增加了查询他人鸣潮角色数据和深塔数据的功能
- 优化了部分提示语

### 2025.01.12

- 修复由于库洛又双叒叕更改接口地址带来的报错（懒得喷了，累了）
- 由于探索数据图片过大，导致无法发送，现将鸣潮探索数据拆分为按地区名查询，例如：/鸣潮探索数据 黎那汐塔

### 2024.12.12 (紧急修复)

- 紧急修复上一版代码忘了修改的地方（我是大笨蛋😭）

### 2024.12.12

- 修复鸣潮角色数据当角色未穿戴声骸时会报错的异常
- 修复战双数据获取角色等级时报错的异常
- 上述两个都是因为沟槽的库洛又双叒叕改接口和数据格式！阿！米！诺！斯！
- 战双战斗相关的接口地址更改了，下个版本将会更改部分接口地址

### 2024.11.29

- 修复鸣潮探索数据

### 2024.11.26

- 增加鸣潮数据解密，修复部分问题（不是库洛，你要干什么，这玩意加密干啥啊，阿米诺斯😡😡😡😡😡）
- 抱歉各位，最近几个月太忙了，一直没时间更新代码，但是没有跑路😶‍🌫️
- 探索数据将在下次更新时修复，欢迎各位入群催更（）

### 2024.09.03

- 修复鸣潮逆境深塔以及角色详情数据不刷新的问题（沟槽的库洛这个也要refresh是吧😡👊）

### 2024.09.02

- 新增鸣潮逆境深塔挑战详情查询功能

### 2024.08.31

- 新增鸣潮角色详情查询功能
- 修复历史代码中的隐藏bug（目前应该没人发现过，但是我也不打算说，因为这错误太蠢了🧐）

### 2024.08.13

- 修复由于库洛更新数据内容以及格式造成的数据缺失和运行报错（沟槽的库洛你没事改什么数据格式和内容！😡👊）

### 2024.07.30

- 战双数据查询新增战双研发券详情

### 2024.07.28

- 修复文件名大小写原因导致结果生成失败的问题
- 修复由于路径硬编码导致的Linux下生成图片失败的问题

### 2024.07.10

- 增加鸣潮地图探索数据查询
- 修复未抽取到五星时无回复的问题

### 2024.07.07

- 增加鸣潮抽卡数据欧非分析功能

### 2024.06.30

- 修复鸣潮抽卡数据分析功能，在重复抽取时，数据不准确的问题

### 2024.06.29

- 修复角色“今汐”排版异常的问题（沟槽的库洛图片大小不统一😡👊）
- 修复发送“鸣潮抽卡详情”指令后查询鸣潮数据出现“还没有设置鸣潮角色”的问题

### 2024.06.16

- 新增查询指定人的鸣潮数据
- 新增抽卡数据查询

### 2024.06.10

- 新增短信登录功能
- 新增库街区签到功能

### 2024.06.07

- 修复无游戏角色时崩溃的bug
- 增加鸣潮体力回满时间

### 2024.06.06

- 增加鸣潮数据查询

## 🐧 写在最后

欢迎加入用户交流群~
https://qm.qq.com/q/qSclXekdH4
![qrcode_1724496065359](https://github.com/user-attachments/assets/592ccd28-a92c-4069-9b89-a74b227bb796)
