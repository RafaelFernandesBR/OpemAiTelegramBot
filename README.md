# OpemAiTelegramBot
Um bot para telegram do chat GPT
## sobre
Esse bot usa a api da opem AI para gerar resposta para perguntas do usuário.
## usando via docker
para criar uma imagem docker desse projeto, basta abrir o dockerfile e modificar as variáveis de ambientes tokem e opemAItokem, e depois usar o comando docker build -t opbot . para buildar a imagem.
Feito isso, use o comando docker run -d opbot  para executar a imagem.
## executando diretamente
Para executar o projeto diretamente, adicione os dados nas variáveis de ambientes do seu systema.
no windows, pode utilizar os seguintes comandos no cmd.
setx openAItoken "seu_token_aqui"
setx token "seu_token_telegram_aqui"

Feito isso, reinicie o systema.
Com o python já instalado, execute python main.py e pronto!