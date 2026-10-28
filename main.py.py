import requests
import pprint
import os
from dotenv import load_dotenv


load_dotenv()
chave_api = os.getenv("CHAVE_API")
link_api = "http://api.weatherapi.com/v1//current.json"


parametros = {
    "key" : chave_api,
    "q": "São Paulo",
    "lang": "pt",
    
}

resposta = requests.get(link_api, params=parametros)

if resposta.status_code == 200:
    dados_requisicao = resposta.json()
    # pprint.pprint(dados_requisicao)
    temp = dados_requisicao["current"]['temp_c']
    desricao = dados_requisicao['current']['condition']['text']
    umidade = dados_requisicao['current']['humidity']
    vento = dados_requisicao['current']['wind_kph']
    sensacao_termica = dados_requisicao['current']['windchill_c']
    cidade = dados_requisicao["location"]["region"]
    pais = dados_requisicao["location"]["country"]
    data_hora = dados_requisicao["location"]['localtime']

    print("—"*50)
    print("CLIMA TEMPO".center(50))
    print(f"\n\n📍{cidade}, {pais}.")
    print(f"🕒 Última atualização: {data_hora}")
    print("—"*30)
    print(f"\n🌡️ Tempreratura: {temp}°")
    print(f"💨 Vento: {vento} km/h")
    print(f"🌡️ Sensação Térmica: {sensacao_termica}º")
    print(f"💧 Umidade: {umidade}%")
    print("—"*30)
    print(f"\n🌤️  {desricao}.".center(50))

input("\n\n\n\nPressione ENTER para sair do program.")
   
    



