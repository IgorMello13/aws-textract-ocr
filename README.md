# 📝 Projeto de OCR com AWS Textract

Este repositório contém um projeto de OCR utilizando **AWS Textract**, permitindo a extração de texto a partir de imagens. O objetivo é processar automaticamente documentos escaneados e transformá-los em texto digital de forma otimizada.

## 📌 Funcionalidades
- Extração automática de texto de imagens usando **AWS Textract**.
- Reutilização do arquivo `response.json` para evitar chamadas desnecessárias à AWS.
- Suporte a múltiplas imagens de entrada.
- Salvamento dos resultados em JSON para pós-processamento.

## 🛠️ Tecnologias Utilizadas
- 🐍 Python 3.8+
- ☁️ AWS Textract
- 🏗️ Boto3 (SDK da AWS para Python)

## 🚀 Como Executar

### 1️⃣ **Instalar Dependências**
Antes de rodar o script, instale as dependências necessárias:

```bash
pip install boto3 mypy-boto3-textract


2️⃣ Configurar AWS Credentials
Para utilizar o AWS Textract, configure suas credenciais da AWS:

```bash
aws configure

Você precisará fornecer:
- AWS Access Key ID
- AWS Secret Access Key
- Região padrão da AWS


3️⃣ Executar o Script
Basta rodar o arquivo main.py:

```bash
python main.py

Isso processará a imagem lista-material-escolar.jpeg e gerará um arquivo response.json contendo os resultados. Se o response.json já existir, o script evita chamadas desnecessárias ao AWS Textract, economizando tempo e custo.


Abaixo está um exemplo do texto extraído da imagem:
Lista de Material Escolar
3 rolos de fita crepe
1 bloco de canson A4
1 fita adesiva
...

📈 Possíveis Melhorias
- Melhor tratamento dos resultados extraídos.
- Integração com Amazon S3 para armazenar imagens automaticamente.
- Uso de AWS Lambda para automação.