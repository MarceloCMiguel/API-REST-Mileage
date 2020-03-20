# API-REST-Mileage
Processo Seletivo

Como funciona:
O arquivo app.py roda as rotas do site, enquanto o db.py faz a conexão entre o dicionario (database) do app.py 
com o MongoDB Atlas. A pasta template e static armazena o html dos sites e um css base para seu funcionamento.

Para rodar o site, basta digitar no terminal: python app.py. Após isso, entrar no endereço http://localhost:5000/
Sempre que o site for para sua pagina inicial (de abertura), o dicionário é atualizado no MongoDB Atlas.


Apesar do site estar funcionando, não consegui fazer com que o site funcionasse no servidor do Heroku por conta 
de um erro no requirements.txt