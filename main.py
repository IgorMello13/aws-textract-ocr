import json
import boto3
from botocore.exceptions import ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef
from pathlib import Path

# Definição dos caminhos diretamente no script
IMAGE_PATH = Path("images/lista-material-escolar.jpeg")
RESPONSE_PATH = Path("response.json")

def detect_file_text() -> None:
    """Processa a imagem e salva a resposta do AWS Textract no JSON."""
    client = boto3.client("textract")

    if not IMAGE_PATH.exists():
        print(f"Erro: Arquivo {IMAGE_PATH} não encontrado!")
        return

    with IMAGE_PATH.open("rb") as f:
        document_bytes = f.read()

    try:
        response = client.detect_document_text(Document={"Bytes": document_bytes})
        RESPONSE_PATH.write_text(json.dumps(response, indent=4))  # Salva resposta formatada
    except ClientError as e:
        print(f"Erro ao processar documento: {e}")

def get_lines() -> list[str]:
    """Lê os dados extraídos do AWS Textract e retorna as linhas de texto."""
    if not RESPONSE_PATH.exists():
        print("Arquivo de resposta não encontrado, chamando detect_file_text()...")
        detect_file_text()
    
    if not RESPONSE_PATH.exists():  # Verifica novamente após tentativa de criação
        print("Erro: O arquivo de resposta JSON não foi gerado corretamente.")
        return []

    try:
        data: DetectDocumentTextResponseTypeDef = json.loads(RESPONSE_PATH.read_text())
        return [block["Text"] for block in data["Blocks"] if block["BlockType"] == "LINE"]  # type: ignore
    except (IOError, KeyError, json.JSONDecodeError) as e:
        print(f"Erro ao ler arquivo JSON: {e}")
        return []

if __name__ == "__main__":
    for line in get_lines():
        print(line)
