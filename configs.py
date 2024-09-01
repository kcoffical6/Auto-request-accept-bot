from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", , "")
    BOT_TOKEN = getenv("BOT_TOKEN", "665196")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", "-))#update channel
    SUDO = list(map(int, getenv("SUDO", "").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://:/?retryWrites=true&w=majority")
    WEB_SERVER = getenv("WEB_SERVER", False)
    PORT = int(getenv("PORT", 8080))
cfg = Config()
