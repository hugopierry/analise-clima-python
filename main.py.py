# Biblioteca pra fazer requisições HTTP (consultar a API)
import requests
# Acessa variáveis do sistema (usado pra ler a chave da API)
import os
# Carrega as variáveis do arquivo .env
from dotenv import load_dotenv
# Console do rich: imprime com cores e estilos
from rich.console import Console
# Panel: desenha a caixa em volta do conteúdo
from rich.panel import Panel

# Objeto usado pra imprimir com o rich
console = Console()

# Lê o arquivo .env e deixa as variáveis disponíveis
load_dotenv()
# Pega a chave da API do .env (assim ela não fica exposta no código)
chave_api = os.getenv("CHAVE_API")
# Endereço da API (endpoint do clima atual)
link_api = "http://api.weatherapi.com/v1/current.json"

# Parâmetros que vão na URL da consulta
parametros = {
    "key": chave_api,    # sua chave de acesso
    "q": "auto:ip",  # cidade consultada
    "lang": "pt",        # idioma da descrição do clima
}

# Faz a requisição GET e guarda a resposta
resposta = requests.get(link_api, params=parametros)

# 200 = a API respondeu com sucesso
if resposta.status_code == 200:
    # Converte a resposta de JSON para dicionário Python
    dados_requisicao = resposta.json()

    # Extrai cada dado navegando pelo dicionário: ["bloco"]["campo"]
    temp = dados_requisicao["current"]["temp_c"]                    # temperatura em °C
    desricao = dados_requisicao["current"]["condition"]["text"]     # descrição (ex.: "Chuva fraca")
    umidade = dados_requisicao["current"]["humidity"]               # umidade em %
    vento = dados_requisicao["current"]["wind_kph"]                 # vento em km/h
    sensacao_termica = dados_requisicao["current"]["feelslike_c"]   # sensação térmica em °C
    cidade = dados_requisicao["location"]["name"]                   # nome da cidade
    data_hora = dados_requisicao["location"]["localtime"]           # data e hora local

    # Monta o texto de dentro do painel (f-string + \n pra quebrar linha)
    conteudo = (
        f"{temp}°C\n"
        f"\nVento: {vento} km/h\n"
        f"Sensação: {sensacao_termica}º\n"
        f"Umidade: {umidade}%\n\n"
        f"\n[bold][/bold]{desricao}"  # [bold][/bold] está vazio: não deixa nada em negrito
    )

    # Imprime o painel
    console.print(
        Panel(
            conteudo,                                  # texto de dentro
            title="CLIMA TEMPO",                       # título na borda de cima
            subtitle=f"{cidade}•{data_hora} ",         # subtítulo na borda de baixo
            expand=False,                              # caixa se ajusta ao texto
            border_style="sky_blue1",                  # cor da borda
            padding=(1, 2),                            # espaço interno (vertical, horizontal)
        )
    )
# Se a API não respondeu 200, mostra o erro em vermelho
else:
    console.print(f"[red]Erro ao consultar a API (código {resposta.status_code}).[/red]")

# 7 linhas em branco seguidas (empurram o texto de baixo)
print()
print()
print()
print()
print()
print()
print()
# Segura a janela aberta até apertar ENTER
input("Pressione ENTER para sair do programa.")