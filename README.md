# Gestao de propostas

faça o clone do repositório `git clone https://github.com/LeonardoCavachini/gestao_propostas.git`,

## Rodando a aplicação backend

entre na pasta server, no seu terminal digite `cd server`

crie um abiente virtual, digite no seu terminal `python3 -m venv venv` ative-o `source venv/bin/activate`.

digite no seu terminal `docker compose up`, lembrando que você deve ter o docker

instalado. Mais detalhes em [Docker](https://www.docker.com/).

abra um novo terminal e digite `python manage.py migrate` para rodar as migrações, e `python manage.py proposta_seed` para popular o banco e `python manage.py runserver` para rodar a aplicação.

no seu terminal digite `python manage.py createsuperuser` e digite um nome e senha para criar um usuário.

abra um novo terminal e `celery -A gestao worker -l INFO` para rodar o celery.

abra um novo terminal e `celery -A gestao beat -l INFO` para rodar o celery beat.

## Rodando a aplicação frontEnd

entre na pasta web, para isso digite no seu terminal `cd web`

install dependencias digite `npm install`

rodar aplicação digite `npm run dev`

## Cotextalização da aplicação

Ao entrar na aplicação você verá um formulário onde poderá registrar uma proposta, aconselho digitar valores entre 0 e 100, após 20segundos ela sera analisada, para visualizar a analise entre no admin do django, digite `http://127.0.0.1:8000/admin` no browser e inseria seu login e senha do admin `leodev - 123456789` por exemplo, após acesso clique em prposta para visualizar os status.

