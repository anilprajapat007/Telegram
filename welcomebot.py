import os
import logging
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Logging enable karo
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Environment Variables
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

app = Flask(__name__)

bot_app = Application.builder().token(TOKEN).build()

# Group Rules
GROUP_RULES = """
📢 *Grp Rules...* 📢
👉 [Join Now](https://t.me/onyourdemand007)
*ThnQ 😊😊*
"""

async def start(update: Update, context):
    await update.message.reply_text("Hello! I am your Welcome Bot. Add me to a group, and I'll welcome new users!")

async def welcome(update: Update, context):
    for new_member in update.message.new_chat_members:
        welcome_text = f"👋 Welcome, {new_member.first_name} जी ! 🎉\n\n{GROUP_RULES}"
        logger.info(f"New user joined: {new_member.first_name}")
        await update.message.reply_text(welcome_text, parse_mode="Markdown", disable_web_page_preview=True)

bot_app.add_handler(CommandHandler("start", start))
bot_app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome))

# ✅ Root Route (Fix for 404 Error)
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Telegram Webhook Bot!", 200

# ✅ Webhook Route
@app.route(f"/{TOKEN}", methods=["POST"])
async def webhook():
    update = Update.de_json(request.get_json(force=True), bot_app.bot)
    await bot_app.process_update(update)
    return "OK", 200

if __name__ == "__main__":
    bot_app.run_webhook(
        listen="0.0.0.0",
        port=int(os.environ.get("PORT", 10000)),
        webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
    )
