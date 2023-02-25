# Aplicação Flask para exibição de notícias 📰

> ### <p>Este é um exemplo de aplicação Flask que utiliza a API do NewsAPI para exibir notícias separadas por categorias. A aplicação inclui uma página inicial com links para as páginas de notícias de diferentes categorias.</p>
___
## Pré-requisitos 🧑‍💻

### Antes de executar a aplicação, certifique-se de ter as seguintes bibliotecas Python instaladas:

    Python 3
    Flask
    Requests

### Você também precisará de uma chave de API válida do NewsAPI para fazer solicitações à API.
___
## Executando a aplicação 🚀
### Para executar a aplicação, siga estas etapas:

1 - Clone este repositório em seu computador local.

2 - Abra o arquivo app.py em um editor de código e substitua YOUR_API_KEY pela sua chave de API do NewsAPI.

3 - No terminal, navegue até o diretório do projeto e execute o seguinte comando:

    python app.py

4 - Abra um navegador e acesse http://localhost:5000 para ver a página inicial da aplicação.
___
## Estrutura do código 🏗️
### A aplicação é composta por vários arquivos e diretórios:
* app.py: contém o código Python para a aplicação Flask.
* templates/: diretório que contém os arquivos HTML que são renderizados pela aplicação.
* static/: diretório que contém arquivos estáticos, como CSS e JavaScript.
___

## Etapas do código 📝
### Aqui estão as principais etapas do código da aplicação:
1 - Realiza uma solicitação à API do NewsAPI para obter as notícias de diferentes categorias.

2 - Armazena as notícias em variáveis separadas para cada categoria.
Renderiza um template HTML que exibe as notícias separadas por categoria.

3 - Adiciona links na página inicial que levam às páginas de notícias de diferentes categorias.
___
## Conclusão 🎉
### Espero que este exemplo de aplicação Flask tenha sido útil para você! Sinta-se à vontade para adaptá-lo ou usá-lo como ponto de partida para seus próprios projetos.