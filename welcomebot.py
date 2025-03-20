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

# Group Rules (Fixed MarkdownV2 Issues)
GROUP_RULES = """
📢 *ग्रुप के नियम* 📢

1️⃣ *ज़रूरी नियम* – मूवीज़ की रिक्वेस्ट करने के लिए हमारे [YouTube चैनल](https://youtube.com/@iluprajapat) और [Instagram](https://www.instagram.com/anilkumarbci/) को जॉइन करें।  
   _(बिना इसके आपकी रिक्वेस्ट स्वीकार नहीं होगी\!)_

2️⃣ *सिर्फ़ एडमिन* मूवी अपलोड कर सकते हैं। ग्रुप में मीडिया अपलोड करने की अनुमति नहीं है।

3️⃣ *कोई बाहरी लिंक शेयर न करें* 🚫 – ट्रेलर लिंक आदि के लिए एडमिन से DM में संपर्क करें।

4️⃣ *चैटिंग या अनावश्यक चर्चा न करें* ❌ – बस मूवी या वेब सीरीज़ का नाम भेजें।

5️⃣ *रिक्वेस्ट फॉर्मेट:*  
   - ✅ *सही:* `Mirzapur S03`  
   - ❌ *गलत:* `Mirzapur`, `Mirazapur`, `Mirzapoor`  
   - ✅ `Bhag Milkha Bhag 2013` ❌ `Bhag Milkha Bhag` _(साल लिखना अनिवार्य है\)_

6️⃣ *अधिकतर मूवीज़ पहले से अपलोडेड हैं\!* 🔍 रिक्वेस्ट करने से पहले ग्रुप में सर्च करें।

📌 *लेटेस्ट मूवीज़ और वेब सीरीज़ के लिए ग्रुप शेयर करें\!*  
👉 [अभी जॉइन करें](https://t.me/onyourdemand007) | 📲 *शेयर करें*

धन्यवाद\! 😊🎬
"""

async def start(update, context):
    """Respond to /start command"""
    await update.message.reply_text(
        "Hello! I am your Welcome Bot. Add me to a group, and I'll welcome new users!"
    )

async def welcome(update, context):
    """Send welcome message to new group members"""
    for new_member in update.message.new_chat_members:
        welcome_text = f"👋 Welcome, {new_member.first_name} जी\! 🎉\n\n{GROUP_RULES}"
        logger.info(f"New user joined: {new_member.first_name}")
        await update.message.reply_text(
            welcome_text, parse_mode="MarkdownV2", disable_web_page_preview=True
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
