from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Database sederhana
USER_DATA = {
    "aaa": (
        "Letda Laut (E) Abdul Aziz Anaoval. S.Kom "
        "NRP 2225101020028400 PAPK 32B "
        "Alumni Universitas Pelita Bangsa "
        "Jurusan Teknik Informatika asal Bekasi"
    ),
    "ncy": (
        "Nanang Cahyadi S.T., M.T "
        "NRP 2225104960028409 PAPK 32B "
        "Alumni Institut Teknologi Bandung "
        "Jurusan Rekayasa dan Manajemen Keamanan Informasi asal Purwakarta"
    )
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Halo! Selamat datang di Angkatan Laut JALESVEVA JAYAMAHE!!."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Gunakan /amelden <kode> untuk memperkenalkan diri.\n"
        "Contoh: /amelden aaa"
    )

async def amelden(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Ambil argumen setelah command
    if not context.args:
        await update.message.reply_text(
            "Mohon sertakan kode user.\nContoh: /amelden aaa"
        )
        return

    kode = context.args[0].lower()

    # Cek apakah kode ada di database
    if kode in USER_DATA:
        biodata = USER_DATA[kode]
        await update.message.reply_text(
            f"Selamat malam mohon ijin memperkenalkan diri dengan kami {biodata}. "
            "Selanjutnya mohon ijin arahan terimakasih mohon ijin."
        )
    else:
        await update.message.reply_text(
            f"Kode '{kode}' tidak ditemukan. Silakan cek kembali."
        )

if __name__ == '__main__':
    TOKEN = "8519079354:AAEUNohS_GpCUjlIOn6JHyi02cw-N_F9IJM"

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("amelden", amelden))

    print("Bot berjalan...")
    app.run_polling()
