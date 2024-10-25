# Usar uma imagem base do Python 3.12 slim
FROM python:3.12-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências para o contêiner
COPY requirements.txt .

# Instalar as dependências sem usar cache para economizar espaço
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos da aplicação para o diretório de trabalho do contêiner
COPY . .

# Expor a porta que o Flask usará
EXPOSE 8000

# Configurar o ambiente para produção
ENV FLASK_ENV=production
ENV FLASK_APP=main.py

# Comando para iniciar a aplicação Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]
