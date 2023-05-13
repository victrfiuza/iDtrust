print("=="*31)
print("VALIDAÇÃO DE IDADE".center(62))
print("=="*31)
print("Digite o sexo e a idade separados por ponto e virgula")
print("""Exemplos:
    1. masculino;74
    2. feminino;4""")
print('--'*31)

user_input = input("Digite o sexo;idade: ").lower().split(";")
sexo = user_input[0].strip()
idade = int(user_input[1].strip())
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
