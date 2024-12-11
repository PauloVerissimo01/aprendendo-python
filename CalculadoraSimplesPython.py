print(" ##### Calculadora em Python ###### \n \n")

print("Selecione a Operação Desejada: \n ")
print("1- Adição")
print("2- Subtração") 
print("3- Multiplicação") 
print ("4- Divisão")


opcao = input("Digite a Opção ")

if opcao == '1': 
    v1 = float(input("Digite o primeiro valor \n ")) 
    v2 = float(input("Deigite o segundo valor \n "))

    print("Adição \n")

    def soma(v1,v2):
        soma = v1 +v2
        return print(v1,"+",v2, " = ", soma)

    soma(v1,v2)

if opcao =='2':
    v1 = float(input("Digite o primeiro valor \n ")) 
    v2 = float(input("Deigite o segundo valor \n "))

    def subtracao(v1,v2):
        subtracao = v1-v2
        return print(v1,"-",v2, " = ", subtracao)

    subtracao(v1,v2)

if opcao =='3': 
    v1 = float(input("Digite o primeiro valor \n ")) 
    v2 = float(input("Deigite o segundo valor \n "))

    def multiplicacao(v1,v2):
        multi = v1 * v2
        return print(v1,"*",v2, " = ", multi)

    multiplicacao(v1,v2)

if opcao=='4':
    v1 = float(input("Digite o primeiro valor \n ")) 
    v2 = float(input("Deigite o segundo valor \n "))
        
    def divisao(v1,v2):
        div = v1 / v2
        return print(v1,"/",v2, " = ", div)

    divisao(v1,v2)
else:
        print('\n \n Opçao Inválida')
    