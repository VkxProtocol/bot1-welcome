import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext

# Configuração de logs (opcional, para monitoramento)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Token do bot e ID do grupo
TOKEN = '[REDACTED_SECRET]'
GROUP_CHAT_ID = '-1002405955713'

# Função para enviar a mensagem de boas-vindas
async def welcome_new_member(update: Update, context: CallbackContext):
    # Verifica se a mensagem vem do grupo correto
    if update.message.chat_id == int(GROUP_CHAT_ID):
        for member in update.message.new_chat_members:
            # Usa @username se disponível, senão usa first_name
            user_display = f"@{member.username}" if member.username else member.first_name
            # Monta a mensagem de boas-vindas
            welcome_message = (
                f"Bem vindo {user_display}! Veja nosso Site e nosso programa de AIRDROP!\n"
                "🌐 Site: https://www.vkinha.com.br\n"
                "🚀 Airdrop: https://www.vkinha.com.br/airdrop"
            )
            # Envia a mensagem no grupo
            await context.bot.send_message(chat_id=update.message.chat_id, text=welcome_message)
            logger.info(f"Mensagem de boas-vindas enviada para {user_display}")

# Função principal para iniciar o bot
def main():
    # Inicializa o bot com o token
    application = Application.builder().token(TOKEN).build()
    # Adiciona o handler para novos membros
    application.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))
    # Inicia o bot com polling
    application.run_polling()

if __name__ == '__main__':
    main()