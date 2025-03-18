import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Logging enable karein
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Environment Variable Load karo
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # 🔒 Secure way to load the token

# Group Rules (MarkdownV2 Safe)
GROUP_RULES = """
📢 *Grp Rules\\.\\.\\.* 📢

1️⃣ Join My [YouTube](https://youtube.com/@iluprajapat?si=sfs4fwo2aQRy0yBI) & [Instagram](https://www.instagram.com/anilkumarbci/profilecard/?igsh=MWR3NW5wNmpvZTR6bQ==) to Get Movies\\.  
   _(Without this, your requests won\\'t be considered\\!)_  
2️⃣ *Only Admin* can upload movies\\. Media upload is restricted\\.  
3️⃣ No External Links Allowed 🚫 \\(For trailers, DM Admin\\)\\.  
4️⃣ No Chatting or Discussion ❌ – Just send movie/web series name\\.  
5️⃣ *Request Format:*  
   \- ✅ *Correct:* `Mirzapur S03`  
   \- ❌ *Wrong:* `Mirzapur`, `Mirazapur`, `Mirzapoor`  
   \- ✅ `Bhag Milkha Bhag 2013` ❌ `Bhag Milkha Bhag` _(Year Required)_  
6️⃣ Most movies are already uploaded\\! 🔍 Search the group before requesting\\.  

🎬 *Share this group* with friends & family to get the latest movies & web series\\!  
👉 [Join Now](https://t.me/onyourdemand007)

*ThnQ 😊😊*
"""

async def start(update, context):
    """Start command ka response"""
    await update.message.reply_text(
        "Hello! I am your Welcome Bot. Add me to a group, and I'll welcome new users!"
    )

async def welcome(update, context):
    """New members ke liye welcome message & rules"""
    for new_member in update.message.new_chat_members:
        welcome_text = f"👋 Welcome, {new_member.first_name} जी \\! 🎉\n\n{GROUP_RULES}"
        logger.info(f"New user joined: {new_member.first_name}")
        await update.message.reply_text(welcome_text, parse_mode="MarkdownV2", disable_web_page_preview=True)

def main():
    """Bot ko start karne ka function"""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    logger.info("Bot started successfully... Waiting for messages")
    
    app.run_polling()

if __name__ == '__main__':
    main()
