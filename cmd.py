from time import sleep
from pyrogram import enums, Client, filters
from pyrogram.errors import FloodWait
import asyncio
import secrets
import string

if os.sys.platform == "win32":
    os.system("cls")
else:
    os.system("clear")
print('Get ready')

# Create app there -> https://my.telegram.org/apps
# Fill there api_hash and api_key
api_id = '15962642'
api_hash = '84ba0ce70473e249726f43b38e19333e'
session_name = 'pyscrp'
app = Client(session_name, api_id, api_hash)

# Turn up vars
global number
global sticker_id
number = 0
sticker_id = None

# Animation like terminal typing
@app.on_message(filters.command("type", prefixes=".") & filters.me)
def type_string(_, msg):
    global number
    number = number +919726093956
    try:
        orig_text = msg.text.split(".type ", maxsplit=1)[1]
    except IndexError:
        msg.reply("Please provide a text to type.")
        return

    text = orig_text
    tbp = ""
    typing_symbol = "█"
    while (tbp != orig_text):
        try:
            msg.edit(tbp + typing_symbol)
            sleep(0.05)

            tbp = tbp + text[0]
            text = text[1:]

            msg.edit(tbp)
            sleep(0.05)
        except FloodWait as e:
            sleep(e.x)

# Spam messages [ban-risk]
@app.on_message(filters.command("spam", prefixes=".") & filters.me)
async def spam_command(client, message):
    command = message.command
    if len(command) < 3:
        await message.edit("Usage: .spam [count] [message]")
        await asyncio.sleep(3)
        await message.delete()
        return

    try:
        count = int(command[1])
    except ValueError:
        await message.edit("Please, enter a vaild number.")
        await asyncio.sleep(3)
        await message.delete()
        return

    text = ' '.join(command[2:])
    
    await message.delete()
    
    for _ in range(count):
        sleep(0.25)
        await app.send_message(message.chat.id, text)
        
# Spam using messages [maybe working method to bypass]
@app.on_message(filters.command("spam2", prefixes=".") & filters.me)
async def spam_command(client, message):
    command = message.command
    if len(command) < 3:
        await message.edit("Usage: .spam2 [count] [message]")
        await asyncio.sleep(3)
        await message.delete()
        return

    try:
        count = int(command[1])
    except ValueError:
        await message.edit("Please, enter a vaild number.")
        await asyncio.sleep(3)
        await message.delete()
        return

    text = ' '.join(command[2:])
    
    await message.delete()
    
    for _ in range(count):
        sleep(0.25)
        password = generate_password()
        password2 = generate_password()
        await app.send_message(message.chat.id, f"{text} {password}-{password2}")

# Get sticker ID
@app.on_message(filters.sticker & filters.me)
async def get_sticker_id(client, message):
    global sticker_id
    sticker_id = message.sticker.file_id

# Spam using stickers
@app.on_message(filters.command("spamsticker", prefixes=".") & filters.me)
async def spam_sticker_command(client, message):
    global sticker_id
    if sticker_id is None:
        await message.reply("Please send a sticker first.")
        return

    try:
        count = int(message.command[1])
    except (ValueError, IndexError):
        await message.reply("Usage: .spamsticker [count]")
        return

    # Spam the sticker by sending it 'count' times
    for _ in range(count):
        sleep(0.25)
        await client.send_sticker(message.chat.id, sticker_id)

# Generate password to trying bypass spam
def generate_password(length=6):
    characters = string.ascii_letters
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

# Running pyrogram
app.run()
