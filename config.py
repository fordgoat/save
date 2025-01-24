# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "29486311"))
API_HASH = getenv("API_HASH", "ffdc688dc4eee8d2585cb24155188432")
BOT_TOKEN = getenv("BOT_TOKEN", "7300347870:AAFNfnj1sEUQNnE1zdyFq-xgY8UkeuKjubw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "1707380693").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://ucik:ucik@cluster0.0l3r8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002339772659")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002234563714"))
