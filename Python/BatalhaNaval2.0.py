# Batalha Naval. Realizando imports necessários:
from typing import List

# Variáveis Globais:

campo_de_batalha = []
numero_de_linhas = 20
numero_de_colunas = 20
qtd_porta_aviao = 3
qtd_cruzador = 4
qtd_fragata = 5


def criar_campo_de_batalha():
    global numero_de_linhas, numero_de_colunas, campo_de_batalha

    for linha in range(numero_de_linhas):
        campo_de_batalha.append("-" * numero_de_linhas)
    mostrar_campo_de_batalha()


def mostrar_campo_de_batalha():
    global campo_de_batalha, numero_de_linhas, numero_de_colunas

    for linha in range(numero_de_linhas):
        print(f'{linha}', end='')
        for coluna in range(numero_de_colunas):
            print(f'{(campo_de_batalha[linha][coluna])}', end='')
        print()
    for coluna in range(numero_de_colunas):
        print(f'{coluna}', end='')
    print()


def ler_dimensoes():
    global numero_de_linhas, numero_de_colunas

    print('Digite o tamanho do campo de batalha. Mínimo 10x10 e Máximo 30x30')

    numero_de_linhas = int(input('Digite o número de linhas do campo de batalha (Dimensão X): '))
    if 10 <= numero_de_linhas <= 30:
        numero_de_colunas = int(input('Digite o número de colunas do campo de batalha (Dimensão Y): '))
        if 10 <= numero_de_colunas <= 30:
            criar_campo_de_batalha()
        else:
            while numero_de_colunas < 10 or numero_de_colunas > 30:
                print('Número de linhas inválido, tente novamente.')
                numero_de_colunas = int(input('Digite o numero de linhas do campo de batalha (Dimensão Y): '))
    else:
        while numero_de_linhas < 10 or numero_de_linhas > 30:
            print('Número de colunas inválido, tente novamente.')
            numero_de_linhas = int(input('Digite o numero de colunas do campo de batalha (Dimensão X): '))


def jogar():
    on = True
    while on:
        print('Batalha Naval!')
        criar_campo_de_batalha()

    on = False


jogar()
