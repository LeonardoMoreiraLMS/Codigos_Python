def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("\n=== CONVERSOR DE TEMPERATURA ===")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Sair")

while True:
    menu()
    escolha = input("Escolha uma opção (1-3): ")

    if escolha == '3':
        print("Encerrando o conversor.")
        break

    if escolha == '1':
        celsius = float(input("Digite a temperatura em Celsius: "))
        print(f"{celsius}°C é igual a {celsius_para_fahrenheit(celsius)}°F")
    elif escolha == '2':
        fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
        print(f"{fahrenheit}°F é igual a {fahrenheit_para_celsius(fahrenheit)}°C")
    else:
        print("Opção inválida. Tente novamente.")
