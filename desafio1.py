# caractere = input("Digite uma letra: ")

# valor_decimal = ord(caractere)

# valor_hexadecimal = hex(valor_decimal)

# valor_binario = bin(valor_decimal)

# print(f"Letra digitada foi: {caractere}")
# print(f"Seu valor em decimal é: {valor_decimal}")
# print(f"Seu valor em hexadecimal é: {valor_hexadecimal}")
# print(f"Seu valor em binário é: {valor_binario}")

nome = input("Nome")
altura = float(input("Altura(m):"))
massa = float(input("Massa(kg):"))

imc = massa/(altura*altura)

print("Nome\tAltura\tMassa\tIMC\n{}\t{}\t{}\t{:.2f}".format(nome, altura, massa, imc))


