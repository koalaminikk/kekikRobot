# Thanks to catuserbot          ~t.me/catuserbot17

import re
from asyncio import sleep
from emoji import get_emoji_regexp
from userbot import bot
from userbot.events import register
from userbot.cmdhelp import CmdHelp

async def reply_id(event):
    reply_to_id = None
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    return reply_to_id


def deEmojify(inputString: str) -> str:
    return get_emoji_regexp().sub("", inputString)


async def hide_inlinebot(asena, bot_name, text, chat_id, reply_to_id, c_lick=0):
    sticcers = await asena.inline_query(bot_name, f"{text}.")
    mesaj = await sticcers[c_lick].click("me", hide_via=True)
    if mesaj:
        await asena.send_file(int(chat_id), mesaj, reply_to=reply_to_id)
        await mesaj.delete()

#---------------------------------------------------------#

@register(outgoing=True, pattern="^.honk(?: |$)(.*)")
async def honk(event):
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@honka_says_bot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await event.edit(
                event, "**Bu grupta satır içi botlara izin verilmiyor!**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)

#---------------------------------------------------------#

@register(outgoing=True, pattern="^.twt(?: |$)(.*)")
async def twt(event):
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@TwitterStatusBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "**Bu grupta satır içi botlara izin verilmiyor!**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)

#---------------------------------------------------------#

@register(outgoing=True, pattern="^.glax(|r)(?:\s|$)([\s\S]*)")
async def glax(event):
    cmd = event.pattern_match.group(1).lower()
    text = event.pattern_match.group(2)
    reply_to_id = await reply_id(event)
    bot_name = "@GlaxScremBot"
    c_lick = 1 if cmd == "r" else 0
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "**Bu grupta satır içi botlara izin verilmiyor!**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(
        event.client, bot_name, text, event.chat_id, reply_to_id, c_lick=c_lick)

#---------------------------------------------------------#

@register(outgoing=True, pattern="^.shb(?: |$)(.*)")
async def shb(event):
    text = event.pattern_match.group(1)
    reply_to_id = await reply_id(event)
    bot_name = "@DogeStickerBot"
    if not text:
        if event.is_reply:
            text = (await event.get_reply_message()).message
        else:
            return await edit_delete(
                event, "**Bu grupta satır içi botlara izin verilmiyor!**"
            )
    text = deEmojify(text)
    await event.delete()
    await hide_inlinebot(event.client, bot_name, text, event.chat_id, reply_to_id)

#---------------------------------------------------------#

CmdHelp('inlinefun').add_command(
    "honk", "<metin/yanıt>", "Yazdığınız yazıyı hareketli peepo çıkartması yapar."
    ).add_command(
    "twt", "<metin/yanıt>", "Yazınızı tweete dönüştürün."
    ).add_command(
    "glax", "<metin/yanıt>", "Yazınızı hareketli stickere dönüştürün. (sola doğru)"
    ).add_command(
    "glaxr", "<metin/yanıt>", "Yazınızı hareketli stickere dönüştürün. (sağa doğru)"
    ).add_command(
    "shb", "<metin/yanıt>", "Yazınızı doge stickerine dönüştürün."
).add()