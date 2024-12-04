import random  # Importa o módulo 'random' para gerar números aleatórios, usado para o número da conta, aprendi no curso Data Science Academy

# Classe base para Conta
class Conta:
    def __init__(self, titular, senha):
        # Inicializa os dados da conta
        self.titular = titular  # Nome do titular da conta
        self.numero_conta = random.randint(100, 999)  # Gera um número aleatório para a conta, entre 100 e 999
        self.__senha = senha  # Define a senha da conta (não pode ser alterada diretamente)
        self.__saldo_corrente = 0.0  # Saldo inicial da conta corrente
        self.__saldo_poupanca = 0.0  # Saldo inicial da conta poupança
        self.bloqueada = False  # Atributo para indicar se a conta está bloqueada

    # Métodos Getters e Setters para saldo corrente
    def get_saldo_corrente(self):
        return self.__saldo_corrente  # Retorna o saldo corrente da conta

    def alterar_saldo_corrente(self, valor):
        self.__saldo_corrente += valor  # Modifica o saldo corrente (valor pode ser positivo ou negativo)

    # Métodos Getters e Setters para saldo poupança
    def get_saldo_poupanca(self):
        return self.__saldo_poupanca  # Retorna o saldo da poupança

    def alterar_saldo_poupanca(self, valor):
        self.__saldo_poupanca += valor  # Modifica o saldo da poupança (valor pode ser positivo ou negativo)

    # Método para verificar a senha com limite de tentativas
    def verificar_senha(self):
        if self.bloqueada:
            # Verifica se a conta está bloqueada
            print("Conta bloqueada. Dirija-se à agência para desbloqueio.")
            return False

        tentativas = 0  # Inicia o contador de tentativas
        while tentativas < 3:  # Limite de 3 tentativas para acertar a senha
            senha_digitada = input("Digite sua senha (4 dígitos): ")  # Solicita a senha
            if senha_digitada == self.__senha:
                return True  # Se a senha estiver correta, retorna True
            else:
                print("Senha incorreta. Tente novamente.")  # Se a senha estiver errada, incrementa as tentativas
                tentativas += 1

        self.bloqueada = True  # Se errar 3 vezes, bloqueia a conta
        print("\nConta bloqueada após 3 tentativas incorretas.") #\n é uma boa prática para Python
        print("Dirija-se à agência com documento com foto para desbloqueio.")
        return False  # Retorna False, indicando que a senha não foi verificada corretamente

    # Método para exibir o extrato da conta
    def extrato(self):
        if self.verificar_senha():  # Primeiro verifica a senha antes de exibir o extrato
            print("\n+------------Luck Bank-----------------------+")
            print(f"| Titular: {self.titular}")
            print(f"| Número da conta: {self.numero_conta}")
            print(f"| Saldo da Conta Corrente: R${self.get_saldo_corrente():.2f}")
            print(f"| Saldo da Conta Poupança: R${self.get_saldo_poupanca():.2f}")
            print("+--------------------------------------------+")

# Classe ContaCorrente herda de Conta
class ContaCorrente(Conta):
    def sacar(self, valor):
        if self.verificar_senha():  # Verifica a senha antes de realizar o saque
            if self.get_saldo_corrente() >= valor:  # Verifica se o saldo é suficiente
                self.alterar_saldo_corrente(-valor)  # Subtrai o valor do saldo corrente
                print(f"Saque de R${valor:.2f} realizado com sucesso!")  # Exibe mensagem de sucesso
            else:
                print("Saldo insuficiente para realizar o saque.")  # Exibe mensagem de erro

    def depositar(self, valor):
        if valor > 0:  # Verifica se o valor do depósito é válido (positivo)
            self.alterar_saldo_corrente(valor)  # Adiciona o valor ao saldo corrente
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")  # Exibe mensagem de sucesso
        else:
            print("Valor de depósito inválido.")  # Exibe mensagem de erro se o valor for inválido

    def aplicar(self, valor, conta_poupanca):
        if self.verificar_senha():  # Verifica a senha antes de realizar a aplicação
            if self.get_saldo_corrente() >= valor:  # Verifica se o saldo é suficiente
                self.alterar_saldo_corrente(-valor)  # Subtrai o valor do saldo corrente
                conta_poupanca.alterar_saldo_poupanca(valor)  # Adiciona o valor à poupança
                print(f"Aplicação de R${valor:.2f} para poupança realizada com sucesso!")  # Exibe mensagem de sucesso
            else:
                print("Saldo insuficiente para realizar a aplicação.")  # Exibe mensagem de erro

# Classe ContaPoupanca herda de Conta
class ContaPoupanca(Conta):
    def resgatar(self, valor, conta_corrente):
        if self.verificar_senha():  # Verifica a senha antes de realizar o resgate
            if self.get_saldo_poupanca() >= valor:  # Verifica se o saldo é suficiente na poupança
                self.alterar_saldo_poupanca(-valor)  # Subtrai o valor da poupança
                conta_corrente.alterar_saldo_corrente(valor)  # Adiciona o valor à conta corrente
                print(f"Resgate de R${valor:.2f} realizado com sucesso!")  # Exibe mensagem de sucesso
            else:
                print("Saldo insuficiente na poupança.")  # Exibe mensagem de erro se não houver saldo suficiente

# Função principal que controla o fluxo do programa
def main():
    print("Bem-vindo ao Luck Bank!")  # Mensagem de boas-vindas

    # Criação da conta
    titular = input("Digite o nome do titular da conta: ")  # Solicita o nome do titular
    while True:
        senha = input("Crie uma senha (4 dígitos): ")  # Solicita a senha
        if len(senha) == 4 and senha.isdigit():  # Verifica se a senha tem 4 dígitos
            break  # Se a senha for válida, sai do loop
        print("Senha inválida. A senha deve conter 4 dígitos.")  # Exibe mensagem de erro se a senha for inválida

    # Criação das contas
    conta_corrente = ContaCorrente(titular, senha)
    conta_poupanca = ContaPoupanca(titular, senha)

    print("\nConta criada! Número da conta:", conta_corrente.numero_conta)  # Exibe o número da conta criada

    # Primeiro depósito obrigatório
    while True:
        try:
            deposito_inicial = float(input("Realize seu primeiro depósito (mínimo R$ 10,00): "))  # Solicita o primeiro depósito
            if deposito_inicial >= 10:  # Verifica se o depósito inicial é válido
                conta_corrente.depositar(deposito_inicial)  # Realiza o depósito na conta corrente
                break  # Sai do loop quando o depósito for válido
            else:
                print("O depósito inicial deve ser no mínimo R$ 10,00.")  # Exibe mensagem de erro se o valor for insuficiente
        except ValueError:
            print("Valor inválido. Tente novamente.")  # Exibe mensagem de erro caso o valor inserido não seja um número válido

    # Menu de opções
    while True:
        if conta_corrente.bloqueada or conta_poupanca.bloqueada:  # Verifica se a conta está bloqueada
            print("Conta bloqueada. Atendimento encerrado.")  # Exibe mensagem de encerramento
            break  # Sai do loop se a conta estiver bloqueada

        print("\nMenu:")  # Exibe o menu de opções
        print("1. Sacar")
        print("2. Depositar")
        print("3. Aplicar para poupança")
        print("4. Resgatar da poupança")
        print("5. Extrato")
        print("6. Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))  # Solicita a opção do usuário
            if opcao == 1:
                valor = float(input("Digite o valor a ser sacado: "))  # Solicita o valor a ser sacado
                conta_corrente.sacar(valor)  # Chama o método para realizar o saque
            elif opcao == 2:
                valor = float(input("Digite o valor a ser depositado: "))  # Solicita o valor a ser depositado
                conta_corrente.depositar(valor)  # Chama o método para realizar o depósito
            elif opcao == 3:
                valor = float(input("Digite o valor para aplicar na poupança: "))  # Solicita o valor a ser aplicado
                conta_corrente.aplicar(valor, conta_poupanca)  # Chama o método para realizar a aplicação
            elif opcao == 4:
                valor = float(input("Digite o valor a ser resgatado da poupança: "))  # Solicita o valor a ser resgatado
                conta_poupanca.resgatar(valor, conta_corrente)  # Chama o método para realizar o resgate
            elif opcao == 5:
                conta_corrente.extrato()  # Exibe o extrato da conta
            elif opcao == 6:
                print("Encerrando o atendimento. Obrigado por usar o Banco!")  # Exibe mensagem de encerramento
                break  # Sai do loop e encerra o programa
            else:
                print("Opção inválida. Tente novamente.")  # Exibe mensagem de erro para opção inválida
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")  # Exibe mensagem de erro para entrada inválida

# Verifica se o arquivo está sendo executado diretamente
if __name__ == "__main__":
    main()  # Chama a função principal para rodar o programa
