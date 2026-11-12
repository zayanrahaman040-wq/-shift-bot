import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Ciao! Sono online ✅\nScrivi /turno per vedere il turno")

async def turno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Turno di oggi: da impostare!")

def main():
    token = os.environ.get("TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("turno", turno))
    print("Bot avviato...")
    app.run_polling()

if __name__ == "__main__":
    main()
