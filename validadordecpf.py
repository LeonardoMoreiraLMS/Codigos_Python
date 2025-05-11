def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))  # Remove qualquer caractere não numérico

    if len(cpf) != 11:
        return False

    # Verificando o primeiro dígito verificador
    soma = sum([int(cpf[i]) * (10 - i) for i in range(9)])
    primeiro_dv = (soma * 10) % 11
    if primeiro_dv == 10 or primeiro_dv == 11:
        primeiro_dv = 0

    if int(cpf[9]) != primeiro_dv:
        return False

    # Verificando o segundo dígito verificador
    soma = sum([int(cpf[i]) * (11 - i) for i in range(10)])
    segundo_dv = (soma * 10) % 11
    if segundo_dv == 10 or segundo_dv == 11:
        segundo_dv = 0

    if int(cpf[10]) != segundo_dv:
        return False

    return True

cpf = input("Digite o CPF (com ou sem pontos e traços): ")
if validar_cpf(cpf):
    print("CPF válido!")
else:
    print("CPF inválido!")
