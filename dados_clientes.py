def capturar_dados_clientes(num_clientes):
    clientes = []
    
    for i in range(num_clientes):
        print(f"\nInsira os dados do cliente {i + 1}:")
        nome = input("Nome: ")
        idade = input("Idade: ")
        cpf = input("CPF: ")
        
        cliente = {
            'Nome': nome,
            'Idade': idade,
            'CPF': cpf
        }
     
        clientes.append(cliente)
    
    return clientes

def salvar_dados_arquivo(clientes, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(f"{'Nome':<20}{'Idade':<10}{'CPF':<15}\n")
        arquivo.write("="*45 + "\n")
        
        for cliente in clientes:
            arquivo.write(f"{cliente['Nome']:<20}{cliente['Idade']:<10}{cliente['CPF']:<15}\n")
    
    print(f"Dados salvos no arquivo '{nome_arquivo}' com sucesso!")

clientes = capturar_dados_clientes(2)

salvar_dados_arquivo(clientes, 'clientes.txt')
