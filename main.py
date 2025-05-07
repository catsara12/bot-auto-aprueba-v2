import os
from telegram.ext import ApplicationBuilder, ChatJoinRequestHandler, ContextTypes

# Leer el token desde la variable de entorno
TOKEN = os.environ["TOKEN"]

async def auto_approve(update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await context.bot.approve_chat_join_request(
            chat_id=update.chat_join_request.chat.id,
            user_id=update.chat_join_request.from_user.id
        )
        print(f"Aprobado: {update.chat_join_request.from_user.username}")
    except Exception as e:
        print(f"Error al aprobar solicitud: {e}")

# Crear la app del bot y agregar el manejador de aprobaciones
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(ChatJoinRequestHandler(auto_approve))

print("Bot iniciado correctamente. Esperando solicitudes...")
app.run_polling()
