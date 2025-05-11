def converter_para_brl(valor_usd, taxa):
    return valor_usd * taxa

def converter_para_usd(valor_brl, taxa):
    return valor_brl / taxa

taxa_de_conversao = 5.50  # Exemplo: 1 USD = 5.50 BRL

print("Escolha a conversão:")
print("1. USD para BRL")
print("2. BRL para USD")
escolha = input("Digite 1 ou 2: ")

if escolha == '1':
    valor_usd = float(input("Digite o valor em USD: "))
    valor_brl = converter_para_brl(valor_usd, taxa_de_conversao)
    print(f"{valor_usd} USD é igual a {valor_brl:.2f} BRL.")
elif escolha == '2':
    valor_brl = float(input("Digite o valor em BRL: "))
    valor_usd = converter_para_usd(valor_brl, taxa_de_conversao)
    print(f"{valor_brl} BRL é igual a {valor_usd:.2f} USD.")
else:
    print("Opção inválida.")
