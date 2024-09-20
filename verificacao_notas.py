notas = []

for i in range(10):
    while True:
        try:
            nota = float(input(f"Digite a nota do aluno {i + 1} (entre 0 e 10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("A nota deve estar entre 0 e 10. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

maior_nota = notas[0]
menor_nota = notas[0]

for nota in notas:
    if nota > maior_nota:
        maior_nota = nota
    if nota < menor_nota:
        menor_nota = nota

print(f"\nA maior nota é: {maior_nota}")
print(f"A menor nota é: {menor_nota}")
