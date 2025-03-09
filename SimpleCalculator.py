primeiro_numero = int(input('Primeiro número: '))
segundo_numero = int(input('Segundo número: '))

menu = 0



while menu != 5:
    print('==-==-==-==-==-==-==-')
    print('[ 1 ] SOMAR')
    print('[ 2 ] Multiplicar')
    print('[ 3 ] Qual o maior')
    print('[ 4 ] Novos números')
    print('[ 5 ] Sair do programa')
    menu = int(input('Qual você escolhe ? '))



    if menu == 1:
        soma = primeiro_numero + segundo_numero
        print(soma)

    
    elif menu == 2:
        multiplicar = primeiro_numero * segundo_numero
        print(multiplicar)
    
    elif menu == 3:
        maior = max(primeiro_numero, segundo_numero)
        print(maior)

    elif menu == 4:
        primeiro_numero = int(input('Primeiro número: '))
        segundo_numero = int(input('Segundo número: '))

    elif menu == 5:
        print('Saindo do programa...')
        break # Sai do loop quando escolher a opção 5



    else:
        print('Opção inválida! Tente novamente...')

    continuar = str(input('Deseja continuar ? [S/N] ')).upper()
    
    if continuar == 'N':
        print('Saindo do programa...')
        break