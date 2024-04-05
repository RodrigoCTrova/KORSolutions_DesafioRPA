from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui

def realizar_insercoes_AWS():

    # Parâmetros de inserção
    regiao = "Leste dos EUA (N. da Virg"
    arquitetura = "x86"
    numsolicitacoes = "1000"
    unidade = "por dia"
    duracao = "3000"
    valor_memoria = "512"
    unidade_memoria = "MB"
    valor_armatemp = "512"
    unidade_armatemp = "MB"

    # Configurando as opções do Chrome para evitar a detecção automatizada
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Inicializando o driver do Chrome com as opções configuradas
    driver = webdriver.Chrome(options=options)
    
    # Maximizando a janela do navegador
    driver.maximize_window()
    
    # Abrindo a página da calculadora AWS
    driver.get("https://calculator.aws/#/createCalculator/Lambda")
    
    # Definindo um tempo de espera máximo para aguardar a página carregar
    wait = WebDriverWait(driver, 10)

    # Aguardando até que um elemento específico na janela seja visível
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "awsui_trigger_dwuol_18p6o_122")))
    
    #Início das inserções

    # Campo: "Escolher uma região"

    # Encontrando todos os elementos com a classe do campo
    elementos = driver.find_elements(By.CLASS_NAME, "awsui_trigger_dwuol_18p6o_122")

    # Selecionando o segundo elemento da lista
    segundo_elemento = elementos[1]

    # Inserindo o valor no segundo elemento
    time.sleep(3)
    segundo_elemento.click()
    pyautogui.typewrite(regiao)
    time.sleep(3)
    pyautogui.press('down')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(2)

    # Campo: "Função do Lambda"

    # Encontrando todos os elementos com a classe do campo
    funclambda = driver.find_elements(By.CLASS_NAME, "awsui_native-input_1wepg_1bxgk_116")[1]

    # Selecionando "Função do Lambda - Sem nível gratúito"
    funclambda.click()
    time.sleep(2)

    # Campo: "Arquitetura"

    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('tab')

    # Inserindo valor
    time.sleep(1)
    pyautogui.typewrite(arquitetura)
    time.sleep(1)
    pyautogui.press(['enter', 'enter'])
    time.sleep(1)

    # Campo: "Número de Solicitações"

    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)

    # Inserindo valor
    pyautogui.typewrite(numsolicitacoes)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # Campo: "Unidade"

    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)
    
    # Inserindo valor
    pyautogui.typewrite(unidade)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # Campo: "Duração de cada solicitação"

    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)
    
    # Inserindo valor
    pyautogui.typewrite(duracao)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # Campo: "ValorMemoria"

    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)
    
    # Inserindo valor
    pyautogui.typewrite(valor_memoria)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # Campo: "UnidadeMemoria"
    
    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)
    
    # Inserindo valor
    pyautogui.typewrite(unidade_memoria)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # Campo: "ValorArmaTemp"

    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)
    
    # Inserindo valor
    pyautogui.typewrite(valor_armatemp)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)

    # Campo: "UnidadeArmaTemp"

    # Navegando ao campo
    pyautogui.press('tab')
    time.sleep(1)
    
    # Inserindo valor
    pyautogui.typewrite(unidade_armatemp)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

    # Click no botão "Salvar e vizualizar resumo"

    salvar = driver.find_elements(By.CLASS_NAME, "awsui_content_vjswe_2od9j_103")[3]
    salvar.click()
    time.sleep(3)

    # Click no botão "Exportar"
    exportar = driver.find_elements(By.CLASS_NAME, 'awsui_content_vjswe_2od9j_103')[2]
    exportar.click()
    time.sleep(2)

    # Selecionando o item "JSON"
    json = driver.find_elements(By.CLASS_NAME, 'awsui_menu-item_93a1u_1rwbp_158')[2]
    json.click()
    time.sleep(3)

    # Confirmando o download
    download = driver.find_elements(By.CLASS_NAME, 'awsui_content_vjswe_2od9j_103')[23]
    download.click()

# Chamando a função para realizar a busca na página da calculadora AWS
realizar_insercoes_AWS()
