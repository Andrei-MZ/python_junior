# condicionais 1

idade = int( input("Informe a sua idade: ") )

if idade >= 18:
    print("PERMITIDO!")
else:
    print("NEGADO!")

# condicionais 2

salario = float(input("Informe seu salário: "))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <=6000:
    print("programador pleno")
elif salario > 6000 and salario <=15000:
    print("programador senior")
else: 
    ("gerente de projetos")
