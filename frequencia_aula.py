
'''
DESAFIO 4 — PROJEÇÃO DE FREQUÊNCIA

Calcula uma estimativa de quantas aulas consecutivas
o aluno precisa frequentar para atingir 75% de frequência.
'''

import math

FATOR_FALTA = 1.25
FREQUENCIA_MINIMA = 75

print("=" * 55)
print("       SISTEMA DE PROJEÇÃO DE FREQUÊNCIA")
print("=" * 55)
print()
print("Informe os dados disponíveis no sistema da ETEC.")
print("-" * 55)

nome_materia = input("Nome da matéria: ").strip()

try:
    faltas_sistema = float(
        input("Faltas exibidas no sistema: ").replace(",", ".")
    )
    frequencia = float(
        input("Frequência atual (%): ").replace(",", ".")
    )

    if not nome_materia:
        raise ValueError("O nome da matéria não pode ficar vazio.")

    if faltas_sistema < 0:
        raise ValueError("As faltas não podem ser negativas.")

    if not 0 <= frequencia <= 100:
        raise ValueError("A frequência deve estar entre 0 e 100.")

    if faltas_sistema == 0 and frequencia < 100:
        raise ValueError(
            "Os dados são inconsistentes: há frequência abaixo de "
            "100%, mas nenhuma falta informada."
        )

    print()
    print("=" * 55)
    print(f"       RELATÓRIO: {nome_materia.upper()}")
    print("=" * 55)
    print()
    print(f"Frequência informada: {frequencia:.2f}%")

    if frequencia >= FREQUENCIA_MINIMA:
        print("Você já atingiu a frequência mínima de 75%.")
        print("Continue frequentando as aulas para manter sua frequência.")

    else:
        faltas_aulas = faltas_sistema / FATOR_FALTA

        proporcao_faltas = 1 - (frequencia / 100)

        total_aulas_estimado = faltas_aulas / proporcao_faltas
        presencas_estimadas = total_aulas_estimado - faltas_aulas

        aulas_necessarias = math.ceil(
            (FREQUENCIA_MINIMA / 100 * total_aulas_estimado
             - presencas_estimadas)
            / (1 - FREQUENCIA_MINIMA / 100)
        )

        aulas_necessarias = max(0, aulas_necessarias)

        print(f"Faltas convertidas em aulas: {faltas_aulas:.2f}")
        print(f"Total aproximado de aulas: {total_aulas_estimado:.2f}")
        print()
        print(f"Aulas consecutivas estimadas: {aulas_necessarias}")

        print()
        print("-" * 55)
        print("       PROJEÇÃO DE TEMPO")
        print("-" * 55)

        aulas_semanais = float(
            input("Quantas aulas por semana dessa matéria? ").replace(",", ".")
        )

        if aulas_semanais <= 0:
            print("Erro: informe uma quantidade positiva de aulas semanais.")
        else:
            semanas = aulas_necessarias / aulas_semanais
            meses = semanas / 4

            print()
            print(f"Aulas presenciais necessárias: {aulas_necessarias}")
            print(f"Semanas estimadas: {semanas:.2f}")
            print(f"Meses estimados: {meses:.2f}")

            print()
            print("-" * 55)
            print("ATENÇÃO: projeção baseada em valores estimados.")
            print("A frequência arredondada pode alterar o resultado.")
            print("Considere nenhuma nova falta durante a recuperação.")
            print("-" * 55)

except ValueError as erro:
    print()
    print(f"Erro nos dados informados: {erro}")
