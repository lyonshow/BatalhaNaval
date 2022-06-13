# Batalha Naval. Realizando imports necessários:
from typing import List

# Variáveis Globais:
campo_de_batalha = ['']
numero_de_linhas = 20
numero_de_colunas = 20
qtd_porta_aviao = 3
qtd_cruzador = 4
qtd_fragata = 5


def criar_campo_de_batalha():
    global numero_de_linhas, numero_de_colunas, campo_de_batalha

    for linha in range(numero_de_linhas):
        campo_de_batalha.append('-' * numero_de_linhas)
