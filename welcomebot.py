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

# Group Rules
GROUP_RULES = """
📢 *Grp Rules...* 📢
...
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
        welcome_text = f"👋 Welcome, {new_member.first_name} जी ! 🎉\n\n{GROUP_RULES}"
        logger.info(f"New user joined: {new_member.first_name}")
        await update.message.reply_text(welcome_text, parse_mode="Markdown", disable_web_page_preview=True)

def main():
    """Bot ko start karne ka function"""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    logger.info("Bot started successfully... Waiting for messages")
    
    app.run_polling()

if __name__ == '__main__':
    main()
