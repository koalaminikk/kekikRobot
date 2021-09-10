from userbot import CMD_HELP
from userbot.events import register
from userbot.cmdhelp import CmdHelp
from io import BytesIO
from random import randint
from textwrap import wrap
from PIL import Image, ImageDraw, ImageFont
from requests import get

@register(outgoing=True, pattern="^.peepo (.*)")
async def peepo(e):

    SusText = e.pattern_match.group(1)

    await e.edit("`İşleniyor...`")

    arr = randint(1, 17)
    fontsize = 125
    FONT_FILE = 'userbot/fonts/impact.ttf'
    url = 'https://raw.githubusercontent.com/Selfuucuk/Peepo/main/'
    font = ImageFont.truetype(FONT_FILE, size=int(fontsize))

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    text_ = '\n'.join(['\n'.join(wrap(part, 30)) for part in SusText.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 65, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    image.save("peepo.webp", 'WebP')

    await e.delete()
    await e.client.send_file(e.chat_id, "peepo.webp", reply_to=e.message.reply_to_msg_id)
    
@register(outgoing=True, pattern="^.peepo2 (.*)")
async def peepo(e):

    SusText = e.pattern_match.group(1)

    await e.edit("`İşleniyor...`")

    arr = randint(1, 12)
    fontsize = 125
    FONT_FILE = 'userbot/fonts/impact.ttf'
    url = 'https://raw.githubusercontent.com/Selfuucuk/Peepo2/main/'
    font = ImageFont.truetype(FONT_FILE, size=int(fontsize))

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    text_ = '\n'.join(['\n'.join(wrap(part, 30)) for part in SusText.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    image.save("peepo.webp", 'WebP')

    await e.delete()
    await e.client.send_file(e.chat_id, "peepo.webp", reply_to=e.message.reply_to_msg_id)

@register(outgoing=True, pattern="^.doge (.*)")
async def selffuck(e):

    SusText = e.pattern_match.group(1)

    await e.edit("`İşleniyor...`")

    arr = randint(1, 19)
    fontsize = 125
    FONT_FILE = 'userbot/fonts/impact.ttf'
    url = 'https://raw.githubusercontent.com/Selfuucuk/doge/master/'
    font = ImageFont.truetype(FONT_FILE, size=int(fontsize))

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    text_ = '\n'.join(['\n'.join(wrap(part, 30)) for part in SusText.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    image.save("doge.webp", 'WebP')

    await e.delete()
    await e.client.send_file(e.chat_id, "doge.webp", reply_to=e.message.reply_to_msg_id)
    
@register(outgoing=True, pattern="^.iqless (.*)")
async def peepo(e):

    SusText = e.pattern_match.group(1)

    await e.edit("`İşleniyor...`")

    arr = randint(1, 12)
    fontsize = 125
    FONT_FILE = 'userbot/fonts/impact.ttf'
    url = 'https://raw.githubusercontent.com/Selfuucuk/iqless/main/'
    font = ImageFont.truetype(FONT_FILE, size=int(fontsize))

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    text_ = '\n'.join(['\n'.join(wrap(part, 30)) for part in SusText.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    image.save("iqless.webp", 'WebP')

    await e.delete()
    await e.client.send_file(e.chat_id, "iqless.webp", reply_to=e.message.reply_to_msg_id)
    
@register(outgoing=True, pattern="^.selffuck (.*)")
async def selffuck(e):

    SusText = e.pattern_match.group(1)

    await e.edit("`İşleniyor...`")

    arr = randint(1, 19)
    fontsize = 125
    FONT_FILE = 'userbot/fonts/impact.ttf'
    url = 'https://raw.githubusercontent.com/Selfuucuk/Selffuck/master/'
    font = ImageFont.truetype(FONT_FILE, size=int(fontsize))

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    text_ = '\n'.join(['\n'.join(wrap(part, 30)) for part in SusText.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    image.save("sf.webp", 'WebP')

    await e.delete()
    await e.client.send_file(e.chat_id, "sf.webp", reply_to=e.message.reply_to_msg_id)

# Thanks to TeamDerUntergang for idea and helps.    ~t.me/SedenUserBot

# Unofficial and Copied Amogus plugin for Asena Userbot
#      t.me/selacs 

@register(outgoing=True, pattern="^.amogus (.*)")
async def amogus(e):

    SusText = e.pattern_match.group(1)

    await e.edit("`İşleniyor...`")

    arr = randint(1, 12)
    fontsize = 125
    FONT_FILE = 'userbot/fonts/impact.ttf'
    url = 'https://raw.githubusercontent.com/KeyZenD/AmongUs/master/'
    font = ImageFont.truetype(FONT_FILE, size=int(fontsize))

    imposter = Image.open(BytesIO(get(f'{url}{arr}.png').content))
    text_ = '\n'.join(['\n'.join(wrap(part, 30)) for part in SusText.split('\n')])
    w, h = ImageDraw.Draw(Image.new('RGB', (1, 1))).multiline_textsize(
        text_, font, stroke_width=2
    )
    text = Image.new('RGBA', (w + 40, h + 40))
    ImageDraw.Draw(text).multiline_text(
        (15, 15), text_, '#FFF', font, stroke_width=2, stroke_fill='#000'
    )
    w = imposter.width + text.width + 30
    h = max(imposter.height, text.height)
    image = Image.new('RGBA', (w, h))
    image.paste(imposter, (0, h - imposter.height), imposter)
    image.paste(text, (w - text.width, 0), text)
    image.thumbnail((512, 512))
    image.save("sus.webp", 'WebP')

    await e.delete()
    await e.client.send_file(e.chat_id, "sus.webp", reply_to=e.message.reply_to_msg_id)
    
CmdHelp('stickerfun').add_command(
    'peepo', '<metin>', 'Girilen yazıyı peepo textine çevirir.'
    ).add_command(
    'peepo2', '<metin>', 'Girilen yazıyı farklı peepo textine çevirir. '
    ).add_command(
    'doge', '<metin>', 'Girilen yazıyı doge textine çevirir.'
    ).add_command(
    'iqless', '<metin>', 'Girilen yazıyı iqless textine çevirir.'
    ).add_command(
    'selffuck', '<metin>', 'Girilen yazıyı selffuck textine çevirir.'
    ).add_command(
    'amogus', '<metin>', 'Girilen yazıyı amogus textine çevirir.'
).add()