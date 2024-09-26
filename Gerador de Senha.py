import random
import string

# Recebe todas as letras do alfabeto em maiúsculas
letras = string.ascii_uppercase

# Recebe caracteres especiais
sinais = '@#!$%&*()_-+='

# Recebe números
numeros = '1234567890'

# Junta as 3 variáveis para ser usada em modo random
plus = letras + sinais + numeros

while True:
    try:
        # Validação do tamanho da senha
        tamanho_senha = int(input('Escolha o tamanho da sua senha (deve ser maior que 0): '))
        if tamanho_senha <= 0:
            print("O tamanho da senha deve ser maior que zero. Tente novamente.")
            continue
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    # Gera a senha
    senha = ''.join(random.choice(plus) for _ in range(tamanho_senha))
    print(f'Sua senha randômica é: {senha}')

    # Avalia a força da senha
    if tamanho_senha <= 8:
        print('Sua senha é fraca')
    else:
        print('Sua senha é forte')

    # Pergunta se deseja continuar
    continuar = input('Deseja continuar? [S/N] ').upper()
    if continuar == 'N':
        break
