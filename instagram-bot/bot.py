from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class InstagramBot:
    def __init__(self, username, password, user_list, message):
        self.username = username
        self.password = password
        self.user_list = user_list
        self.message = message
        self.base_url = 'https://www.instagram.com/'
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        self.driver.get(self.base_url)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'username'))
        ).send_keys(self.username)

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'password'))
        ).send_keys(self.password + Keys.RETURN)

        time.sleep(5)

        # Pop-up "Salvar informações?"
        try:
            self.driver.find_element(By.XPATH, '//button[contains(text(), "Agora não")]').click()
        except:
            pass
        time.sleep(2)

        # Pop-up "Ativar notificações?"
        try:
            self.driver.find_element(By.XPATH, '//button[contains(text(), "Agora não")]').click()
        except:
            pass
        time.sleep(2)

    def send_messages(self):
        # Ir para Direct
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "/direct/inbox")]'))
        ).click()
        time.sleep(3)

        for user in self.user_list:
            try:
                # Clique no botão do lápis para nova mensagem
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "wpO6b")]'))
                ).click()
                time.sleep(2)

                # Digitar o nome do usuário
                search_box = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.NAME, 'queryBox'))
                )
                search_box.clear()
                search_box.send_keys(user)
                time.sleep(2)

                # Clicar no usuário encontrado
                self.driver.find_element(By.XPATH, f'//div[text()="{user}"]').click()
                time.sleep(1)

                # Avançar
                self.driver.find_element(By.XPATH, '//div[contains(text(), "Avançar")]').click()
                time.sleep(2)

                # Digitar mensagem
                text_area = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, 'textarea'))
                )
                text_area.send_keys(self.message)
                time.sleep(1)
                text_area.send_keys(Keys.RETURN)
                print(f"[✔] Mensagem enviada para: {user}")
                time.sleep(2)

            except Exception as e:
                print(f"[✘] Falha ao enviar para {user}: {e}")
                continue
