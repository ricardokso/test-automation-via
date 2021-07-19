#Teste de Automação - Via

Funcionalidade: Pesquisa com o QA Como um recrutador Quero colher dados da pesquisa Para fazer análises mais detalhadas do QA

Link: https://bit.ly/3jOMrR9

Cenário: Preencher pesquisa com dados obrigatórios válidos

Dado que eu acesse a página da VV Test E acesse o menu "Pesquisa - QA" Quando eu preencher todos os campos obrigatórios Então deve ser direcionado para uma página de sucessoa

#Instalação

python -m venv ./venv
source venv/bin/activate #Linux
\env\Scripts\activate.ps1 #Windows

pip install behave selenium
