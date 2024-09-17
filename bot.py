# bot.py

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import config

# WhatsApp bot class
class WhatsApp:
    def init(self):
        options = Options()
        options.add_argument('--headless')  # Run in headless mode for AWS EC2
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')  # Disable GPU
        self.driver = webdriver.Chrome(executable_path=config.WEBDRIVER_PATH, options=options)

    def open_whatsapp(self):
        self.driver.get('https://web.whatsapp.com')
        input("Press Enter after scanning the QR code")

    def get_unread_chats(self):
        # Code to find unread chats goes here (simplified for this example)
        print("Checking for unread chats...")
        return ['Example Chat']

    def get_chat_name(self, chat):
        # Return the name of the chat
        return chat

    def send_message(self, chat_name, message):
        print(f"Sending message to {chat_name}: {message}")
        # Code to send message to the chat_name on WhatsApp goes here


# Start the bot and open WhatsApp Web
whatsapp = WhatsApp()
whatsapp.open_whatsapp()

# Auto-reply function
def auto_reply():
    print("Checking for new messages...")
    unread_chats = whatsapp.get_unread_chats()
    
    if unread_chats:
        for chat in unread_chats:
            chat_name = whatsapp.get_chat_name(chat)
            print(f"Replying to {chat_name}")
            whatsapp.send_message(chat_name, config.OFFLINE_MESSAGE)
            time.sleep(1)  # Short delay between replies to avoid spamming

# Main loop to keep checking for new messages
while True:
    try:
        auto_reply()
        time.sleep(config.CHECK_INTERVAL)  # Check for new messages every defined interval
    except KeyboardInterrupt:
        print("Bot stopped.")
        break
