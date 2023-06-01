mulher = 0
homem = 0

idadem = 0
idadeh = 0
s = str(input("Informe o sexo:\n1-Feminino\n2-Masculino\nR: "))

for n in range (1,11):
    i = int(input("Informe a idade: "))
    if s == 1:
        mulher += 1
        idadem += i
    elif s == 2:
        homem += 1
        idadeh += i

mediamulher = idadem/mulher
print(f"Idade média das mulheres: {mediamulher}")

mediahomem = idadeh/homem
print(f"Idade média dos homens: {mediahomem}")

geral =(idadem+idadeh) / (mulher+homem)
print(f"Idade média do grupo: {geral}")
