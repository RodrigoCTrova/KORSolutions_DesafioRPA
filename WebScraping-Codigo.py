from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import json

# Configuração do Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Executando em modo headless (sem interface gráfica)
driver = webdriver.Chrome(options=options)

# URL da página da Wikipédia
url = 'https://pt.wikipedia.org/wiki/Monty_Python'

# Extraindo o HTML da página
driver.get(url)
html = driver.page_source

# Fechar o navegador
driver.quit()

# Parseando o conteúdo HTML
soup = BeautifulSoup(html, 'html.parser')

# Função para extrair conteúdo de um elemento BeautifulSoup
def extract_content(element):
    # Extrair texto e links
    text = element.get_text(strip=True)
    links = {a.text: 'https://pt.wikipedia.org' + a['href'] for a in element.find_all('a', href=True)}
    return {'title': '', 'content': text, 'hyperlinks': links}

# Verificando se o link leva para a mesma página
def is_internal_link(link):
    parsed_link = urlparse(link)
    return parsed_link.netloc == '' and parsed_link.path.startswith('/wiki/')

# Extraindo o título da página
header = soup.find('h1', {'id': 'firstHeading'}).text.strip()

# Extraindo os dados da infobox
infobox = []
infobox_table = soup.find('table', {'class': 'infobox'})
if infobox_table:
    rows = infobox_table.find_all('tr')
    for row in rows:
        cells = row.find_all(['th', 'td'])
        if len(cells) == 2:
            raw_text = cells[0].get_text(strip=True)
            content = extract_content(cells[1])
            infobox.append({'raw_text': raw_text, 'hyperlinks': {}, 'text_content': content})
        elif len(cells) == 1:  # Caso tenha apenas uma célula, considera como parte do conteúdo
            raw_text = row.get_text(strip=True)
            if raw_text.strip():  # Verifica se o texto não está vazio
                content = extract_content(row)
                infobox.append({'raw_text': raw_text, 'hyperlinks': {}, 'text_content': content})

# Extraindo o conteúdo do artigo
article = {}
current_section = None
current_subsection = None  # Inicializa a variável current_subsection
for element in soup.find_all(['h2', 'h3', 'p']):  # Seções, subseções e parágrafos
    # Nova seção
    if element.name == 'h2':
        section_title = element.get_text(strip=True)
        article[section_title] = []
        current_section = section_title
        current_subsection = None  # Reseta a variável current_subsection ao iniciar uma nova seção
    # Nova subseção
    elif element.name == 'h3':
        subsection_title = element.get_text(strip=True)
        article[current_section].append({'type': 'subsection', 'title': subsection_title, 'content': []})
        current_subsection = article[current_section][-1]['content']
    # Parágrafo
    elif element.name == 'p':
        content = extract_content(element)
        if current_section:
            if current_subsection:  # Se houver subseção atual, adiciona ao conteúdo dela
                current_subsection.append({'type': 'paragraph', **content})
            else:  # Caso contrário, adiciona diretamente à seção
                article[current_section].append({'type': 'paragraph', **content})

# Extraindo as referências
references = {}
references_section = soup.find('ol', {'class': 'references'})
if references_section:
    for i, reference in enumerate(references_section.find_all('li')):
        reference_text = reference.get_text(strip=True)
        reference_links = {f'link_{i + 1}': 'https://pt.wikipedia.org' + a['href'] for a in reference.find_all('a', href=True) if not is_internal_link(a['href'])}
        references[reference_text] = reference_links

# Construindo o JSON
data = {
    'header': header,
    'infobox': infobox,
    'article': article,
    'references': references
}

# Escrever o JSON em um arquivo
output_path = r'C:\Users\Usuario\Desktop\Teste_RPA_KOR\ResultadoDaExtracao_JSON.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f'JSON gerado com sucesso em: {output_path}')