from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "14013342"))
    API_HASH = getenv("API_HASH", "c3e1d740fd207c7ae1b373a7546e8a62")
    BOT_TOKEN = getenv("BOT_TOKEN", "6242127744:AAH18hEaFYTsAF6gggXyFXe5MoU63EMtAhY")
    FSUB = getenv("FSUB", "robotech_bots")
    CHID = int(getenv("CHID", "-1001865881963"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://akshatsingh:xsP1Ri7unyWnEGOY@cluster0.5hcq2s4.mongodb.net/?retryWrites=true&w=majority")
    WEB_SERVER = getenv("WEB_SERVER", True)
    PORT = int(getenv("PORT", 8080))
cfg = Config()
