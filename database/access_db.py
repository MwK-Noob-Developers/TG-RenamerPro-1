from mwk.config import Config
from database.database import Database

db = Database(Config.MONGODB_URI, Config.SESSION_NAME)
