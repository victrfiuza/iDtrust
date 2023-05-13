print("=="*31)
print("VALIDAÇÃO DE IDADE".center(62))
print("=="*31)

sexo = input("Digite o sexo: ").lower()
idade = int(input("Digite a idade: "))
print("--"*31)
if idade >= 65 and sexo == "masculino":
    print("APOSENTADO")
elif idade >= 60 and sexo == "feminino":
    print("APOSENTADA")
elif idade >= 13 and idade <= 18 and (sexo == "masculino" or sexo == "feminino"):
    print("ADOLESCENTE")
elif idade < 13 and (sexo == "masculino" or sexo == "feminino"):
    print("CRIANÇA")
elif sexo == "masculino" or sexo == "feminino":
    print("ADULTO")
else:
    print("Algum dado está incorreto")
