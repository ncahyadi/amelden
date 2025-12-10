from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Halo! Selamat datang di Angkatan Laut JALESVEVA JAYAMAHE!!.")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Gunakan /start untuk memulai bot.")

async def amelden(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Selamat malam mohon ijin memperkenalkan diri dengan kami Letda Laut (E) Abdul Aziz Anaoval. S.Kom NRP 2225101020028400 PAPK 32  Alumni Universitas Pelita Bangsa Jurusan Teknik Informatika asal Bekasi selanjutnya mohon ijin arahan terimakasih mohon ijin")


if __name__ == '__main__':
    TOKEN = '8519079354:AAEUNohS_GpCUjlIOn6JHyi02cw-N_F9IJM'

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("amelden", amelden))
    app.run_polling()
