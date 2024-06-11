
def adicionar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero!"
    return a / b

def mostrar_menu():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

while True:
    mostrar_menu()
    
    escolha = input("Digite sua escolha (1/2/3/4/5): ")
    
    if escolha == '5':
        print("Saindo da calculadora...")
        break

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            resultado = adicionar(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")
        elif escolha == '2':
            resultado = subtrair(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")
        elif escolha == '3':
            resultado = multiplicar(num1, num2)
            print(f"Resultado: {num1} * {num2} = {resultado}")
        elif escolha == '4':
            resultado = dividir(num1, num2)
            print(f"Resultado: {num1} / {num2} = {f"{resultado:.2f}"}")
    else:
        print("Escolha inválida. Por favor, tente novamente.")

    print("\n")

