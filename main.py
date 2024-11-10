import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

# Bot token can be obtained via https://t.me/BotFather
TOKEN = getenv("7201255244:AAFTd8wbPAJA3N1FjjGpvPtayk_bxSPdEIc")

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()




async def main() -> None:

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())