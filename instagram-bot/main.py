from bot import InstagramBot
from dotenv import load_dotenv
import os

# Carregar .env
load_dotenv()

# Credenciais do Instagram
username = os.getenv("IG_USERNAME")
password = os.getenv("IG_PASSWORD")

# Lista de usuários e mensagem
user_list = ['usuario1', 'usuario2']  # Substitua por usernames reais
message = "Olá, tudo bem? Esta é uma mensagem automática de teste."

def main():
    bot = InstagramBot(username, password, user_list, message)
    bot.login()
    bot.send_messages()
    input("Bot finalizado. Pressione Enter para sair.")

if __name__ == "__main__":
    main()
