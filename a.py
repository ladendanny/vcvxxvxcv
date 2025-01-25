from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace these values with your credentials
BOT_TOKEN = "7948105366:AAFXxQjU_zCCa0oi5YoyeH5BtLmNKdYLjic"
USER_ID = 6033462267
GROUP_CHAT_ID = -4712142394

# Function to handle incoming messages
def handle_message(update: Update, context: CallbackContext):
    if update.effective_user.id == USER_ID:
        # Forward message to the group chat
        context.bot.send_message(chat_id=GROUP_CHAT_ID, text=update.message.text)
        update.message.reply_text("Message broadcasted to the group chat!")
    else:
        update.message.reply_text("/")

# Start command
def start(update: Update, context: CallbackContext):
    if update.effective_user.id == USER_ID:
        update.message.reply_text("./")
    else:
        update.message.reply_text("/")

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Add handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    # Start the bot
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    main()
