tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)

def listar_tarefas():
    print("\nLista de tarefas:")
    for i, t in enumerate(tarefas, 1):
        print(f"{i}. {t}")

def remover_tarefa(indice):
    if 0 <= indice < len(tarefas):
        tarefas.pop(indice)

# Exemplo de uso
adicionar_tarefa("Estudar GitHub")
adicionar_tarefa("Criar projeto simples")
listar_tarefas()
remover_tarefa(0)
listar_tarefas()
