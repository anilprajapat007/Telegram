import logging
import os
from dotenv import load_dotenv
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Logging setup
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")  # Secure way to load the bot token

# Group Rules Message
GROUP_RULES = """📢 *Welcome to the Group!* 🎉

🔹 Please follow the group rules:
1️⃣ *Respect Everyone* - No abusive language.
2️⃣ *No Spamming* - Avoid repeated messages.
3️⃣ *Stay on Topic* - Discussions should be relevant.
4️⃣ *No Promotions* - Unapproved links are not allowed.

🔹 Enjoy your stay and have fun! 😃

👉 [Join Now](https://t.me/onyourdemand007) for more updates.

*Thank You & Have a Great Time!* 😊😊
"""

async def start(update, context):
    """Respond to /start command"""
    await update.message.reply_text(
        "Hello! I am your Welcome Bot. Add me to a group, and I'll welcome new users!"
    )

async def welcome(update, context):
    """Send welcome message to new group members"""
    for new_member in update.message.new_chat_members:
        welcome_text = f"👋 Welcome, {new_member.first_name} जी ! 🎉\n\n{GROUP_RULES}"
        logger.info(f"New user joined: {new_member.first_name}")
        await update.message.reply_text(
            welcome_text, parse_mode="Markdown", disable_web_page_preview=True
        )

def main():
    """Start the bot"""
    app = Application.builder().token(TOKEN).build()

    # Add command and message handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

    logger.info("Bot started successfully... Waiting for messages")

    # Enable polling method
    app.run_polling()

if __name__ == '__main__':
    main()
