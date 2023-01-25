# OpemAiTelegramBot
Um bot para telegram do chat GPT
## sobre
Esse bot usa a api da opem AI para gerar resposta para perguntas do usuário.
## usando via docker
para criar uma imagem docker desse projeto, basta abrir o dockerfile e modificar as variáveis de ambientes tokem e opemAItokem, e depois usar o comando docker build -t opbot . para buildar a imagem.
Feito isso, use o comando docker run -d opbot  para executar a imagem.
