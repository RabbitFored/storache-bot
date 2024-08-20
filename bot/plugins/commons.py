from pyrogram import Client, filters

from bot import CONFIG, strings
from bot.core import filters as fltr
from bot.core.utils import generate_keyboard




@Client.on_message(filters.command(["help"]))
async def get_help(client, message):
    group_url = CONFIG.settings["links"]["group_url"]

    text = strings.get("help_txt")
    keyboard = generate_keyboard(strings.get("help_btn", group_url=group_url))

    # extended help message for bot administrator
    chatID = message.chat.id
    admins = CONFIG.get_group("admin")

    if chatID in admins:
        text += "\n\n" + strings.get("admin_help_txt")
    if message.from_user.is_self:
        await message.edit(text,
                           reply_markup=keyboard,
                           disable_web_page_preview=True)
    else:
        await message.reply_text(text,
                                 reply_markup=keyboard,
                                 quote=True,
                                 disable_web_page_preview=True)


@Client.on_message(filters.command(["about"]))
async def aboutTheBot(client, message):
    channel_url = CONFIG.settings["links"]["channel_url"]
    group_url = CONFIG.settings["links"]["group_url"]

    text = strings.get("about_txt")
    keyboard = generate_keyboard(
        strings.get("about_btn", channel_url=channel_url, group_url=group_url))

    await message.reply_text(text,
                             reply_markup=keyboard,
                             quote=True,
                             disable_web_page_preview=True)


@Client.on_message(filters.command(["donate"]))
async def donate(client, message):
    repo_url = CONFIG.settings["links"]["repo_url"]
    donation_url = CONFIG.settings["links"]["donation_url"]
   
    text = strings.get("donate_txt")
    keyboard = generate_keyboard(strings.get("donate_btn",repo_url=repo_url, donation_url=donation_url))

    await message.reply_text(text,
                             reply_markup=keyboard,
                             quote=True,
                             disable_web_page_preview=True)
