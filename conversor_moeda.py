TAXA_BITCOIN_PARA_REAL = 135000
TAXA_REAL_PARA_BITCOIN = 1 / TAXA_BITCOIN_PARA_REAL

def exibir_menu():
    print("\nConversor de Criptomoedas")
    print("1- Converter Bitcoin em Reais.")
    print("2- Converter Reais em Bitcoin.")
    print("3- Sair.")

def converter_bitcoin_para_reais():
    bitcoins = float(input("Digite a quantidade de Bitcoins: "))
    reais = bitcoins * TAXA_BITCOIN_PARA_REAL
    print(f"{bitcoins} Bitcoins equivalem a R${reais:.2f} Reais.")

def converter_reais_para_bitcoin():
    reais = float(input("Digite a quantidade de Reais: "))
    bitcoins = reais * TAXA_REAL_PARA_BITCOIN
    print(f"R${reais:.2f} Reais equivalem a {bitcoins:.6f} Bitcoins.")

def menu_principal():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            converter_bitcoin_para_reais()
        elif opcao == "2":
            converter_reais_para_bitcoin()
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu_principal()
