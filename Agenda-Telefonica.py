import json
import os

class AgendaTelefonica:
    def __init__(self, arquivo='agenda.json'):
        self.arquivo = arquivo
        self.contatos = self.carregar_contatos()

    def carregar_contatos(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, 'r') as file:
                return json.load(file)
        return {}

    def salvar_contatos(self):
        with open(self.arquivo, 'w') as file:
            json.dump(self.contatos, file, indent=4)

    def adicionar_contato(self, nome, telefone):
        self.contatos[nome] = telefone
        self.salvar_contatos()

    def remover_contato(self, nome):
        if nome in self.contatos:
            del self.contatos[nome]
            self.salvar_contatos()

    def atualizar_contato(self, nome, novo_telefone):
        if nome in self.contatos:
            self.contatos[nome] = novo_telefone
            self.salvar_contatos()

    def listar_contatos(self):
        for nome, telefone in self.contatos.items():
            print(f'Nome: {nome}, Telefone: {telefone}')

    def buscar_contato(self, nome):
        return self.contatos.get(nome, 'Contato não encontrado.')

def menu():
    agenda = AgendaTelefonica()
    while True:
        print("\nAgenda Telefônica")
        print("1. Adicionar Contato")
        print("2. Remover Contato")
        print("3. Atualizar Contato")
        print("4. Listar Contatos")
        print("5. Buscar Contato")
        print("6. Sair")
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            nome = input("Digite o nome: ")
            telefone = input("Digite o telefone: ")
            agenda.adicionar_contato(nome, telefone)
        elif escolha == '2':
            nome = input("Digite o nome do contato a ser removido: ")
            agenda.remover_contato(nome)
        elif escolha == '3':
            nome = input("Digite o nome do contato a ser atualizado: ")
            novo_telefone = input("Digite o novo telefone: ")
            agenda.atualizar_contato(nome, novo_telefone)
        elif escolha == '4':
            agenda.listar_contatos()
        elif escolha == '5':
            nome = input("Digite o nome do contato a ser buscado: ")
            print(agenda.buscar_contato(nome))
        elif escolha == '6':
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == '__main__':
    menu()