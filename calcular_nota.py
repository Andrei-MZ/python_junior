def main():
    num_turmas = 9
    alunos_por_turma = 24
    avaliacoes_por_aluno = 5

    turmas = {}

    for turma in range(1, num_turmas + 1):
        print(f"\nTurma {turma}:")
        turmas[turma] = {}

        for aluno in range(1, alunos_por_turma + 1):
            nome = input(f"  Nome do Aluno {aluno}: ")
            notas = []

            for avaliacao in range(1, avaliacoes_por_aluno + 1):
                nota = float(input(f"    Nota da avaliação {avaliacao}: "))
                notas.append(nota)

            turmas[turma][nome] = notas  

    for turma, alunos in turmas.items():
        print(f"\nMédias da Turma {turma}:")
        for nome, notas in alunos.items():
            media = sum(notas) / len(notas)
            print(f"  {nome}: Média = {media:.2f}")

if __name__ == "__main__":
    main()
