import logging
import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from dotenv import load_dotenv

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

# Flask app initialize karo
app = Flask(__name__)

# Initialize Telegram Bot
bot_app = Application.builder().token(TOKEN).build()

# Start Command Function
async def start(update: Update, context):
    """Start command ka response"""
    await update.message.reply_text(
        "Hello! I am your Welcome Bot. Add me to a group, and I'll welcome new users!"
    )

# Welcome Message Function
async def welcome(update: Update, context):
    """New members ke liye welcome message & rules"""
    for new_member in update.message.new_chat_members:
        welcome_text = f"👋 Welcome, {new_member.first_name} जी ! 🎉\n\n{GROUP_RULES}"
        logger.info(f"New user joined: {new_member.first_name}")
        await update.message.reply_text(welcome_text, parse_mode="Markdown", disable_web_page_preview=True)

# Handlers Add Karo
bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    """Webhook handler for Telegram bot"""
    if request.data:
        update = Update.de_json(request.get_json(), bot_app.bot)
        bot_app.update_queue.put(update)
    return "OK", 200

if __name__ == '__main__':
    # Webhook Set Karo
    WEBHOOK_URL = f"https://your-app-name.onrender.com/{TOKEN}"
    bot_app.bot.set_webhook(url=WEBHOOK_URL)

    # Flask app ko start karo
    app.run(host="0.0.0.0", port=5000)
