lista_numeros = []


while True:
    escolha = int(input(' Bem-vindo ao Gerenciador de Números! Digite: \n 1 - Adicionar número \n 2 - Mostrar números \n 3 - Mostrar estatísticas \n 0 - Sair\n '))
    if escolha == 1:
        num = int(input('\nDigite o número: \n'))
        lista_numeros.append(num)
    elif escolha == 2:
        if lista_numeros == []:
            print('\nLista Vazia!\n')
        else: 
            print(lista_numeros)
    elif escolha == 3:
        if len(lista_numeros) == 0:
            print('\nNenhum número foi adicionado ainda.\n')
        else:
            print(f'\nVocê digitou {len(lista_numeros)} número(s)\n')
            print(f'\nO maior número é {max(lista_numeros)}\n')
            print(f'\nO menor número é {min(lista_numeros)}\n')
            print(f'\nA soma dos números é de {sum(lista_numeros)}\n')
            print(f'\nA média é {sum(lista_numeros) / len(lista_numeros)}\n')
    elif escolha == 0:
        print('\nSaindo...')
        break
    else:
        print('\nOpção inválida!\n')
        