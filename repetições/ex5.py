homem_mais_velho = ""
idade_homem_mais_velho = 0
mulheres_menos_20 = 0

for i in range(1, 9):
    print(f" Pessoa {i} ")
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    sexo = input("Digite o sexo (M/F): ")

    if sexo.upper() == "M" and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade

    if sexo.upper() == "F" and idade < 20:
        mulheres_menos_20 += 1

print(f"\nO homem mais velho é: {homem_mais_velho}")
print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_menos_20}")