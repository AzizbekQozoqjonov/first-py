# @MIRSHODBEY
from pyrogram import Client, emoji, filters
from pyrogram.errors import FloodWait
from pyrogram import Client
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)

from pyrogram.types import ChatPermissions
# @MIRSHODBEY
import time
from time import sleep
import random
 
api_id =  946934378
api_hash = "2176806a3cbcf43cb49ebd09654337db"


app = Client("my_account", api_id=api_id, api_hash=api_hash)

# Команда type
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".type ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "...💬"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)

# @MIRSHODBEY
@app.on_message(filters.command("write", prefixes=".") & filters.me)
def type(_, msg):
    orig_text = msg.text.split(".write ", maxsplit=1)[1]
    text = orig_text
    tbp = "" # to be printed
    typing_symbol = "...✍️"
 
    while(tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05) # 50 ms
 
            tbp = tbp + text[0]
            text = text[1:]
 
            msg.edit(tbp)
            sleep(0.05)
 
        except FloodWait as e:
            sleep(e.x)
# @MIRSHODBEY
# Команда взлома пентагона
@app.on_message(filters.command("love", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "🔥🔥🔥🔥🔥🔥🔥🔥🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥" + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0
# @MIRSHODBEY
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0
# @MIRSHODBEY
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 # @MIRSHODBEY
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌹\n🔥❤️🧡💛💚💙💜🤎🔥\n🌹❤️‍🔥💖💗💕💞💓🤍🔥\n🌹❤️🧡💛💚💙💜🤎🔥\n🔥❤️🧡💛💚💙💜🤎🔥\n🔥❤️‍🔥💖💗💕💞💓🤍🔥\n🥀❤️🧡💛💚💙💜🤎🔥\n🔥🔥🔥🔥🔥🔥🔥🔥🔥")
    sleep(0.01)
 
    msg.edit("🔥🔥🔥🔥🔥🔥🔥🔥🌞\n🔥🔥☘️☘️☘️☘️☘️☘️🌞\n🌹🔥🌷🌷🌷🌷🌷🌷🌞\n🌹🔥🌻🌻🌻🌻🌻🌻🌞\n🔥🔥🌺🌺🌺🌺🌺🌺🌞\n🔥🔥🌸🌸🌸🌸🌸🌸🌞\n🥀🔥🌼🌼🌼🌼🌼🌼🌞\n🔥🔥🔥🔥🔥🔥🔥🔥🌞")
    perc = 0

# HELP HELP HELP HELP HELP HELP HELP HELP HELP HELPHELP HELP HELP HELP HELPHELP HELP HELP HELP HELP
@app.on_message(filters.command("help", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 # @MIRSHODBEY
    while(perc < 20):
        try:
            text = "ʜᴇʟᴘ ʙᴜʏʀᴜɢ`ɪ ɪsʜɢᴀ ᴛᴜsʜᴍᴏǫᴅᴀ..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("[H̲̲̅̅E̲̲̅̅L̲̲̅̅P̲̲̅̅]🕹\n\n1) .ʜᴇʟᴘ = ᴜsᴇʀʙᴏᴛ ʜᴀǫɪᴅᴀ!🖲\n\n2) .ᴘɪɴɢ = ᴜsᴇʀʙᴏᴛ ᴛᴇᴢʟɪɢɪ🪫\n\n3) .ʟᴏᴠᴇ = ᴀɴɪᴍᴀᴛsɪᴏɴ ᴏʟᴏᴠʟɪ ʏᴜʀᴀᴋᴄʜᴀʟᴀʀ❤️‍🔥\n\n4) .ɢᴀᴍᴇ = ǫɪᴢɪǫ ᴋᴏ`ɴɢɪʟ ᴋᴏ`ᴛᴀʀᴜᴠᴄʜɪ ᴏ`ʏɪɴ🎮\n\n5) .ᴀɴᴍ = ʏᴜǫᴏʀɪ ᴀɴɪᴍᴛsɪᴀ☣️\n\n6).ʜᴀᴘᴘʏ = ᴛᴜɢᴜʟɢᴀɴ ᴋᴜɴ ᴛᴀʙʀɪᴋ ᴀɴɪᴍᴀᴛsɪᴀ🥳\n\n7).ᴊᴜᴍᴀ = ᴊᴜᴍᴀ ᴛᴀʙʀɪᴋ ᴀɴɪᴍᴀᴛsɪᴀ🌟\n\n8).sᴠᴇᴛ = ᴘᴏʟɪᴛsɪᴀ  ᴀᴠᴛᴏᴍᴏʙɪʟɪ ᴄʜɪʀᴏɢɪ ᴀɴɪᴍᴀᴛsɪᴀ🚓\n\n9).ᴛʏᴘᴇ = .ᴛʏᴘᴇ ᴅᴀɴ sᴏ`ɴɢ ᴘʀᴏʙᴇʟ ᴛᴀsʜᴀʙ sᴏ`ᴢ ʏᴏᴢᴀsᴢ sᴏᴢɪɴɢɪᴢ ᴀɴɪᴍᴀᴛsɪᴀ ʙᴏ`ʟᴀᴅɪ  (...💬) <<< ᴜsʜʙᴜ sʜᴀᴋʟᴅᴀ\n\n10).ᴡɪʀɪᴛᴇ = .ᴡɪʀɪᴛᴇ ᴅᴀɴ sᴏ`ɴɢ ᴘʀᴏʙᴇʟ ᴛᴀsʜᴀʙ sᴏ`ᴢ ʏᴏᴢᴀsᴢ sᴏᴢɪɴɢɪᴢ ᴀɴɪᴍᴀᴛsɪᴀ ʙᴏ`ʟᴀᴅɪ  (...✍️) <<< ᴜsʜʙᴜ sʜᴀᴋʟᴅᴀ\n\n\nP̫̫Y̫̫T̫̫H̫̫O̫̫N̫̫ ̫̫U̫̫S̫̫E̫̫R̫̫B̫̫O̫̫T̫̫ 📌\nC̫̫R̫̫E̫̫A̫̫T̫̫O̫̫R̫̫ @MirshodBEY 📌")
    perc = 0
#GAME GAME GAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAMEGAME GAME
@app.on_message(filters.command("game", prefixes=".") & filters.me)
def game(_, msg):
    perc = 0
 
    while(perc < 50):
        try:
            text = "Qassob NAME 🔪🔪🔪🔪🔪 qo`y suymoqda..." + str(perc) + "%"
            msg.edit(text)
 # @MIRSHODBEY
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
    msg.edit("Qo`y Suyuldi🔪🐑")
    sleep(2.0)
 
    msg.edit("Go`shtini MirshodBEY ga sotib soqqa qildi🥩➕💰➕🤑")
    perc = 0
# PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING PING 
@app.on_message(filters.command("ping", prefixes=".") & filters.me)
def game(_, msg):
    perc = 0
 
    while(perc < 50):
        try:
            text = "Ping Burug`i Ishga Tushmoqda..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 # @MIRSHODBEY
        except FloodWait as e:
            sleep(e.x)

    msg.edit("@MirshodBEY UserBot tezligi 67.8% ni tashkil qiladi!)")
    perc = 0


@app.on_message(filters.command("anm", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍🤍🤍🤍ᴍɪʀsʜᴏᴅʙᴇʏ" + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍🤍🤍❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍🤍❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍❤️❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ❤️❤️❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍🤍🤍❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍🤍❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍❤️❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ❤️❤️❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍🤍🤍❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍🤍❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍🤍❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍🤍❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0
# @MIRSHODBEY
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍🤍❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)
 
    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ🤍❤️❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    perc = 0

    msg.edit("ᴍɪʀsʜᴏᴅʙᴇʏ❤️❤️❤️❤️❤️❤️❤️ᴍɪʀsʜᴏᴅʙᴇʏ")
    sleep(0.01)




# HAPPY HAPPY HAPPY HAPPYHAPPY HAPPYHAPPY HAPPYHAPPY HAPPYHAPPY HAPPYHAPPY HAPPYHAPPY HAPPYHAPPY HAPPYHAPPY HAPPYHAPPY HAPPY
@app.on_message(filters.command("happy", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "⚪️" + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 # @MIRSHODBEY
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("⚪️⚪️")
    sleep(0.01)
 
    msg.edit("⚪️⚪️⚪️")
    perc = 0

    msg.edit("⚪️⚪️⚫️")
    sleep(0.01)
 
    msg.edit("⚪️⚫️⚫️")
    perc = 0

    msg.edit("⚫️⚫️⚫️")
    sleep(0.01)

    msg.edit("⚪️⚪️")
    sleep(0.01)
 
    msg.edit("⚪️⚪️⚪️")
    perc = 0

    msg.edit("⚪️⚪️⚫️")
    sleep(0.01)
 
    msg.edit("⚪️⚫️⚫️")
    perc = 0

    msg.edit("⚫️⚫️⚫️")
    sleep(0.01)

    msg.edit("⚪️⚪️")
    sleep(0.01)
 
    msg.edit("⚪️⚪️⚪️")
    perc = 0

    msg.edit("⚪️⚪️⚫️")
    sleep(0.01)
 
    msg.edit("⚪️⚫️⚫️")
    perc = 0

    msg.edit("⚫️⚫️⚫️")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅]                                                       \n✨[H̲̅]                                                                                    \n✨[H̲̅]                                                           \n✨[H̲̅]                                                            \n✨[H̲̅]                                                             \n✨[H̲̅]                                                             \n✨[H̲̅]                                                             \n✨[H̲̅]                                                             \n✨[H̲̅]                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅A]                                                       \n✨[H̲̅A]                                                                                    \n✨[H̲̅A]                                                           \n✨[H̲̅A]                                                            \n✨[H̲̅A]                                                             \n✨[H̲̅A]                                                             \n✨[H̲̅A]                                                             \n✨[H̲̅A]                                                             \n✨[H̲̅A]                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅AP]                                                       \n✨[H̲̅AP]                                                                                    \n✨[H̲̅AP]                                                           \n✨[H̲̅AP]                                                            \n✨[H̲̅AP]                                                             \n✨[H̲̅AP]                                                             \n✨[H̲̅AP]                                                             \n✨[H̲̅AP]                                                             \n✨[H̲̅AP]                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APP]                                                       \n✨[H̲̅APP]                                                                                    \n✨[H̲̅APP]                                                           \n✨[H̲̅APP]                                                            \n✨[H̲̅APP]                                                             \n✨[H̲̅APP]                                                             \n✨[H̲̅APP]                                                             \n✨[H̲̅APP]                                                             \n✨[H̲̅APP]                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY]                                                       \n✨[H̲̅APPY]                                                                                    \n✨[H̲̅APPY]                                                           \n✨[H̲̅APPY]                                                            \n✨[H̲̅APPY]                                                             \n✨[H̲̅APPY]                                                             \n✨[H̲̅APPY]                                                             \n✨[H̲̅APPY]                                                             \n✨[H̲̅APPY]                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                                                   \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")                                                     
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")                                                       
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                                                     \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                           \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0
# @MIRSHODBEY
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                     \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                                                   \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")        
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")                                                       
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                                                     \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                           \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                     \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0
# @MIRSHODBEY
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                                                   \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")                                                       
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")                                                       
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                                                     \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                           \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                     \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️⚪️                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 # @MIRSHODBEY
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                                                   \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️⚪️🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")                                                       
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                          \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                            \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️⚪️🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")                                                       
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                                                     \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                           \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️⚪️🥳🥳🥳                                                              \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0

    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                      \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] ⚪️🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    sleep(0.01)
 
    msg.edit("✨✨✨✨✨✨✨✨✨✨✨✨\n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                     \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                                                    \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                          \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                            \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨[H̲̅APPY] 🥳🥳🥳🥳🥳                                                             \n✨✨✨✨✨✨✨✨✨✨✨✨")
    perc = 0
    
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0
# @MIRSHODBEY
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0

    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0

    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0
# @MIRSHODBEY
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0

    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0

    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0
# @MIRSHODBEY
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0

    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0

    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    sleep(0.01)
 
    msg.edit("ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳  _____   ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\n\n\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳|||||ᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳\nᴛᴀʙʀɪᴋʟɪʏᴍɪᴢ🥳")
    perc = 0


# JUMA JUMA JUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMAJUMA JUMA
@app.on_message(filters.command("juma", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "▫️▫️▫️▫️▫️" + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("▫️▫️▫️▫️▫️")
    sleep(0.01)
 
    msg.edit("▫️▫️▫️▫️◾️")
    perc = 0

    msg.edit("▫️▫️▫️◾️◾️")
    sleep(0.01)
 
    msg.edit("▫️▫️◾️◾️◾️")
    perc = 0

    msg.edit("▫️◾️◾️◾️◾️")
    sleep(0.01)
 
    msg.edit("◾️◾️◾️◾️◾️")
    perc = 0

    msg.edit("▫️▫️▫️▫️▫️")
    sleep(0.01)
 
    msg.edit("▫️▫️▫️▫️◾️")
    perc = 0

    msg.edit("▫️▫️▫️◾️◾️")
    sleep(0.01)
 
    msg.edit("▫️▫️◾️◾️◾️")
    perc = 0

    msg.edit("▫️◾️◾️◾️◾️")
    sleep(0.01)
 
    msg.edit("◾️◾️◾️◾️◾️")
    perc = 0

    msg.edit("▫️▫️▫️▫️▫️")
    sleep(0.01)
 
    msg.edit("▫️▫️▫️▫️◾️")
    perc = 0

    msg.edit("▫️▫️▫️◾️◾️")
    sleep(0.01)
 
    msg.edit("▫️▫️◾️◾️◾️")
    perc = 0

    msg.edit("▫️◾️◾️◾️◾️")
    sleep(0.01)
 
    msg.edit("◾️◾️◾️◾️◾️")
    perc = 0

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    sleep(0.01)
 
    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💣💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💣💣💣💥💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣\n💣💣💣💣💣💣💣💣💣💣💣")
    perc = 0

    msg.edit("💣💣💣💣💣💣💥💣💣💣💣\n💥💣💥💣💣💣💣💣💣💣💣\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💣💣💥💣\n💣💣💥💣💣💣💣💣💥💣💣\n💥💥💥💣💣💣💣💣💣💣💥")
    sleep(0.01)
 
    msg.edit("💥💣💥💣💥💣💥💣💣💣💣\n💥💣💥💥💣💣💣💥💣💣💥\n💥💣💣💣💣💥💣💣💥💣💣\n💣💣💥💣💣💥💣💥💣💥💣\n💣💣💥💣💥💣💥💣💥💣💣\n💥💥💥💣💣💣💥💣💥💣💥")
    perc = 0

    msg.edit("💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥\n💥💥💥💥💥💥💥💥💥💥💥")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)

    msg.edit("✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨\n✨ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ✨")
    sleep(0.01)

    msg.edit("🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊\n🕊ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🕊")
    sleep(0.01)

    msg.edit("🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟\n🌟ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌟")
    sleep(0.01)

    msg.edit("🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐\n🪐ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🪐")
    sleep(0.01)

    msg.edit("🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞\n🌞ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🌞")
    sleep(0.01)

    msg.edit("🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃\n🍃ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🍃")
    sleep(0.01)

    msg.edit("🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿\n🇺🇿ᴊᴜᴍᴀ ᴀʏʏᴏᴍɪɴɢɪᴢ ᴍᴜʙᴏʀᴀᴋ ʙᴏ`ʟsɪɴ🇺🇿")
    sleep(0.01)
# SVET SVET SVET SVETSVET SVETSVET SVETSVET SVETSVET SVETSVET SVETSVET SVETSVET SVETSVET SVETSVET SVETSVET SVETSVET SVET
@app.on_message(filters.command("svet", prefixes=".") & filters.me)
def love(_, msg):
    perc = 0
 
    while(perc < 3):
        try:
            text = "1..." + str(perc) + "%"
            msg.edit(text)
 
            perc += random.randint(1, 3)
            sleep(0.1)
 
        except FloodWait as e:
            sleep(e.x)
 
    msg.edit("1...")
    sleep(0.01)
 
    msg.edit("2...")
    perc = 0

    msg.edit("3...")
    sleep(0.01)
 
    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)
# @MIRSHODBEY
    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)

    msg.edit("🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵\n🔴🔴🔴🔴🔴🔴🔴⬜️⬜️⬜️⬜️⬜️⬜️🔵🔵🔵🔵🔵🔵🔵")
    perc = 0

    msg.edit("🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴\n🔵🔵🔵🔵🔵🔵🔵⬜️⬜️⬜️⬜️⬜️⬜️🔴🔴🔴🔴🔴🔴🔴")
    sleep(0.01)
# @MIRSHODBEY
app.run()

# @MIRSHODBEY
