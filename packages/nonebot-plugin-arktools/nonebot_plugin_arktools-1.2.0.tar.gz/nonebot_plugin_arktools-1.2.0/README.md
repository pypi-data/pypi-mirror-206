<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">
  
# Nonebot_Plugin_ArkTools
  
_✨ 基于 OneBot 适配器的 [NoneBot2](https://v2.nonebot.dev/) 明日方舟小工具箱插件 ✨_
  
</div>

[![OSCS Status](https://www.oscs1024.com/platform/badge/NumberSir/nonebot_plugin_arktools.svg?size=small)](https://www.oscs1024.com/project/NumberSir/nonebot_plugin_arktools?ref=badge_small)  [![star](https://gitee.com/Number_Sir/nonebot_plugin_arktools/badge/star.svg?theme=white)](https://gitee.com/Number_Sir/nonebot_plugin_arktools/stargazers)

本人python小萌新，插件有不完善和可以改进之处欢迎各位多提pr和issue

- [功能](#功能)
- [安装](#安装)
- [使用](#如何使用)
- [示例](#图片示例)
- [感谢](#感谢)
- [更新日志](#更新日志)

# 功能
## 已实现：
1. [x] 可以查询推荐的公招标签(截图识别/手动输文字)
2. [x] 可以查询干员的技能升级材料、专精材料、精英化材料、模组升级材料
3. [x] 可以通过网易云点歌，以卡片形式发送
4. [x] 猜干员小游戏，玩法与 [wordle](https://github.com/noneplugin/nonebot-plugin-wordle) 相同
5. [x] 可以查看生日为今天的干员
6. [x] 可以记录当前理智，等回复满后提醒
7. [x] 指定群聊自动推送最新游戏公告
8. [x] 查询、订阅、推送 [MAA 作业站](https://prts.plus)的作业

## 编写中...
1. [ ] 可以查询某种资源在哪个关卡期望理智最低
2. [ ] 根据当前有的资源和需要的资源种类、数量测算最优推图计划
3. [ ] 查询某干员的基础数据：
   1. [ ] 给定等级、信赖、潜能下的基础面板
   2. [ ] 天赋、特性、技能
   3. [ ] 干员种族、势力、身高等基本个人信息
4. [ ] 定时提醒剿灭 / 蚀刻章 / 合约等活动过期

# 安装
- 使用 pip
```
pip install -U nonebot_plugin_arktools
```

- 使用 nb-cli
```
nb plugin install nonebot_plugin_arktools
```

# 如何使用
## 启动注意
 - 每次启动并连接到客户端后会从 __[明日方舟常用素材库](https://github.com/yuanyan3060/Arknights-Bot-Resource)__(__[yuanyan3060](https://github.com/yuanyan3060)__), __[《明日方舟》游戏数据库](https://github.com/Kengxxiao/ArknightsGameData)__(__[Kengxxiao](https://github.com/Kengxxiao)__), __[Arknight-Images](https://github.com/Aceship/Arknight-Images)__(__[Aceship](https://github.com/Aceship)__) 下载使用插件必需的文本及图片资源到本地，已经下载过的文件不会重复下载。下载根据网络情况不同可能耗时 5 分钟左右
 - 如需手动更新，请用命令 __“更新方舟素材”__ 进行更新
 - 如果自动下载失败，请手动下载发行版中的 __“`data.zip`”/“`data.tar.gz`”__ 压缩文件，解压到 “`机器人根目录`” 文件夹下(即运行 `nb run` 命令的文件夹/ `bot.py` 的文件夹)。正确放置的文件夹结构应为：
```txt
举例：
├── data
│   └── arktools
│       ├── arknights
│       │   ├── gamedata
│       │   │   └── excel
│       │   │       └── ...
│       │   ├── gameimage
│       │   │   └── ...
│       │   ├── processed_data
│       │   │   └── nicknames.json
│       │   └── ...
│       ├── fonts
│       │   ├── Arknights-en.ttf
│       │   └── Arknights-zh.otf
│       ├── guess_character
│       │   ├── correct.png
│       │   ├── down.png
│       │   ├── up.png
│       │   ├── vague.png
│       │   └── wrong.png
│       └── ...
├── plugin
│   └── nonebot_plugin_arktools
│       ├── src
│       └── ...
├── .env
├── .env.dev
├── .env.prod
...
```

## .env.env 配置项

```ini
# 百度 OCR 配置，公招识别截图用
# 具体见 https://console.bce.baidu.com/ai/?fromai=1#/ai/ocr/app/list
ARKNIGHTS_BAIDU_API_KEY="xxx"    # 【必填】百度 OCR API KEY
ARKNIGHTS_BAIDU_SECRET_KEY="xxx"   # 【必填】百度 OCR SECRET KEY

# 代理配置，如部署机器人的服务器在国内大陆地区可能需要修改
GITHUB_RAW="https://raw.githubusercontent.com"   # 默认为 https://raw.githubusercontent.com，如有镜像源可以替换，如 https://ghproxy.com/https://raw.githubusercontent.com
GITHUB_SITE="https://github.com"  # 默认为 https://github.com，如有镜像源可以替换，如 https://kgithub.com
RSS_SITE="https://rsshub.app"  # 默认为 https://rsshub.app，如有镜像源可以替换

# 定时任务配置，默认是关闭的
ANNOUNCE_PUSH_SWITCH=False  # 是否自动推送舟舟最新公告，默认为 False; True 为开启自动检测
ANNOUNCE_PUSH_INTERVAL=1  # 自动推送最新公告的检测间隔，上述开关开启时有效，默认为 1 分钟
SANITY_NOTIFY_SWITCH=False  # 是否自动检测理智提醒，默认为 False; True 为开启自动检测
SANITY_NOTIFY_INTERVAL=10  # 自动检测理智提醒的检测间隔，上述开关开启时有效，默认为 10 分钟
MAA_COPILOT_SWITCH=False  # 是否自动推送MAA作业站新作业，默认为 False; True 为开启自动检测
MAA_COPILOT_INTERVAL=60  # 自动推送MAA作业站新作业的检测间隔，上述开关开启时有效，默认为 60 分钟

# 启动前素材检查配置，默认是开启的
ARKNIGHTS_UPDATE_CHECK_SWITCH=True  # 是否在启动bot时检查素材版本并下载，默认为True; False 为禁用检查

# 资源路径配置，默认在启动机器人的目录中/运行nb run的目录中/放bot.py的目录中
ARKNIGHTS_DATA_PATH="data/arktools"                                   # 资源根路径，如果修改了根路径，下方路径都要修改
ARKNIGHTS_FONT_PATH="data/arktools/fonts"                             # 字体路径
ARKNIGHTS_GAMEDATA_PATH="data/arktools/arknights/gamedata"            # 游戏数据
ARKNIGHTS_GAMEIMAGE_PATH="data/arktools/arknights/gameimage"          # 游戏图像
ARKNIGHTS_DB_URL="data/arktools/databases/arknights_sqlite.sqlite3"   # 数据库

...
```
各配置项的含义如上。
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/219335891-37933d79-1b52-4452-8959-04861087f4e8.png" width="700" />
</div>


## 干员昵称
位置默认在 `data/arknights/processed_data/nicknames.json` 键为干员中文名称，值为昵称，可自行修改。

## 指令
<details>
<summary>点击展开</summary>

### 详细指令
使用以下指令触发，需加上指令前缀
```text
格式：
指令 => 含义
[] 代表参数
xxx/yyy 代表 xxx 或 yyy
```
杂项
```text
方舟帮助 / arkhelp   => 查看指令列表
更新方舟素材          => 手动更新游戏数据(json)与图片
更新方舟数据库        => 手动更新数据库
更新方舟数据库 -D     => 删除原数据库各表并重新写入
```
猜干员
```text
猜干员    => 开始新游戏
#[干员名] => 猜干员，如：#艾雅法拉
提示      => 查看答案干员的信息
结束      => 结束当前局游戏
```
今日干员
```text
今日干员 => 查看今天过生日的干员
```
塞壬点歌
```text
塞壬点歌 [关键字] => 网易云点歌，以卡片形式发到群内
```
干员信息
```text
干员 [干员名] => 查看干员的精英化、技能升级、技能专精、模组解锁需要的材料
```
公开招募
```text
公招 [公招界面截图]          => 查看标签组合及可能出现的干员
回复截图：公招               => 同上
公招 [标签1] [标签2] ...    => 同上
```
理智提醒
```text
理智提醒                    => 默认记当前理智为0，回满到135时提醒"
理智提醒 [当前理智] [回满理智] => 同上，不过手动指定当前理智与回满理智"
理智查看                    => 查看距离理智回满还有多久，以及当期理智为多少"
```
公告推送
```text
添加方舟推送群 / ADDGROUP   => 添加自动推送的群号
删除方舟推送群 / DELGROUP   => 删除自动推送的群号
查看方舟推送群 / GETGROUP   => 查看自动推送的群号
```
MAA 作业站相关
```text
maa添加订阅 / ADDMAA [关键词1 关键词2 ...]  => 添加自动推送的关键词
maa删除订阅 / DELMAA [关键词1 关键词2 ...]  => 删除自动推送的关键词
maa查看订阅 / GETMAA                      => 查看本群自动推送的关键词

maa查作业 [关键词1 关键词2 ...]                   => 按关键词组合查作业，默认为最新发布的第一个作业
maa查作业 [关键词1 关键词2 ...] | [热度/最新/访问]  => 同上，不过可以指定按什么顺序查询
```
</details>

# 图片示例
<details>
<summary>点击展开</summary>

## 图片们
<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328291-2324ea20-74c4-4182-81ed-4b74950c3ef9.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328307-f71e08ff-2370-4fb9-8898-c76f7e06a168.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328316-9259d9e6-6c2f-40e9-87bd-cee68da240e2.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328320-9ee76c53-dcf2-4245-b302-ea1df7927772.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328326-0fc07fc7-0aa9-42b9-83e1-6eb490f4cff2.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328333-770d08e6-76c6-4087-9d62-75e302ca5f66.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328340-ce4ade0d-d00d-4520-8632-544940a1cc96.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328344-2b9b0cda-3894-451b-9ea0-d7aeec7d200c.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328356-a8a511c4-fa62-481b-af92-71052a087670.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/218328361-95ae9117-cd5e-4295-982c-9498e0b880fb.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/232200400-43d46da2-09a7-4e89-9cd0-dacc2cfe3c9c.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/232200403-275f5ef9-bcd3-4bd3-9aa5-3429bb0ecff9.png" width="500" />
</div>

<div align="left">
  <img src="https://user-images.githubusercontent.com/52584526/232200407-b689d0af-e764-4254-9689-f871af80b079.png" width="500" />
</div>
</details>


# 感谢
 - __[yuanyan3060](https://github.com/yuanyan3060)__ 的 __[明日方舟常用素材库](https://github.com/yuanyan3060/Arknights-Bot-Resource)__
 - __[Aceship](https://github.com/Aceship)__ 的 __[Arknight-Images](https://github.com/Aceship/Arknight-Images)__
 - __[AmiyaBot](https://github.com/AmiyaBot)__ 的 __[Amiya-bot](https://github.com/AmiyaBot/Amiya-Bot)__
 - __[Strelizia02](https://github.com/Strelizia02)__ 的 __[AngelinaBot](https://github.com/Strelizia02/AngelinaBot)__
 - __[MaaAssistantArknights](https://github.com/MaaAssistantArknights)__ 的 __[MAA](https://github.com/MaaAssistantArknights/MaaAssistantArknights)__

# 更新日志
<details>
<summary>点击展开</summary>

> 2023-05-04 v1.2.0
> - 更换数据源 [@issue/42](https://github.com/NumberSir/nonebot_plugin_arktools/issues/42)
> - 更新数据键值对
> - 修复了使用 `ghproxy` 作为 github 镜像时无法获取数据的问题
> - 添加了删表重写功能
> - 修复了从 maa 作业站自动推送作业出错的问题
> 
> 2023-04-15 v1.1.0
> - 公招查询、猜干员、理智提醒现在均可以私聊进行 (不推荐，私聊发消息可能导致风控)
> - 简易修复了与其它同用 Tortoise-ORM 的插件初始化冲突的问题 [@zx-issue/15](https://github.com/NumberSir/zhenxun_arktools/issues/15)
> - 添加在群聊查询、订阅、推送 [MAA 作业站](https://prts.plus)作业的功能
> - 修复了更新数据库中某张表格时会删除所有表格的问题
> 
> 2023-04-08 v1.0.20
> - 修复因素材库更新滞后导致无法查看干员的问题
> 
> 2023-04-07 v1.0.19
> - 修复更新数据库命令不会强制覆盖更新的问题
> 
> 2023-04-06 v1.0.18
> - 修复了舟舟更新数据结构导致的创建表单错误
>
> 2023-04-04 v1.0.17
> - 添加数据库初始化检查，不再每次启动bot时重复创建
> - 添加每次启动 bot 时的数据更新检查开关，默认启用 [@issue/39](https://github.com/NumberSir/nonebot_plugin_arktools/issues/39)
>
> 2023-03-28 v1.0.15
> - 猜干员与干员信息功能可以使用干员昵称(可自行增删改查)
> 
> 2023-03-24 v1.0.14
> - 修复阿米娅与近卫阿米娅冲突的问题 [@zx-issue/13](https://github.com/NumberSir/zhenxun_arktools/issues/13)
> 
> 2023-03-08 v1.0.12
> - 添加 rsshub 代理配置项 [@issue/34](https://github.com/NumberSir/nonebot_plugin_arktools/issues/34)
> - 修复公招命令不处理的问题 [@issue/35](https://github.com/NumberSir/nonebot_plugin_arktools/issues/35)
> - 添加方舟素材/资源路径配置项，现在默认在机器人根目录下 `data/arktools` 文件夹 [@issue/36](https://github.com/NumberSir/nonebot_plugin_arktools/issues/36)
> - 修复查询暮落干员信息时会选中空白暮落的问题
> 
> 2023-02-20 v1.0.11
> - 修复最新版本检测出错的问题
> 
> 2023-02-19 v1.0.9
> - 添加定时任务配置项
> - 修复定时任务导致其它处理器阻塞的问题 [@issue/30](https://github.com/NumberSir/nonebot_plugin_arktools/issues/30) [@zx-issue/9](https://github.com/NumberSir/zhenxun_arktools/issues/9)
> - 修复猜干员无法判断重复猜的问题 [@zx-issue/10](https://github.com/NumberSir/zhenxun_arktools/issues/10)
> - 修复猜干员结果图不按顺序绘制的问题
>
> 2023-02-16 v1.0.8
> - 移除 `nb plugin install` 安装命令，无法识别最新版本号 [@issue/28](https://github.com/NumberSir/nonebot_plugin_arktools/issues/28)
> - 修改百度 OCR 配置项名称 [@issue/29](https://github.com/NumberSir/nonebot_plugin_arktools/issues/29)
> - 修复资源下载与数据库初始化顺序不一致的问题
> - 补充更多错误提示信息
> 
> 2023-02-15 v1.0.7
> - 添加自动推送最新公告功能 [@issue/10](https://github.com/NumberSir/nonebot_plugin_arktools/issues/10)
> - 修复最新图像资源落后版本的问题
> - 修复启动 nonebot 时不检查素材最新版本的问题
> 
> 2023-02-13 v1.0.6
> - 添加请求素材时的错误反馈
> 
> 2023-02-13 v1.0.5
> - 可替换 github 镜像源，原先的 kgithub.com 可能出现无法请求的问题[@issue/26](https://github.com/NumberSir/nonebot_plugin_arktools/issues/26)
>
> 2023-02-13 v1.0.3
> - 重构插件目录结构
> - 优化原有功能实现：干员信息、公招查询、理智提醒、塞壬点歌 [@issue/19](https://github.com/NumberSir/nonebot_plugin_arktools/issues/19) [@issue/21](https://github.com/NumberSir/nonebot_plugin_arktools/issues/21)
>   - 公招查询的截图识别改为 [百度 OCR](https://ai.baidu.com/tech/ocr) (腾讯 OCR 太拉了，识别不出烫金的高资和资深)
>   - 换用 [tortoise-orm](https://github.com/tortoise/tortoise-orm) 进行本地数据库异步读写
>   - 优化联网请求资源时的效率
> - 添加新功能：猜干员、今日干员、帮助图片
> - 最低支持 Python 版本上调至 Python3.8，与 Nonebot2-rc2 一致
> 
> 2022-09-27 v0.5.8
> - 修复理智恢复提醒文件检测不存在问题 [@issue/16](https://github.com/NumberSir/nonebot_plugin_arktools/issues/16)
> - 重新添加文字公招查询 [@issue/17](https://github.com/NumberSir/nonebot_plugin_arktools/issues/17) [@issue/18](https://github.com/NumberSir/nonebot_plugin_arktools/issues/18)
> - 优化干员查询：干员不存在时提醒
> - 优化公招查询：反馈检测到的公招标签
> 
> 2022-09-24 v0.5.7
> - 修复干员公招查询算法问题 [@issue/13](https://github.com/NumberSir/nonebot_plugin_arktools/issues/13)
> - 修复干员公招查询作图重叠问题
> - 修复文件不存在报错问题 [@issue/15](https://github.com/NumberSir/nonebot_plugin_arktools/issues/15)
> - 优化公招查询结果
> 
> 2022-09-23 v0.5.6
> - 干员查询添加模组材料查询
> 
> 2022-09-15 v0.5.5
> - 修复了json文件不会覆盖下载的问题
> - 修复了公招识别读取头像路径的问题 [@issue/11](https://github.com/NumberSir/nonebot_plugin_arktools/issues/11)
> 
> 2022-09-01 v0.5.4
> - 修改资源获取方式为启动 nonebot 后下载到本地
> - 修复了检测路径缺失的问题 [@issue/8](https://github.com/NumberSir/nonebot_plugin_arktools/issues/8)
>
> 2022-09-01 v0.5.3
> - 修复未导入 os 模块的问题
>
> 2022-09-01 v0.5.2
> - 修复公招保存图片出错和缺少文件的问题 [@issue/7](https://github.com/NumberSir/nonebot_plugin_arktools/issues/7)
>
> 2022-09-01 v0.5.1
> - 重写了查询推荐公招标签的功能 [@issue/6](https://github.com/NumberSir/nonebot_plugin_arktools/issues/6)
>
> 2022-08-29 v0.5.0
> - 添加了查询干员的技能升级材料、专精材料、精英化材料的功能
>
> 2022-06-03 v0.4.1
> - 修复了发行版和源码不匹配的问题 [@issue/4](https://github.com/NumberSir/nonebot_plugin_arktools/issues/4)
> 
> 2022-06-03 v0.4.0
> - 添加了查询推荐公招标签的功能
>
> 2022-05-30 v0.3.0
> - 向下兼容到 Python 3.7.3 版本 [@issue/2](https://github.com/NumberSir/nonebot_plugin_arktools/issues/2)
>
> 2022-05-30 v0.2.1
> - 修复了使用 nb plugin install 命令安装后无法正常工作的问题 [@issue/1](https://github.com/NumberSir/nonebot_plugin_arktools/issues/1)
> 
> 2022-05-26 v0.2.0
> - 添加了查询最新活动信息的功能
>
> 2022-05-24 v0.1.0
> - 添加了查询今日开放资源关卡的功能

</details>
