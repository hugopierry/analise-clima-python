import requests
import os
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel

console = Console()

load_dotenv()
chave_api = os.getenv("CHAVE_API")
link_api = "http://api.weatherapi.com/v1/current.json"

parametros = {
    "key": chave_api,
    "q": "Carapicuiba",
    "lang": "pt",
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    temp = dados_requisicao["current"]["temp_c"]
    desricao = dados_requisicao["current"]["condition"]["text"]
    umidade = dados_requisicao["current"]["humidity"]
    vento = dados_requisicao["current"]["wind_kph"]
    sensacao_termica = dados_requisicao["current"]["feelslike_c"]
    cidade = dados_requisicao["location"]["name"]
    data_hora = dados_requisicao["location"]["localtime"]

    conteudo = (
        f"{temp}°C\n"
        f"\nVento: {vento} km/h\n"
        f"Sensação: {sensacao_termica}º\n"
        f"Umidade: {umidade}%\n\n"
        f"\n[bold][/bold]{desricao}"
    )

    console.print(
        Panel(
            conteudo,
            title="CLIMA TEMPO",
            subtitle=f"{cidade}•{data_hora} ",
            expand=False,
            border_style="sky_blue1",
            padding=(1, 2),
        )
    )
else:
    console.print(f"[red]Erro ao consultar a API (código {resposta.status_code}).[/red]")
print()
print()
print()
print()
print()
print()
print()
input("Pressione ENTER para sair do programa.")