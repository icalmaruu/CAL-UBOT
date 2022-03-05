from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.ical(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Perkenalkan Namaku Ical`")
    sleep(3)
    await typew.edit("Aku Tinggal Di Tanggerang`")
    sleep(1)
    await typew.edit("`Dan Aku Mencintai Gingun💖💖, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Gingun`")
    sleep(3)
    await typew.edit("`Ical Sayang Gingun❤️`")
    sleep(1)
    await typew.edit("`I LOVE YOU GINGUN ❣️💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart
