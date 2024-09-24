from motorista import Motorista
from corrida import Corrida
from passageiro import Passageiro
from motorista_dao import MotoristaDAO

class MotoristaCLI:
    def __init__(self):
        self.dao = MotoristaDAO()

    def menu(self):
        while True:
            print("\nMenu:")
            print("1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.create_motorista()
            elif opcao == "2":
                self.read_motorista()
            elif opcao == "3":
                self.update_motorista()
            elif opcao == "4":
                self.delete_motorista()
            elif opcao == "5":
                break
            else:
                print("Opção inválida!")

    def create_motorista(self):
        nome = input("Nome do Motorista: ")
        cnh = input("CNH do Motorista: ")
        corridas = []

        while True:
            print("\nAdicione uma corrida:")
            nota = input("Nota: ")
            distancia = input("Distância: ")
            valor = input("Valor: ")
            nome_passageiro = input("Nome do Passageiro: ")
            documento = input("Documento do Passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento)
            corrida = Corrida(nota, distancia, valor, passageiro)
            corridas.append(corrida)
            continuar = input("Adicionar mais uma corrida? (s/n): ")
            if continuar.lower() != 's':
                break

        motorista = Motorista(nome, cnh, corridas)
        self.dao.create_motorista(motorista)
        print("Motorista criado com sucesso!")

    def read_motorista(self):
        motorista_id = input("ID do Motorista: ")
        motorista = self.dao.read_motorista(motorista_id)
        if motorista:
            print(motorista)
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        motorista_id = input("ID do Motorista: ")
        nome = input("Novo nome do Motorista: ")
        cnh = input("Nova CNH do Motorista: ")
        novos_dados = {"nome": nome, "cnh": cnh}
        self.dao.update_motorista(motorista_id, novos_dados)
        print("Motorista atualizado com sucesso!")

    def delete_motorista(self):
        motorista_id = input("ID do Motorista: ")
        self.dao.delete_motorista(motorista_id)
        print("Motorista deletado com sucesso!")
