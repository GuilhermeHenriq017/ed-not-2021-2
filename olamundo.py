#print(): exibe informações
print("Olá, mundo!")

#input(): permite entrada de informações
nome = input('Qual é o seu nome? ')

print(f"Olá, {nome}!")

#int() converte o que foi onformado no input() de texto para NÚMERO INTEIRO
idade = int(input('Informe a sua idade: '))

if idade >= 18:
    print("Você já pode beber.")
    print("Você já pode tirar habilitação.")

else:
    print("Você não pode beber.")
    print("Você não pode tirar habilitação.")