import os
import logging
from logging.handlers import RotatingFileHandler




BOT_TOKEN = os.environ.get("BOT_TOKEN", "8148883828:AAG3l7ML6HT3kxVzUoenR2R-X1GpC-lsnGo")
API_ID = int(os.environ.get("API_ID", "27642526"))
API_HASH = os.environ.get("API_HASH", "8bc14441805c29b64843165c1d73ce31")


OWNER_ID = int(os.environ.get("OWNER_ID", "7653921320"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://Itachidb:12345@cluster0.ej2egtd.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "Itachidb")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1003169580929"))

FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", "-1003139985943"))

FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", "-1002566730080"))

FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", "-1002434474630"))

FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", "-1003043264664"))

START_PIC = os.environ.get("START_PIC", "https://ibb.co/kg45hQN4")
F_PIC = os.environ.get("FORCE_PIC", "https://i.ibb.co/671SqSMt/x.jpg")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds
AUTO_DELETE_MSG = int(os.getenv("AUTO_DELETE_MSG", "❗️ IMPORTANT ❗️

This Video / File Will Be Deleted In 20 minutes (Due To Copyright Issues).

📌 Please Forward This Video / File To Somewhere Else And Start Downloading There."))


PORT = os.environ.get("PORT", "8050")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[6299192020 ,6016699737, 5000956033]
    for x in (os.environ.get("ADMINS", "6462248335").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', None) == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Sry You can't Able to Message me !\n\n» My Owner 👉 @Anime_Paradise

START_MSG = os.environ.get("START_MESSAGE", "<b>Hi {first} Friend I am a Advance File Store bot 😈 \n\n I was created by 👉@Anime_Paradise </b>")

FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "𝐒𝐨𝐫𝐫𝐲 {first} You must join the given channels ..\n\n 𝐒𝐨 please join and  “𝐍𝐨𝐰 𝐂𝐥𝐢𝐜𝐤 𝐡𝐞𝐫𝐞” 𝐛𝐮𝐭𝐭𝐨𝐧....!")




ADMINS.append(OWNER_ID)
ADMINS.append(6299192020)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   

class Txt(object):
    about = f"""<b>😈 My Name :</b> <a href=''>[IF] ItachiFileStore 😈 </a>
<b>📝 Language :</b> <a href='https://python.org'>Python 3</a>
<b>📚 Library :</b> <a href='https://pyrogram.org'>Pyrogram 2.0</a>
<b>🚀 Server :</b> <a href='https://heroku.com'>Heroku</a>
<b>📢 Channel :</b> <a href='https://t.me/+Vv6cGnXmVQo0OTk1'>IV BOTS</a>
<b>🛡️ :</b> <a href='https://t.me/+Vv6cGnXmVQo0OTk1'>IV Developer</a>
    
<b>😈 Bot Made By :</b> @Eren_157"""


# Tech freak 
# Don't Remove Credit!!!
# Telegram Channel @Tech_freak_tamil
# Developer @devilo7
