# **Analise de Sentimento**


#### Esse projeto tem o propósito de extrair comentarios de qualquer video do Youtube e fazer uma analise de sentimento definindo um padrão do texto.

###### TCC - MARCO BATISTA DA SILVA JUNIOR - ENGENHARIA DA COMPUTAÇÃO - ESTACIO DE SÁ 2024.2

##### veja documentação do tcc em ->  [DOC TCC](https://docs.google.com/document/d/e/2PACX-1vQCcJgKuDNtDvwF-kxkwDJH5fsXSyVUa3v4Z0gflVQkkm51ihxhuBfv_ZCOv8jkQQ/pub)

para testar o codigo veja o passo a passo abaixo.

##### O REPOSITORIO HÁ DOIS ARQUIVOS PRINCIPAIS:
1. **api_youtube** - para extrair comentarios do video
2. **analise** - toda analise do texto coletado

### PASSO A PASSO:



### 1. Clonar 
##### Para iniciar o desenvolvimento, é necessário clonar o projeto em seu diretório de preferência usando o seguinte comando no terminal:
 
```
git clone https://github.com/marcojnr/analise-sentimento.git
```

### 2. Criar ambiente
##### Criar e ativar um ambiente virtual do projeto em seu diretório de preferencia para aplicação python.

```
python -m venv venv
```
```
venv\Script\activate
```

### 3. Bibliotecas fundamentais
##### Para preparar o ambiente, instale os pacotes necessários.

```
pip install -r requirements.txt
```
### 4. Conta
##### É necessario criar conta no google develop para acesso da API.
*https://developers.google.com/youtube/v3/getting-started?hl=pt*

### 5. Inicio Coleta
##### Para coletar os comentarios, abre o prompt e chame o api_youtube.py e em seguida o link do video.
```
api_youtube.py link_do_video
```
### 6. Analise
##### Analise completa da raspagem feita do video e resultado dos sentimento em analise.ipynb.
obs veja mais detalhes no doc do tcc.
