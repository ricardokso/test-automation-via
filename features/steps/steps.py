from behave import *
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select



@given(u'que eu acesse a página da VV Test')
def step_impl(context):
    context.driver = webdriver.Chrome("./drivers/chromedriver") #webdriver.Firefox("./drivers/geckodriver")
    context.driver.maximize_window()
    context.driver.get("http://lourencodemonaco.com.br/vvtest/")
    time.sleep(5)


@given(u'acesse o menu "Pesquisa - QA"')
def clicaMenuPesquisaQA(context):
    context.driver.find_element_by_id("menu-item-226").click()
    time.sleep(5)


@when(u'eu preencher todos os campos obrigatório')
def preencheCampos(context):
    for row in context.table:
        nome = context.driver.find_element_by_id("nf-field-5")
        nome.send_keys(row["Nome"])
        sobrenome = context.driver.find_element_by_id("nf-field-6")
        sobrenome.send_keys(row["Sobrenome"])
        email = context.driver.find_element_by_id("nf-field-7")
        email.send_keys(row["Email"])
        confirma_email = context.driver.find_element_by_id("nf-field-8")
        confirma_email.send_keys(row["Confirma email"])
        telefone = context.driver.find_element_by_id("nf-field-17")
        telefone.send_keys(row["Telefone"])
        idade = context.driver.find_element_by_id("nf-label-class-field-10-1")
        idade.click()
        quanto_tempo_area_de_QA = Select(context.driver.find_element_by_id("nf-field-11"))
        quanto_tempo_area_de_QA.select_by_value(row["Quanto tempo voce esta na area de QA"])
        o_que_atriu_na_area = Select(context.driver.find_element_by_id("nf-field-12"))
        o_que_atriu_na_area.select_by_visible_text(row["O que te atraiu na area"])
        o_que_mais_precisa_melhorar = context.driver.find_element_by_id("nf-label-class-field-13-4")
        o_que_mais_precisa_melhorar.click()
        qual_linguagem_interessa = context.driver.find_element_by_id("nf-field-14")
        qual_linguagem_interessa.send_keys(row["Qual linguagem de programacao interessa"])
        escreva_resumidamente_plano_carreira = context.driver.find_element_by_id("nf-field-15")
        escreva_resumidamente_plano_carreira.send_keys(row["Escreva resumidamente um plano para sua carreira"])

    context.driver.find_element_by_id("nf-field-16").click()


@then(u'deve ser direcionado para uma página de sucesso')
def paginaSucesso(context):
    assert context.driver.page_source.find('Your form has been successfully submitted')
