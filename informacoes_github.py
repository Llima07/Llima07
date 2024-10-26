"""
Código para apresentação 
"""
import os
from datetime import date
ano_atual = date.today().year
idade_atual = ano_atual - 1997

#Variais, com as listas e dados
informacoes = {'1':'Informações Gerais','2':'Informações Academicas','3':'Informações Profissionais','4':'Hobbies e Gostos pessoais'}
hobbies = {'1': 'Games', '2':'Filmes'}
games = ['God of war', 'The legend of Zelda', 'Devil may Cry', 'Souls Like da From Software','Fallout', 'GTA', 'Assassins Creed','The Witcher']
filmes = ['Interestelar', 'Troia', 'Trilogia Batman do Nolan','Saga Senhor dos Aneis', 'Saga Star Wars', 'Marvel "Até certo ponto kkk"', "Disney e Pixar"]


def menu_usuario():
    print("============================================")
    print("Olá Mundo!\nBem vindo ao meu perfil :)\n")
    print("O que gostaria de fazer?")
    for chave, valor in informacoes.items():
        print(chave,"-",valor)
    print("============================================")

def informacoes_pessais():
    print("============================================")
    print("Nome: Luan Gomes de Lima")
    print(f"Idade: {idade_atual} Anos")
    print("email: luanlima7344@gmail.com")
    print("Telefone: +55 (11) 9 9198-1579")
    print("São Paulo - SP (Brasil)")
    print("============================================\n")
    print(input("Digite qualquer botão para voltar!\n"))    

def informacoes_academicas():
    print("============================================")
    print("Instituição: Ebac")
    print("Curso: Ciencia de dados")
    print("Inicio: Julho/2024")
    print("============================================")

def informacoes_profissionais():
    print("============================================")
    print("Empresas:\n1 - Cielo\n2 - Capgemini\n3 - LifeCare\n4 - Nava")
    print("Digite qual empresa gostaria de mais inforações:\n(Nome ou numero)")
    print("============================================")

def cielo():
    print("=================================")
    print("==============CIELO==============")
    print("=================================")
    print("Cargo: Analista de Desenvolvimento de Tecnologia Jr")
    print("Inicio: Julho/2024")
    print("Modelo: Hibrido")
    print("Descrição: Apesar do cargo, na pratica sou Gestor de Incidente e monitoramento, onde realizo o gerenciamento dos incidentes, onde temos como objetivo a diminuição do tempo de incidente e a quantidade de incidentes criticos.")
    print("===============================")
    input("Digite qualquer botão para voltar!\n")  

def capgemini():
    print("=================================")
    print("============CAPGEMINI============")
    print("=================================")
    print("Cargo: Analista Soluções Nuvem II")
    print("Inicio: Agosto/2022\nSaída: Fevereiro/2024")
    print("Modelo: Remoto")
    print("Descrição: Prestando serviços para o Ifood, realizava a monitoração, abertura e fechamento de chamado, tenho maestria na obervabilidade na Cloud da AWS")
    print("===============================")
    input("Digite qualquer botão para voltar!\n")   

def lifecare():
    print("================================")
    print("============LIFECARE============")
    print("================================")
    print("Analista de sistemas Junior")
    print("Inicio: Maio/2022\nSaída: Agosto/2022")
    print("Modelo: Presencial")
    print("Descrição: Manutenção no sistema, analise de bugs e utilização de programação em HTML, CSS, JavaScript e PHP, para realizar os reparos e adicionar paginas. Feito a manutenção das maquinas, sendo feito a abertura e testes em seu Hardware.")
    print("===============================")
    input("Digite qualquer botão para voltar!\n")  

def nava():
    print("================================")
    print("==============NAVA==============")
    print("================================")
    print("Cargo: Analista de Monitoração Sênior")
    print("Inicio: Outubro/2020\nSaída: Março/2022")
    print("Modelo: Remoto")
    print("Descrição: Monitoramento do desempenho de sistemas, sites e componentes da infraestrutura, a fim de detectar desvios e evitar indisponibilidade no ambiente, registro de ocorrência de falhas e acompanha resolução de incidentes.")
    print("===============================")
    input("Digite qualquer botão para voltar!\n")  

while True:
#Hub do usuario
    os.system('cls')
    menu_usuario()
    opcao_user = input("")

    os.system('cls')
#Informações conforme a seleção do usuario
    if opcao_user == '1':
        informacoes_pessais()

#INFORMAÇÕES ACADEMICAS
    os.system('cls')
    if opcao_user == '2':
        informacoes_academicas()
        input("Digite algo para voltar ao menu")

#INFORMAÇÕES PROFISSIONAIS
    os.system('cls')
    if opcao_user == '3':
        informacoes_profissionais()
        opcao_profissional=input("Digite qualquer botão para voltar!\n")
        
        os.system('cls')
        if opcao_profissional == '1' or opcao_profissional == 'cielo':
            cielo()
        os.system('cls')
        if opcao_profissional == '2' or opcao_profissional == 'capgemini':
            capgemini()

        os.system('cls')
        if opcao_profissional == '3' or opcao_profissional == 'lifecare':
            lifecare()

        os.system('cls')  
        if opcao_profissional == '4' or opcao_profissional == 'nava':
            nava()

#HOBBIES
    if opcao_user == '4':
        print("===============================")
        print("===HOBBIES E GOSTOS PESSOAIS===")
        print("===============================")
        for chave, valor in hobbies.items():
            print(chave, ":", valor)
        print("===============================")    
        print("Selecione o que deseja saber mais")
        info_hobbies = input("")
        info_hobbies.lower

        os.system('cls')
        if info_hobbies == '1' or info_hobbies == 'games':
            print("===============================")
            print("=============GAMES=============")
            print("===============================")
            print("Apaixonado pelo mundo dos games, sempre focando em um balanceamento entre Historia, Jogabilidade e Graficos, abaixo uma lista das minhas franquias favoritas:\n")
            for game in games:
                print(game)
            print("===============================")
            input("Digite algo para voltar ao menu")
            
        if info_hobbies == '2' or info_hobbies =='fimes':
            print("================================")
            print("=============FILMES=============")
            print("================================")
            print("Estou em aprofundando na parte de cinema, mas ja sou fascinado pela setima arte, não conheco muito, mas tenho alguns filmes favoritos:\n")
            for filme in filmes:
                print(filme)
            print("===============================")
            input("Digite algo para voltar ao menu")





