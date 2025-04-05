# Usando a imagem base do Python
FROM python:3.9-slim

# Atualiza o pip para a versão mais recente
RUN python -m pip install --upgrade pip

# Configura o diretório de trabalho
WORKDIR /main

# Copia o conteúdo do projeto para o diretório de trabalho no container
COPY . /main

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Comando para rodar o aplicativo
CMD ["python", "main.py"]
