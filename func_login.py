from classUser import Usuario
from random import randint

# Def que testa valores de login
def envia_valor(user, senha, janela_p, app):
    with open('users', 'r', encoding='utf=8') as arq_u:
        for i in arq_u:
            lista_us = i.split()
            if user == lista_us[0] and senha == lista_us[1]:
                janela_p.show(wait=True)
                break
            else:
                continue

        else:
            app.error('Erro', 'Usuário não encontrado.')


# Gerador de código aleatório
def cria_codigo():
    codigo_cria = randint(1000, 9999) # Cria um código
    with open('users', 'r', encoding='utf=8') as arq_users:
        for user in arq_users: # Testa o código criado
            lista_user = user.split()
            if lista_user[2] != codigo_cria: # Testa com os códigos do arquivo
                return codigo_cria
            else:
                cria_codigo() # Caso encontre algum igual, cria outo código.


# Função de cadastro do user
def cadrastro_user(user_cad, senha_cad, janela_r):
    # Teste se valores são nulos
    if user_cad == '' or senha_cad == '':
        janela_r.info('Usuário e senha não definidos', 'Insira usuário e senha, por favor')
    else:
        # Testa se tem espaços na senha ou usuário
        if user_cad.count(' ') != 0 or senha_cad.count(' ') != 0:
            janela_r.error('Espaços', 'Usuário e senha devem ser sem espaços.')
        else:
            # Abre arquivo de usuários
            with open('users', 'r', encoding='utf=8') as users_arq:
                for i in users_arq:
                    lista_users = i.split()
                    # Testa se usuário já existe
                    if (user_cad == lista_users[0] and senha_cad == lista_users[1]) or (user_cad == lista_users[0]):
                        janela_r.error('Cadastro', 'Usuário já é cadastrado.')
                        break
                    else:
                        continue
                else:
                    janela_r.info('Cadastro', 'Usuário cadastrado.')
                    obj_user = Usuario(user_cad, senha_cad, cria_codigo())
                    with open('users', 'a', encoding='utf=8') as arq_users:
                        arq_users.write(f'{obj_user.nome} {obj_user.senha} {obj_user.codigo}\n')


#Função da busca de usuário
def busca_user(user_cod, janela_p):
    # Abre arquivo do usuário
    with open('users', 'r', encoding='utf=8') as arq_user:
        for users_arq in arq_user:
            lista_users = users_arq.split()
            # Tenta encontrar user no arquivo com os parâmetros informados
            if lista_users[0] == user_cod or lista_users[2] == user_cod:
                janela_p.info('Usuário encontrado', 
                              f'Nome: {lista_users[0]} | Senha: {lista_users[1]} | Código: {lista_users[2]}')
                break
            else:
                continue
        else:
            janela_p.error('Busca erro', 'Usuário não encontrado.')


# Função que exclui usuário usando o código informado
def exclui_user(codigo, janela_p):
    # Testa se código é nulo
    if codigo == '':
        janela_p.error('Código não fornecido', 'Escreva o codigo do usuário na caixa de exclusão'
              ' para excluí-lo.')
    else:
        # Abre arquivo em leitura para pegar linhas
        with open('users', 'r', encoding='utf=8') as arq_users:
            linhas = arq_users.readlines() # Aloca linhas do arquivo

            # Abre arquivo em escrita
            with open('users', 'w', encoding='utf=8') as w_arq_users:

                # Percorre as linhas de leitura
                for linha in linhas:
                    lista_linha = linha.split() # Lista de cada linha
                    # Se o codigo for igual ao codigo da linha
                    if codigo == lista_linha[2]:
                        #r Remove linha do usuário do respectivo código
                        linhas.remove(linha)
                        janela_p.info('Excluir usuário', 'Usuário excluido.')
                        break
                    else:
                        continue
                else:
                    janela_p.error('Excluir usuário', 'Usuário não encontrado.')
                    # Reescreve arquivos com a linha apagada (resultado do arquivo aberto em r), se houver
                    # A reescrita de linhas, para que a linha excluida seja retirada do arquivo
                for linha_f in linhas:
                    w_arq_users.write(linha_f)
                