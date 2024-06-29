# Use uma imagem base do Python
FROM python:3.8-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos necessários
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=dashboard.py

# Exponha a porta que o Flask usará
EXPOSE 5000

# Comando para rodar a aplicação
CMD ["flask", "run", "--host=0.0.0.0"]
