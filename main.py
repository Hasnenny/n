from pyrogram import Client
from pyrogram import  filters,enums
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import InlineKeyboardMarkup as mk, InlineKeyboardButton as btn
from pyrogram.types import ChatPermissions

from asSQL import Client as cl


data = cl("protect")
db = data['data']
db.create_table()
db.set("botname",['عهد' , 'عهود' , 'بوت' ,'عاهد' , 'عهو'])
db.set("bad_words",['كس','عير','طيز','زب','كسمك','كسختك','طيزك','مص'])

plugins = dict(root="plugins")

Client("x",
api_id=21916110,
api_hash="5e934a743eacd3bba982df50f2849209",
bot_token="7163792001:AAF0-3OYkxmhBqWtmpERCXHTNq_3zD8l5B0", plugins=plugins).run()