
'''
DESAFIO 4 — PROJEÇÃO DE FREQUÊNCIA

O programa estima quantas aulas consecutivas o aluno
precisa frequentar para atingir 75% de frequência.

Também calcula o tempo estimado em semanas e meses.
'''

# Importa a biblioteca math para utilizar o arredondamento para cima
import math


# Constantes utilizadas nos cálculos
FATOR_FALTA = 1.25
FREQUENCIA_MINIMA = 75


# Apresentação do programa
print("=" * 55)
print("       SISTEMA DE PROJEÇÃO DE FREQUÊNCIA")
print("=" * 55)
print()

print("Informe os dados disponíveis no sistema da ETEC.")
print("-" * 55)


# Solicita o nome da matéria e remove espaços extras
nome_materia = input("Nome da matéria: ").strip()


# Solicita as faltas exibidas no sistema
# O replace permite digitar decimais com vírgula ou ponto
faltas_sistema = float(
    input("Faltas exibidas no sistema: ").replace(",", ".")
)


# Solicita a frequência atual da matéria em porcentagem
frequencia = float(
    input("Frequência atual (%): ").replace(",", ".")
)


# Verifica se o nome da matéria foi informado
if nome_materia == "":
    print("Erro: informe o nome da matéria.")


# Verifica se a quantidade de faltas é negativa
elif faltas_sistema < 0:
    print("Erro: as faltas não podem ser negativas.")


# Verifica se a frequência está entre 0% e 100%
elif frequencia < 0 or frequencia > 100:
    print("Erro: a frequência deve estar entre 0 e 100.")


# Verifica se as faltas e a frequência são inconsistentes
# Zero faltas deve corresponder a 100% de frequência
# Frequência de 100% deve corresponder a zero faltas
elif (faltas_sistema == 0 and frequencia < 100) or (
    faltas_sistema > 0 and frequencia == 100
):
    print("Erro: as faltas e a frequência são inconsistentes.")


# Se a frequência for igual ou superior a 75%,
# o aluno já atingiu a meta mínima
elif frequencia >= FREQUENCIA_MINIMA:

    print()
    print("=" * 55)
    print(f"       RELATÓRIO: {nome_materia.upper()}")
    print("=" * 55)
    print()

    print(f"Frequência atual: {frequencia:.2f}%")
    print("Você já atingiu a frequência mínima de 75%.")
    print("Continue frequentando as aulas para manter sua frequência.")


# Se nenhuma das condições anteriores for verdadeira,
# o aluno está abaixo da frequência mínima
else:

    # Converte as faltas do sistema em aulas perdidas
    # Exemplo: 15 / 1.25 = 12 aulas perdidas
    faltas_aulas = faltas_sistema / FATOR_FALTA


    # Calcula a proporção de faltas
    # Exemplo: 100% - 72.72% = 27.28%
    proporcao_faltas = 1 - (frequencia / 100)


    # Estima o total de aulas dadas usando as faltas
    # e a proporção de faltas calculada anteriormente
    total_aulas_estimado = faltas_aulas / proporcao_faltas


    # Estima quantas aulas o aluno frequentou
    # Presenças = total de aulas - aulas perdidas
    presencas_estimadas = total_aulas_estimado - faltas_aulas


    # Calcula quantas aulas consecutivas são necessárias
    # para atingir a frequência mínima de 75%
    #
    # A fórmula considera que cada nova aula frequentada
    # aumenta tanto o total de aulas quanto as presenças
    aulas_necessarias = math.ceil(
        (FREQUENCIA_MINIMA / 100 * total_aulas_estimado
         - presencas_estimadas)
        / (1 - FREQUENCIA_MINIMA / 100)
    )


    # Garante que o resultado não seja negativo
    aulas_necessarias = max(0, aulas_necessarias)


    # Exibe o relatório da matéria
    print()
    print("=" * 55)
    print(f"       RELATÓRIO: {nome_materia.upper()}")
    print("=" * 55)
    print()

    print(f"Frequência informada: {frequencia:.2f}%")
    print(f"Faltas convertidas em aulas: {faltas_aulas:.2f}")
    print(f"Total aproximado de aulas: {total_aulas_estimado:.2f}")
    print()

    print(f"Aulas consecutivas estimadas: {aulas_necessarias}")


    # Solicita a quantidade de aulas semanais da matéria
    print()
    print("-" * 55)
    print("       PROJEÇÃO DE TEMPO")
    print("-" * 55)

    aulas_semanais = float(
        input("Quantas aulas por semana dessa matéria? ").replace(",", ".")
    )


    # Verifica se a quantidade de aulas semanais é válida
    if aulas_semanais <= 0:
        print("Erro: informe uma quantidade positiva de aulas semanais.")


    else:

        # Divide as aulas necessárias pelas aulas semanais
        # para estimar quantas semanas serão necessárias
        semanas = aulas_necessarias / aulas_semanais


        # Considera meses com aproximadamente 4 semanas
        meses = semanas / 4


        # Exibe os resultados da projeção
        print()
        print(f"Aulas presenciais necessárias: {aulas_necessarias}")
        print(f"Semanas estimadas: {semanas:.2f}")
        print(f"Meses estimados: {meses:.2f}")

        print()
        print("-" * 55)
        print("ATENÇÃO: esta projeção é uma estimativa.")
        print("Ela considera que você não terá novas faltas.")
        print("-" * 55)
