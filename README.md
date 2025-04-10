# 🤖 Bot de Mensagens para Instagram com Python

Este projeto automatiza o envio de mensagens no Instagram utilizando **Python** e **Selenium WebDriver**.

## 🚀 Requisitos

- Python 3.x instalado  
- Google Chrome instalado  
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) compatível com a versão do seu navegador  

## 📦 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seuusuario/instagram-bot.git
cd instagram-bot
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Crie um arquivo `.env` na raiz do projeto e adicione suas credenciais do Instagram:

```env
INSTA_USER=seu_usuario
INSTA_PASS=sua_senha
```

## ▶️ Como usar

Execute o bot com o comando:

```bash
python main.py
```

O bot irá:

- Abrir o site do Instagram  
- Fazer login com suas credenciais  
- Acessar a lista de usuários definida no código (variável `audience`)  
- Enviar mensagens privadas automaticamente  

## ⚠️ Avisos Importantes

- Use com moderação para evitar bloqueios por parte do Instagram  
- A automação de interações pode violar os termos de uso do Instagram  
- Este projeto tem finalidade **educacional** e é de uso pessoal  

---
