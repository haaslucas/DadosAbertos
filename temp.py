import requests

# CARGA GLOBAL VERIFICADA
url = 'https://apicarga.ons.org.br/prd/cargaverificada?dat_inicio=2024-01-01&dat_fim=2024-02-01&cod_areacarga=NE'


# Cabeçalhos da requisição
headers = {
    'accept': 'application/json'
}

# Fazendo a requisição GET
response = requests.get(url, headers=headers)

# Verificando se a requisição foi bem-sucedida
if response.status_code == 200:
    # Convertendo a resposta em JSON
    data = response.json()
    # Exibindo os dados (ou você pode salvá-los em um arquivo, processá-los, etc.)
    print(data)
else:
    print(f"Erro na requisição: {response.status_code}")

a=1