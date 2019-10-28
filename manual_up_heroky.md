# django-heroku

Configuração minima para hospedar o projeto em Django no Heroku

# Criando o diretório do projeto

    mkdir directory_name
    cd directory_name

# Criando e ativado sua virtual env

    virtualenv -p python3 .vEnv
    ..vEnv/bin/activate

# Instalando o Django

    pip install django

# Criando o projeto Django

django-admin startproject myproject

# Criando o Git Repositório

    git init

# Instanciando as configurações iniciais

    pip install python-decouple

Criar o arquivo .env no caminho root do projeto e inserir as variaveis

    SECRET_KEY=Your$eCretKeyHere (Pegar essa variavel no settings.py)
    DEBUG=True

Settings.py

    from decouple import config
    SECRET_KEY = config('SECRET_KEY')
    DEBUG = config('DEBUG', default=False, cast=bool)

# Configurando a Database

    pip install dj-database-url

Settings.py

    from dj_database_url import parse as dburl
    default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.slite3')
    DATABASE = {'default':config('DATABASE_URL', default=default_dburl, cast=dburl),}

# Configurando os arquivos estaticos


    pip install dj-static

Configurando o WSGI.py

    from dj_static import Cling
    application = Cling(get_wsgi_application())

Configurando o setting.py

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Criando o arquivo de requirements


    pip freeze > requirements-dev.txt

# Criando o arquivo do requirements.txt e incluindo a referencia 

    -r requirements-dev.txt
    gunicorn
    psycopg2

# Criando o arquivo Procfile e adicionando o código abaixo

    web: gunicorn website.wsgi --log-file -

# Criando um arquivo runtime.txt e adicionando o código abaixo

    python-3.6.0

# Criando o aplicativo no Heroky

Primeiro você deve inicialmente instalar o Heroky CLI no seu computador.

    heroku apps:create app-name

No lugar de app-name coloque o nome que você deseja no heroky

# Configurando os host acessiveis no settings.py

Incluir seu endereço na variavel ALLOWED_HOSTS em settings.py

ALLOWED_HOSTS = ['pontos-turist.herokuapp.com', 'localhost:8000']

# Instalando o config plugin do Heroky

    heroku plugins:install heroku-config

# Enviando as configurações para .env do Heroku (Você precisa ter o arquivo .env em seus arquivos)

    heroku config:push

Para verificar se foi feito com sucesso:

    heroku config

# Publicando o app

    git add .
    git commit -m "Configurando app no Heroky"
    heroku config:set DISABLE_COLLECTSTATIC=1
    git push heroku master --force

# Criando o banco de dados no Heroku

heroku run python3 manage.py migrate
heroku run python3 manage.py createsuperuser
