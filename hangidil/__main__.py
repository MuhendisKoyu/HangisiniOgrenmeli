from hangidil.BotConfig import Hangi
import logging
from decouple import config

logging.basicConfig(
    format="%(levelname)s - %(name)s - %(message)s",
    level=logging.getLevelName(config("LOG_LEVEL", default="INFO")),
)

if __name__ == "__main__":
    Hangi().run()

