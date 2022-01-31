def listar(lista_principal):
    print(lista_principal)

def add_sem(tarefa):
    #print('Tarefas: ')
    lista_principal.append(tarefa)

def apagando(lista_principal, lixeira):
    if not lista_principal:
        print('Nada a desfazer')
        return
    else:
        ultimo_lista = lista_principal.pop()
        lixeira.append(ultimo_lista)

def refaz(lista_principal, lixeira):
    if not lixeira:
        print('Nada a refazer')
    else:
        last_lixeira = lixeira.pop()
        lista_principal.append(last_lixeira)


if __name__ == '__main__':
    lista_principal = []
    lixeira = []
    while True:
        todo = input('Digite uma tarefa ou refazer, apagar, listar: ')
        if todo == 'refazer':
            refaz(lista_principal, lixeira)
        elif todo == 'apagar':
            apagando(lista_principal, lixeira)
        elif todo == 'listar':
            listar(lista_principal)
        else:
            add_sem(todo)
