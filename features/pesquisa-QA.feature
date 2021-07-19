Feature: Pesquisa com o QA
  Como um recrutador
  Quero colher dados da pesquisa
  Para fazer análises mais detalhadas do QA

  Scenario: Preencher pesquisa com dados obrigatórios válidos
    Given que eu acesse a página da VV Test
    And acesse o menu "Pesquisa - QA"
    When eu preencher todos os campos obrigatório
        |Nome   |Sobrenome    |Email              |Confirma email|Telefone          |Idade|Quanto tempo voce esta na area de QA|O que te atraiu na area|O que mais voce precisa melhorar|Qual linguagem de programacao interessa|Escreva resumidamente um plano para sua carreira|
        |Ricardo|K. S         |test3@teste3.com.br|test3@teste3.com.br |9 99999-9999|31-49|mais-de-5-anos                      |Desafio                |Todas as anteriores             |Python                                 |Algum texto aqui                                |
    Then deve ser direcionado para uma página de sucesso
