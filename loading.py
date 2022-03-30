
import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.lsh(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("`Visual loading module`")
	sleep(1.5)
	await typew.edit("loading")
	await typew.edit("•loading•")
	sleep(0.6)
	await typew.edit("••loading••")
	sleep(0.6)
	await typew.edit("•••loading•••")
	sleep(0.6)
	await typew.edit("•loading•")
	sleep(0.6)
	await typew.edit("••loading••")
	sleep(0.6)
	await typew.edit("•••loading•••")
	sleep(0.6)
	await typew.edit("•loading•")
	sleep(0.6)
	await typew.edit("••loading••")
	sleep(0.6)
	await typew.edit("•••loading•••")
	sleep(0.6)
	await typew.edit("•loading•")
	sleep(0.6)
	await typew.edit("••loading••")
	sleep(0.6)
	await typew.edit("•••loading•••")
	sleep(0.6)
	sleep(1.3)
	await typew.edit("`Ready!`")
