from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from pyrogram import Client, filters

from bot import CONFIG
from bot.core.utils import generate_keyboard

from . import base62, chat, iv, key


def encrypt_file_id(file_id):
  file_id_bytes = str(file_id).encode()
  cipher = AES.new(key, AES.MODE_CFB, iv=iv)
  encrypted_bytes = cipher.encrypt(pad(file_id_bytes, AES.block_size))
  encrypted_base62 = base62.bytes_to_base62(encrypted_bytes)
  return encrypted_base62
  
@Client.on_message(filters.private & (filters.document | filters.video))
async def doc(client, message):
  editable = await message.reply_text("Please wait ...", quote=True)
  BotUsername = CONFIG.me.username
  forwarded_msg = await message.copy(chat)
  Ache_map = f'''
**Ache Map:**

**User ID** :{message.from_user.id}
  '''
  await forwarded_msg.reply(Ache_map)
  
  key = encrypt_file_id(forwarded_msg.id)

  
  url = f"https://telegram.dog/{BotUsername}?start=theostrich_{(str(key))}"
  btn = f"[Get file](url::{url})"
  keyboard = generate_keyboard(btn)

  await editable.reply(url, reply_markup=keyboard)
