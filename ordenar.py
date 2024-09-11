def ordenar_funcionarios(codigos):
    n = len(codigos)
    # Implementação do Bubble Sort
    for i in range(n):
        # O laço interno percorre a lista não ordenada
        for j in range(0, n - i - 1):
            # Compara os elementos adjacentes
            if codigos[j] > codigos[j + 1]:
                # Troca os elementos se estiverem fora de ordem
                codigos[j], codigos[j + 1] = codigos[j + 1], codigos[j]
    return codigos

# Lista de códigos de matrícula dos funcionários
codigos_funcionarios = [103, 121, 104, 102, 99]

# Ordena a lista
codigos_ordenados = ordenar_funcionarios(codigos_funcionarios)

# Exibe a lista ordenada
print("Lista ordenada de códigos de matrícula dos funcionários:")
print(codigos_ordenados)
