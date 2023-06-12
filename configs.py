from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "10079689"))
    API_HASH = getenv("API_HASH", "8e402fe63a69576b82cda6daf1ab617f")
    BOT_TOKEN = getenv("BOT_TOKEN", "6115136533:AAGTdrepiD0tnHCVKxhyV6nQIoJiC9qQlac")
    FSUB = getenv("FSUB", "apz_bots")
    CHID = int(getenv("CHID", "-100172778261"))
    SUDO = list(map(int, getenv("SUDO", "l1729415252").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Testing01:Testing01@cluster0.rstjt.mongodb.net/?retryWrites=true&w=majority")
    WEB_SERVER = getenv("WEB_SERVER", True)
    PORT = int(getenv("PORT", 8080))
cfg = Config()
