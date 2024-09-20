from guizero import App, Text, TextBox, PushButton, Window, Box
from func_login import cadrastro_user, envia_valor, busca_user, exclui_user


# Funções que chamam os métodos usados no programa.
# Os elementos do guizero não recebem métodos com atributos, para isso é preciso cirar estes métodos.

def chama_cadastro():
    cadrastro_user(user_cad_ent.value, senha_cad_ent.value, janela_registra)
    user_cad_ent.clear()
    senha_cad_ent.clear()


def chama_envia_valor():
    envia_valor(user_ent.value, senha_ent.value, janela_p, app)
    user_ent.clear()
    senha_ent.clear()


def chama_busca():
    busca_user(user_cod_busca.value, janela_p)
    user_cod_busca.clear()


def chama_exclui():
    exclui_user(user_cod_exclui.value, janela_p)
    user_cod_exclui.clear()


# Funções de navegação do programa
    
def voltar_p_in():
    janela_p.hide()
    app.show()


def voltar_r_p():
    janela_registra.hide()
    janela_p.show()


def registrar():
    janela_registra.show(wait=True)


# Janela Inicial do App
app = App(title='Cadastro', width=300, height=200, bg='LightSkyBlue2')
app.tk.resizable(0, 0)
box_infos = Box(app, border=True, align='top', layout='grid')

Text(box_infos, text='Usuário:', grid=[0, 0])
user_ent = TextBox(box_infos, grid=[1, 0], width=30)

Text(box_infos, text='Senha:', grid=[0, 1])
senha_ent = TextBox(box_infos, grid=[1, 1], width=30, hide_text=True)


box_botoes = Box(app, align='bottom', layout='grid', border=True)
envia = PushButton(box_botoes, text='Login', grid=[0, 0], command=chama_envia_valor)
cancela = PushButton(box_botoes, text='Sair', grid=[1, 0], command=app.destroy)


# Janela principal
janela_p = Window(app, title='Janela', width=300, height=250, bg='LightSkyBlue2')
janela_p.tk.resizable(0, 0)
Text(janela_p, text='Janela Principal')


Text(janela_p, text='Buscar usuário:')
box_busca_users = Box(janela_p, layout='grid', border=True)
Text(box_busca_users, text='Usuário ou código:', grid=[0, 0])
user_cod_busca = TextBox(box_busca_users, grid=[1, 0])

Text(janela_p, text='Excluir usuário:')
box_exclui_user = Box(janela_p, layout='grid', border=True)
Text(box_exclui_user, text='Código:', grid=[0, 0])
user_cod_exclui = TextBox(box_exclui_user, grid=[1, 0])

# Botões da janela principal
box_jP_botoes = Box(janela_p, align='bottom', layout='grid', border=True)


volta_p_in = PushButton(box_jP_botoes, image='img\VOLTAR.png', command=voltar_p_in, grid=[0, 0]) # Botão de voltar
registra = PushButton(box_jP_botoes, command=registrar, grid=[1, 0], image='img\DISQUETE-0.png') # Botão de abrir janela registro
busca = PushButton(box_jP_botoes, command=chama_busca, grid=[2, 0], image='img\LUPA.png') # Botão de busca
exclui = PushButton(box_jP_botoes, image='img\EXCLUIR.png', command=chama_exclui, grid=[3, 0]) # Botão de excluir
janela_p.hide() # Deixa janela fechada 


# janela registro
janela_registra = Window(janela_p, title='Registro de Usuário', width=300, height=200, bg='LightSkyBlue2')
janela_registra.tk.resizable(0, 0)
Text(janela_registra, text='Cadastro de Usuário')

box_users_entrada = Box(janela_registra, border=True, layout='grid', align='top')
Text(box_users_entrada, grid=[0, 0], text='Usuário:')
user_cad_ent = TextBox(box_users_entrada, grid=[1, 0])
Text(box_users_entrada, grid=[0, 1], text='Senha:')
senha_cad_ent = TextBox(box_users_entrada, grid=[1, 1], hide_text=True)

box_jR_botoes = Box(janela_registra, align='bottom', border=True, layout='grid')
cadastro = PushButton(box_jR_botoes, image='img\DISQUETE.png', grid=[1, 0], command=chama_cadastro)
voldar_r_p = PushButton(box_jR_botoes, image='img\VOLTAR.PNG', grid=[0, 0], command=voltar_r_p)
janela_registra.hide()

janela_p.when_closed = app.destroy
janela_registra.when_closed = app.destroy

app.display()
