import httpx
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.typing import T_State

__plugin_meta__ = PluginMetadata(
    name="对对联",
    description="人工智能和你对对联",
    usage="对联<内容> (数量)",
    type="application",
    homepage="https://github.com/CMHopeSunshine/nonebot-plugin-couplets",
    supported_adapters=None,
    extra={
        "author":  "惜月 <277073121@qq.com>",
        "version": "1.0.0",
    },
)

couplets = on_command('对联', aliases={'对对联'}, priority=13, block=True, state={
    'pm_usage': '对联<内容> (数量)',
    'pm_describe': '人工智能和你对对联',
    'pm_priority': 15
})


@couplets.handle()
async def _(state: T_State, msg: Message = CommandArg()):
    msg_text = msg.extract_plain_text().strip()
    args = msg_text.split(' ', 1)
    if len(args) == 2 and args[1].isdigit():
        num = int(args[1])
    else:
        num = None
    if args[0]:
        state['text'] = args[0]
    if num:
        state['num'] = min(num, 10)
    else:
        state['num'] = 1


@couplets.got('text', prompt='请输入上联内容')
async def couplets_handler(state: T_State):
    url = f'https://seq2seq-couplet-model.rssbrain.com/v0.2/couplet/{state["text"]}'
    async with httpx.AsyncClient() as client:
        res = await client.get(url=url)
    res = res.json()
    result = '\n'.join(['➤' + res['output'][n] for n in range(state['num'])])
    await couplets.finish(f'上联：\n➤{state["text"]}\n下联：\n{result}')
