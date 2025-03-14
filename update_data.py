import requests
import yaml

# Exemplo: Coleta dados do MXRF11 do Fundamentus
url = "https://www.fundamentus.com.br/detalhes.php?papel=MXRF11"
response = requests.get(url)
# ... parse da página com BeautifulSoup ...

# Salva em YAML
with open("_data/fiis.yml", "w") as f:
    yaml.dump(dados, f)