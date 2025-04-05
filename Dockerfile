# Use a imagem oficial do Python como base
FROM python:3.9-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos do diretório local para dentro do container
COPY . /app

# Instala as dependências do projeto, caso haja um requirements.txt
# Caso não tenha, essa linha pode ser removida
RUN pip install --no-cache-dir -r requirements.txt

# Define o comando padrão a ser executado no contêiner
CMD ["python", "main.py"]
