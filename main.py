import asyncio
import logging
import sys
import random
import os

from aiogram import Bot, Dispatcher, html, types
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, BotCommand, BotCommandScopeDefault

TOKEN = os.getenv("TOKEN")
print(TOKEN)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Привет, {html.bold(message.from_user.full_name)}!")


@dp.message(Command("kitty"))
async def kitty(message: Message) -> None:
    files = os.listdir('cats')
    file = random.choice(files)
    file = 'cats/' + file
    await message.answer_photo(types.FSInputFile(path=file))

@dp.message(Command("puppy"))
async def kitty(message: Message) -> None:
    files = os.listdir('dogs')
    file = random.choice(files)
    file = 'dogs/' + file
    await message.answer_photo(types.FSInputFile(path=file))

@dp.message()
async def echo_handler(message: Message) -> None:
    try:
        await message.answer("Я умею только отправлять картинки с котятами по команде /kitty")
    except TypeError:
        await message.answer("Я умею только отправлять картинки с котятами по команде /kitty")


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    commands = [
        BotCommand(command="start", description="Запустить бота"),
        BotCommand(command="kitty", description="Прислать рандомного котёнка"),
        BotCommand(command="puppy", description="Прислать рандомного щеночка")
    ]
    # scope=BotCommandScopeDefault() означает «для всех пользователей»
    await bot.set_my_commands(commands, scope=BotCommandScopeDefault())

    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())