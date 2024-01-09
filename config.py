import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("BOT_TOKEN")
# Add Owner Username without @ 
OWNER_USERNAME = getenv("OWNER_USERNAME","Itachi007ff")
# Get Your bot username
BOT_USERNAME = getenv("BOT_USERNAME" , "")
# Don't Add style font 
BOT_NAME = getenv("BOT_NAME" , "")
#get Your Assistant User name
ASSUSERNAME = getenv("ASSUSERNAME" , "")
EVALOP = list(map(int, getenv("EVALOP", "").split()))
# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("LOGGER_ID", ))

# Get this value from  on Telegram by /id
OWNER_ID = int(getenv("OWNER_ID", ))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
   "UPSTREAM_REPO",
   "https://github.com/tushar007ff/Itachi2.-0",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Rudra")
GIT_TOKEN = getenv(
   "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/mei_support")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/warzone_123")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
   "START_IMG_URL", = getenv( "START_IMG_URL", "https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png", "https://te.legra.ph/file/639efe98c133d71c418db.png", "https://te.legra.ph/file/8a834586b677739b86bff.png", "https://te.legra.ph/file/13f79674ce777f43871fb.png", "https://te.legra.ph/file/147157eca055a1e2c8756.png", "https://te.legra.ph/file/b774a8da74dc954afebc6.png", "https://te.legra.ph/file/7ae4a6a6a6c28f9f08ceb.png", "https://te.legra.ph/file/12d5ea64ed00416a38ec8.png", "https://telegra.ph/file/6fb14167a9a6a0b367c25.jpg", "https://telegra.ph/file/f3b2776b2766e911383f0.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/7bd0df591ffc6efb4e222.jpg", "https://telegra.ph/file/3b02a59a4a7fa8a5e1df4.jpg", "https://telegra.ph/file/1b80eec8135011abbe532.jpg", "https://telegra.ph/file/2b6c398eff3897b14bc1c.jpg", "https://telegra.ph/file/8b4a30cc04bb36352ab34.jpg", "https://telegra.ph/file/51b2139b3ec584befb62f.jpg", "https://telegra.ph/file/8aa3a086fb9690b6ff221.jpg", "https://telegra.ph/file/15305e45af3139022a789.jpg", "https://telegra.ph/file/f48a14480e4a6736438dd.jpg", "https://graph.org/file/597fb01053d7d19454a56.jpg", "https://graph.org/file/8d9f37781edef499e6240.jpg", "https://graph.org/file/8f792296f4cb01f207521.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg", "https://graph.org/file/4ddbe257d2fa3f55037b4.jpg","https://graph.org/file/598c181eb136ae92aa107.jpg", "https://graph.org/file/59a167ff606909e30ad73.jpg", "https://graph.org/file/8084b560bd19d28caae87.jpg", "https://graph.org/file/5b0fc5b3ff12c17f30c89.jpg" ) PING_IMG_URL = getenv( "PING_IMG_URL","https://te.legra.ph/file/7757731c3e8b784b6a550.png", "https://te.legra.ph/file/58c34981e21180989887c.png", "https://te.legra.ph/file/a3a874be5095d9af685ac.png", "https://te.legra.ph/file/ac461a1889255424420ff.png", "https://te.legra.ph/file/74a8ba5270d0e27ac045c.png", "https://te.legra.ph/file/c0d0ee1452cbbbce116f4.png", "https://te.legra.ph/file/d373ae93502a5ae7fd403.png", "https://te.legra.ph/file/ab243bcad20965f637b5c.png", "https://te.legra.ph/file/fd9cc86239dd76d564d01.png", "https://te.legra.ph/file/c12a0b77178e2d2e27a50.png", "https://te.legra.ph/file/35177bbb5d5f07ad8e394.png", "https://te.legra.ph/file/700af8c3ee786a20aff35.png", "https://te.legra.ph/file/cbecd8af0446a422a95ca.png", "https://te.legra.ph/file/c3a0fde4abde25dd25e26.png", "https://te.legra.ph/file/7be8c2f9e093f695c4c6e.png", "https://te.legra.ph/file/ee10888e828bae3a6a0fc.png", "https://te.legra.ph/file/1b55fe681163188149fa4.png", "https://te.legra.ph/file/30ee4e96f64cd9abb69b6.png", "https://te.legra.ph/file/30b121ce5fa87360692ba.png", "https://te.legra.ph/file/f0617cc52008bd78f1a9d.png", "https://te.legra.ph/file/1cd1adc3eb9ac0a101610.png", "https://te.legra.ph/file/860c3dd149f91eb450d5a.png", "https://te.legra.ph/file/2e9df77f8100e0327ba52.png",
)
PING_IMG_URL = getenv(
   "PING_IMG_URL", "https://telegra.ph/file/7ed9dfc48b7b507d7eec8.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
STATS_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/0592ea63ab99370aae099.jpg"


def time_to_seconds(time):
   stringt = str(time)
   return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))