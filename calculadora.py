def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero."
    return a / b

def exibir_menu():
    print("\n=== CALCULADORA SIMPLES ===")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sair")

while True:
    exibir_menu()
    escolha = input("Escolha uma opção (1-5): ")

    if escolha == '5':
        print("Encerrando a calculadora.")
        break

    if escolha in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite números.")
            continue

        if escolha == '1':
            print("Resultado:", somar(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtrair(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicar(num1, num2))
        elif escolha == '4':
            print("Resultado:", dividir(num1, num2))
    else:
        print("Opção inválida. Tente novamente.")
