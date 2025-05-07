from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

TOKEN = "7297046332:AAFpi4TDuTfoZYEAZdbeHnOXXE1qdgDfHVk

"

async def auto_approve(update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.approve_chat_join_request(update.chat_join_request.chat.id, update.chat_join_request.from_user.id)
        print(f"Aprobado: {update.chat_join_request.from_user.username}")
    except Exception as e:
        print(f"Error al aprobar solicitud: {e}")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(auto_approve))
print("Bot iniciado correctamente. Esperando solicitudes...")
app.run_polling()
