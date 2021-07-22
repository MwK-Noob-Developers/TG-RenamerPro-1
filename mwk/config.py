import os 

class Config(object):
  APP_ID = int(os.environ.get("APP_ID", ""))
  API_HASH = os.environ.get("API_HASH", "")
  TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")
  AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
  DOWNLOAD_LOCATION = "./bot/DOWNLOADS"
  DB_URI = os.environ.get("DATABASE_URL", "")
  OWNER_ID = [int(i) for i in os.environ.get("OWNER_ID", "").split(" ")]
  CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION",False)
  UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1271358814))
  MONGODB_URI = os.environ.get("MONGODB_URI", "")
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True)) 
