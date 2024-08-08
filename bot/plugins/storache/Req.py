from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from pyrogram import Client, filters
from pyrogram.errors import FloodWait

from bot import strings
from bot.core.utils import generate_keyboard

from . import base62, chat, iv, key


def decrypt_file_id(encrypted_file_id):
  combined_data = base62.base62_to_bytes(encrypted_file_id)
  encrypted_bytes = combined_data

  cipher = AES.new(key, AES.MODE_CFB, iv=iv)
  decrypted_padded_bytes = cipher.decrypt(encrypted_bytes)
  file_id_bytes = unpad(decrypted_padded_bytes, AES.block_size)

  return int(file_id_bytes.decode())
    
@Client.on_message(filters.command(["start"]))
async def start(client, message):
    
    
    #print(message.command)
    key = message.text.split("_")[-1]

    if key == "/start":   
        text = strings.get("start_txt", user=message.from_user.mention)
        keyboard = generate_keyboard(strings.get("start_btn"))

        await message.reply_text(
            text,
            disable_web_page_preview=True,
            reply_markup=keyboard,
            quote=True,
    )
    else:
         
         try:
          file_id = decrypt_file_id(key)
         except:
            await message.reply("File Not Found")
            return
         try:
            await client.forward_messages(chat_id=message.from_user.id,
                                      from_chat_id=chat,
                                      message_ids=int(file_id))
         except FloodWait as e:
             await message.reply_text(f"A floodwait of {e.value} seconds is required. Please try again later.")
            
             