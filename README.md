<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-couplets

_✨ Nonebot2对对联插件 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/CMHopeSunshine/nonebot-plugin-couplets.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-couplets">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-couplets.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

## 📖 介绍

基于[王斌给您对对联API](https://ai.binwang.me/couplet/)的Nonebot2对对联插件。

## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-couplets

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-couplets
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-couplets
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-couplets
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-couplets
</details>

打开 nonebot2 项目的 `bot.py` 文件, 在其中写入

    nonebot.load_plugin('nonebot_plugin_couplets')

</details>


## ☀ ️指令
```
对联 <上联内容> (数量)
· 数量可选，默认为1
```
例如，`对联 苟利国家生死以 3`

