const TelegramBot = require('node-telegram-bot-api');

// Replace these values with your credentials
const BOT_TOKEN = "7809481260:AAHBUX4j2_xlwwfIxvuzQIu2dlQDcENvA74";
const USER_ID = 6033462267;
const GROUP_CHAT_ID = -4783624680;

// Create a bot instance
const bot = new TelegramBot(BOT_TOKEN, { polling: true });

// Handle incoming messages
bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  const chatType = msg.chat.type;

  // Process messages only if they are from you in a private chat (DM)
  if (chatType === "private" && chatId === USER_ID) {
    // Forward the message to the group chat
    bot.sendMessage(GROUP_CHAT_ID, msg.text)
      .then(() => {
        bot.sendMessage(chatId, "Message broadcasted to the group chat!");
      })
      .catch((error) => {
        console.error("Error broadcasting message:", error);
        bot.sendMessage(chatId, "Failed to broadcast the message.");
      });
  } else if (chatType === "private") {
    // Respond to unauthorized users in private chats
    bot.sendMessage(chatId, "You are not authorized to use this bot.");
  }
  // Ignore group chat messages completely
});

// Notify when the bot starts
console.log("Bot is running...");
