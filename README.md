# 🌦️ Sistema de Consulta de Clima e Tempo em Python

## 📌 Sobre o projeto

Este projeto consiste em um sistema desenvolvido em Python que consulta uma API meteorológica para obter informações atualizadas sobre as condições do tempo e apresentá-las diretamente no terminal.

Inicialmente, era necessário informar manualmente a cidade no código-fonte. Com a melhoria implementada, o sistema utiliza a localização automática por IP para identificar a região aproximada do usuário e consultar os dados meteorológicos correspondentes, eliminando a necessidade de alterar o código para cada consulta.

O objetivo principal é praticar o consumo de APIs, a obtenção de dados externos e o desenvolvimento de aplicações em Python.

## ⚙️ Funcionalidades

Ao executar o programa, são exibidas as seguintes informações:

- 🌡️ Temperatura atual;
- 🌡️ Sensação térmica;
- 💧 Umidade relativa do ar;
- 💨 Velocidade do vento;
- 🕒 Data e hora local;
- 🌤️ Descrição das condições meteorológicas, como céu encoberto, tempo chuvoso e chuva fraca;
- 📍 Identificação automática da localização aproximada por IP.

## 🛠️ Tecnologias utilizadas

- **Python** — desenvolvimento da aplicação;
- **WeatherAPI** — obtenção dos dados meteorológicos e identificação da localização por IP;
- **Requests** — realização de requisições HTTP;
- **python-dotenv** — leitura de variáveis de ambiente para armazenar a chave da API fora do código-fonte;
- **Rich** — formatação e apresentação das informações no terminal.

## ▶️ Como executar

1. Clone este repositório para sua máquina.
2. Instale as dependências necessárias:

   ```bash
   pip install requests python-dotenv rich
   ```

3. Crie um arquivo `.env` na pasta do projeto e adicione sua chave de acesso:

   ```env
   CHAVE_API=sua_chave_aqui
   ```

4. Execute o arquivo principal pelo terminal:

   ```bash
   python main.py
   ```

**Observação:** substitua `main.py` pelo nome do arquivo principal utilizado no projeto, caso seja diferente. É necessário possuir uma chave válida da WeatherAPI.

## 🎯 Objetivo de aprendizado

Este projeto foi desenvolvido para consolidar conhecimentos em Python e compreender, na prática, como consumir APIs, realizar requisições HTTP, interpretar respostas em JSON e apresentar dados externos de forma organizada.

A implementação da localização automática por IP representa uma evolução do sistema, tornando a consulta mais prática e reduzindo a necessidade de alterações manuais no código-fonte.

O projeto faz parte da minha jornada de aprendizado em programação e do desenvolvimento de aplicações que utilizam APIs para obter e apresentar informações atualizadas.

---

**Projeto desenvolvido para fins de estudo e aprendizado em Python e consumo de APIs.**