def mostrar_tarefas():
  if not tarefas:
    print("Nenhuma tarefa cadastrada.")
  else:
    for indice, tarefa in enumerate(tarefas, 1):
      print(f"{indice}. {tarefa}")

def adicionar_tarefa():
  tarefa = input("Digite a tarefa: ")
  tarefas.append(tarefa)
  print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def remover_tarefa():
  if not tarefas:
    print("Nenhuma tarefa cadastrada para remover.")
  else:
    mostrar_tarefas()
    indice = int(input("Digite o número da tarefa para remover: "))
    if 1 <= indice <= len(tarefas):
      removed = tarefas.pop(indice - 1)
      print(f"Tarefa '{removed}' removida com sucesso!")
    else:
      print("Índice inválido. Tente novamente.")

tarefas = []

while True:
  print("\nMenu de Opções:")
  print("1. Adicionar Tarefa")
  print("2. Visualizar Tarefas")
  print("3. Remover Tarefa")
  print("4. Sair")

  opcao = input("Escolha uma opção: ")

  if opcao == "1":
    adicionar_tarefa()
  elif opcao == "2":
    mostrar_tarefas()
  elif opcao == "3":
    remover_tarefa()
  elif opcao == "4":
    print("Saindo do gerenciador de tarefas.")
    break
else:
    print("Opção inválida. Tente novamente.")
