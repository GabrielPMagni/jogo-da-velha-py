from os import system, name

def resetar_tabela():
    return [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']


def resetar_tabela_bool():
    return [None, None, None, None, None, None, None, None, None]


def limpar_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def mostrar_tabela():
    contador = 0
    contador2 = 0
    for k in range(3):
        if k == 0:
            pass
        else:
            print('\n'+'-'*16)
        for j in range(3):
            contador2 += 1
            print(contador2, tabela[contador], end=' | ')
            contador += 1


def jogar_x():
    mostrar_tabela()
    try:
        escolha = int(input('\n\nJogador X, digite o número correspondente onde você quer jogar: \n\t>'))
        if escolha not in range(1, 10):
            limpar_tela()
            print('\033[31mSelecione números inteiros apenas de 1 até 9!\033[m')
            return jogar_x()
        elif tabela_bool[escolha - 1] is True or tabela_bool[escolha - 1] is False:
            limpar_tela()
            print('\033[33mEscolha outro local, esse já foi usado!\033[m')
            return jogar_x()
        else:
            tabela_bool[escolha - 1] = True
            tabela[escolha - 1] = 'X'

    except ValueError:
        limpar_tela()
        print('\033[31mDigite apenas números inteiros!\033[m')
        return jogar_x()


def jogar_o():
    mostrar_tabela()
    try:
        escolha = int(input('\n\nJogador O, digite o número correspondente onde você quer jogar: \n\t>'))
        if escolha not in range(1, 10):
            limpar_tela()
            print('\033[31mSelecione números inteiros apenas de 1 até 9!\033[m')
            return jogar_o()
        elif tabela_bool[escolha - 1] is True or tabela_bool[escolha - 1] is False:
            limpar_tela()
            print('\033[33mEscolha outro local, esse já foi usado!\033[m')
            return jogar_o()
        else:
            tabela_bool[escolha - 1] = False
            tabela[escolha - 1] = 'O'

    except ValueError:
        limpar_tela()
        print('\033[31mDigite apenas números inteiros!\033[m')
        return jogar_o()


def vencer():

    if (tabela_bool[0] is True and tabela_bool[1] is True and tabela_bool[2] is True) or (tabela_bool[3] is True and tabela_bool[4] is True and tabela_bool[5] is True) or (tabela_bool[6] is True and tabela_bool[7] is True and tabela_bool[8] is True):
        print('Jogador X é o vencedor!')
        return 1

    elif (tabela_bool[0] is True and tabela_bool[3] is True and tabela_bool[6] is True) or (tabela_bool[1] is True and tabela_bool[4] is True and tabela_bool[7]) or (tabela_bool[2] is True and tabela_bool[5] is True and tabela_bool[8] is True):
        print('Jogador X é o vencedor!')
        return 1

    elif (tabela_bool[0] is True and tabela_bool[4] is True and tabela_bool[8] is True) or (tabela_bool[2] is True and tabela_bool[4] is True and tabela_bool[6] is True):
        print('Jogador X é o vencedor!')
        return 1

    elif (tabela_bool[0] is False and tabela_bool[1] is False and tabela_bool[2] is False) or (tabela_bool[3] is False and tabela_bool[4] is False and tabela_bool[5] is False) or (tabela_bool[6] is False and tabela_bool[7] is False and tabela_bool[8] is False):
        print('Jogador O é o vencedor!')
        return 1

    elif (tabela_bool[0] is False and tabela_bool[3] is False and tabela_bool[6] is False) or (tabela_bool[1] is False and tabela_bool[4] is False and tabela_bool[7]) or (tabela_bool[2] is False and tabela_bool[5] is False and tabela_bool[8] is False):
        print('Jogador O é o vencedor!')
        return 1

    elif tabela_bool[0] is False and tabela_bool[4] is False and tabela_bool[8] is False or tabela_bool[2] is False and tabela_bool[4] is False and tabela_bool[6] is False:
        print('Jogador O é o vencedor!')
        return 1

    else:
        return 0


def repetir():
    try:
        repetidor = input('Gostaria de jogar de novo? [S/N]')
        if repetidor in 'Ss':
            global tabela
            global tabela_bool
            tabela = resetar_tabela()
            tabela_bool = resetar_tabela_bool()
            return jogo()
        elif repetidor in 'Nn':
            exit('Até')
        else:
            print('Valor inválido, tente novamente')
            limpar_tela()
            return repetir()

    except ValueError:
        print('Valor inválido, tente novamente')
        return repetir()


def jogo():
    for i in range(1, 10):
        contador = 0

        limpar_tela()
        jogar_x()
        a = vencer()
        if a == 1:
            repetir()
            break

        for item in tabela_bool:
            if item is not None:
                contador += 1
            else:
                pass
        if contador == 9:
            print('Ninguém venceu!')
            repetir()
            break
        limpar_tela()
        jogar_o()
        a = vencer()
        if a == 1:
            repetir()
            break


vencedor = None
tabela = resetar_tabela()
tabela_bool = resetar_tabela_bool()
jogo()
