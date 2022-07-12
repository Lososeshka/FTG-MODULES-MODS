import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.antiban(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Antiban starts`")
	sleep(1.5)
	await typew.edit("import `asyncio`")
	sleep(1.0)
	await typew.edit("import `re`")
	sleep(1.0)
	await typew.edit("import `time`")
	sleep(1.0)
	await typew.edit("from userbot import `CMD_HELP, ZALG_LIST`")
	sleep(1.0)
	await typew.edit("from userbot.events import `register`")
	sleep(1.0)
	await typew.edit("from telethon.errors import~~~")
	sleep(1.0)
	await typew.edit("ChatAdminRequiredError")
	sleep(1.0)
	await typew.edit("UserAdminInvalidError")
	sleep(1.0)
	await typew.edit("except ChatAdminRequiredError:")
	sleep(1.5)
	await typew.edit("return await utils.answer.message, self.strings")
	sleep(1.5)
	await typew.edit("ban_users=adm_rights.ban_users")
	sleep(1.5)
	sleep(0.5)
	await typew.edit("[okay]~~~except ChatAdminRequiredError")