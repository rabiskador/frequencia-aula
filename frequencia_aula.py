'''
DESAFIO 4 — PROJEÇÃO DE FREQUÊNCIA

Crie um sistema que analise a frequência do aluno e calcule
quantas aulas consecutivas ele precisa frequentar para atingir
75% de frequência.

O sistema também deve calcular quantas semanas e meses serão
necessários para alcançar essa meta.
'''

print("=" * 55)
print("       SISTEMA DE PROJEÇÃO DE FREQUÊNCIA")
print("=" * 55)
print()
print("Este sistema calcula sua frequência atual e, caso esteja")
print("abaixo de 75%, informa quantas aulas você precisa")
print("frequentar para atingir a frequência mínima.")
print()
print("INFORME OS DADOS DA MATÉRIA:")
print("-" * 55)

nome_materia = input("Nome da matéria: ")
quantidade_aulas = int(input("Quantidade de aulas dadas: "))
quantidade_faltas = float(input("Quantidade de faltas: "))

quantidade_presencas = quantidade_aulas - quantidade_faltas
frequencia = (quantidade_presencas / quantidade_aulas) * 100

freq_aumento = (3 * quantidade_faltas) - quantidade_presencas


if freq_aumento > 0:

    print()
    print("=" * 55)
    print(f"      RELATÓRIO DE RECUPERAÇÃO: {nome_materia}")
    print("=" * 55)
    print()
    
    print(f"Frequência Atual: {frequencia:.1f}%")
    print(f"Necessidade: Você precisa de {freq_aumento:.0f} aulas seguidas.")
    print()
    
    print("-" * 55)
    print("       VAMOS CALCULAR O TEMPO NECESSÁRIO")
    print("-" * 55)
    print()
    
    aulas_semanas = float(
        input("Insira quantas aulas por semana você tem dessa matéria: ")
    )
    
    print()
    
    semanas_necessarias = freq_aumento / aulas_semanas
    meses_necessarios = semanas_necessarias / 4
    
    print("=" * 55)
    print("       META PARA ATINGIR 75% DE PRESENÇA")
    print("=" * 55)
    print()
    
    print(f"Aulas presenciais necessárias: {freq_aumento:.0f}")
    print(f"Semanas consecutivas: {semanas_necessarias:.1f}")
    print(f"Meses de frequência perfeita: {meses_necessarios:.1f}")
    
    print()
    print("-" * 55)
    print("AVISO: Você NÃO pode faltar nenhuma vez")
    print("durante esse período de recuperação!")
    print("-" * 55)


else:

    print()
    print("=" * 55)
    print(f"           MATÉRIA: {nome_materia}")
    print("=" * 55)
    print()
    
    print(f"Frequência Atual: {frequencia:.1f}%")
    print()
    print("✓ Tudo certo!")
    print("Você já está na zona segura (igual ou acima de 75%).")
    print("Continue administrando suas presenças para não cair.")
    print()
    print("=" * 55)