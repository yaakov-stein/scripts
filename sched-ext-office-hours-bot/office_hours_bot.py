import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import pytz
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
scheduler = AsyncIOScheduler(timezone=pytz.timezone("America/New_York"))

ZOOM_REMINDER = """\
Hi everyone, office hours begin an hour from now:
Join Zoom Meeting
https://fb.zoom.us/j/92428111425?pwd=QUZMTXVrUlRma3pGUGdHcHQvUko5UT09
Meeting ID: 924 2811 1425
Passcode: 455165
---
**One tap mobile**
+13126266799,,92428111425#,,,,*455165# US (Chicago)
+13092053325,,92428111425#,,,,*455165# US
---
**Dial by your location**
• +1 312 626 6799 US (Chicago)
• +1 309 205 3325 US
• +1 929 205 6099 US (New York)
• +1 301 715 8592 US (Washington DC)
• +1 305 224 1968 US
• +1 646 931 3860 US
• +1 719 359 4580 US
• +1 253 205 0468 US
• +1 253 215 8782 US (Tacoma)
• +1 346 248 7799 US (Houston)
• +1 360 209 5623 US
• +1 386 347 5053 US
• +1 507 473 4847 US
• +1 564 217 2000 US
• +1 669 444 9171 US
• +1 669 900 6833 US (San Jose)
• +1 689 278 1000 US
• 888 788 0099 US Toll-free
• 833 548 0276 US Toll-free
• 833 548 0282 US Toll-free
• 877 853 5247 US Toll-free
Meeting ID: 924 2811 1425
Passcode: 455165
Find your local number: https://fb.zoom.us/u/aezu9gs8np
---
**Join by SIP**
• 92428111425@zoomcrc.com
---
**Join by H.323**
• 162.255.37.11 (US West)
• 162.255.36.11 (US East)
• 115.114.131.7 (India Mumbai)
• 115.114.115.7 (India Hyderabad)
• 213.19.144.110 (Amsterdam Netherlands)
• 213.244.140.110 (Germany)
• 103.122.166.55 (Australia Sydney)
• 103.122.167.55 (Australia Melbourne)
• 149.137.40.110 (Singapore)
• 64.211.144.160 (Brazil)
• 149.137.68.253 (Mexico)
• 69.174.57.160 (Canada Toronto)
• 65.39.152.160 (Canada Vancouver)
• 207.226.132.110 (Japan Tokyo)
• 149.137.24.110 (Japan Osaka)
Meeting ID: 924 2811 1425
Passcode: 455165"""

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    scheduler.start()

    # Schedule a job every Tuesday at 10:00 AM NY time
    scheduler.add_job(send_reminder, CronTrigger(day_of_week="tue", hour=10, minute=0))

async def send_reminder():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(ZOOM_REMINDER)

bot.run(TOKEN)
