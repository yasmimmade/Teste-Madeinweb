# # 1-a)
# print(b) será (20). E print (a, b) será (10, 5).

# # 1-b)
# print(c) será (50), print(b, c) será (10, 50) e print(a, b, c) será (30, 10, 40).

# # 1-c)
# print(a, b, c) será (10, 10, 10)

# # 1-d)
# print(a) será (12) e print(a, b) será (14, 13)

# # 1-e)
# print(a, b, c) será (10, 20, 15)

# # 1-f)
# print(z) será (1) e print(x, y, z) será (5, 6, 1)

# 2- Escreva um algoritmo que armazene o valor 10 em uma variável A e o valor 20 em uma variável B. A seguir (utilizando apenas atribuições entre variáveis) troque os seus conteúdos fazendo com que o valor que está em A passe para B e vice-versa. Ao final, escrever os valores que ficaram armazenados nas variáveis. 

a = 10
b = 20
c = 10

a = b 
b = c

print(a, b)

# 3- Escreva um algoritmo para ler um valor (do teclado) e escrever (na tela) o seu antecessor. 

valor = int(input("Digite um valor: "))

print(valor - 1)

# 4- Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com 365 dias e mês com 30 dias.

idade = int(input("Digite sua idade: "))

dias = idade * 365

print(f"Sua idadade é de: {dias} dias")

# 5-  Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

votoBranco = int(input("Digite o total de votos em brancos: "))
votoNulo = int(input("Digite o total de votos nulos: "))
votoValido = int(input("Digite o total de votos válidos: "))

eleitores = votoBranco + votoNulo + votoValido

print(f"Nessa eleição hoveram {eleitores} eleitores. Destes, {votoBranco} pessoas votaram em branco, {votoNulo} votaram nulo e as demais {votoValido} votaram em seus respectivos canditados.")

# 6- Ler um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10! 

numero = int(input("Digite um valor para saber se é maior que 10: "))

if numero < 10:
    print(f"{numero} não é maior que 10.")
else:
    print(f"{numero} é maior que 10!"),

# 7- Ler um valor e escrever se é positivo ou negativo (considere o valor zero como positivo)

valor1 = int(input("Digite um número: "))

if valor1 < 0:
    print(f"{valor1} é negativo!")
else:
     print(f"{valor1} é positivo!")

# 8- As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra. 

maca = int(input("Digite o número de maçãs compradas: "))

if maca < 12:
    total = maca * 1.30
else:
    total = maca * 1

print(f"Seu total foi de: {total} reais.")

# 9-  Ler as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada. 

nota1 = float(input("Digite sua nota 1a: "))
nota2 = float(input("Digite sua nota 2a: "))

media = (nota1 + nota2) / 2

if media < 6:
    print(f"Sua média foi {media}, você está reprovado!")
else:
    print(f"Sua média foi {media}, você está aprovado!")

# 10-  Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente

v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

if v1 == v2:
    print("Por favor digite valores diferentes.")
elif v1 > v2:
    print(v2, v1)
else:
    print(v1, v2)

# 11- Escreva um algoritmo para imprimir os números de 1 (inclusive) a 10 (inclusive) em ordem decrescente. 

i = 1

while i <= 10:
    print(i)
    i += 1

# 12-  Ler um valor N e imprimir todos os valores inteiros entre 1 (inclusive) e N (inclusive). Considere que o N será sempre maior que ZERO. 

n = int(input("Digite um valor maior que 0: "))

while n <= 0:
    print("Por favor, digite um número que seja maior que 0")
    n = int(input("Digite o valor: "))

i = 1

while i <= n:
    print(i)
    i += 1
    
# 10- Ler 10 valores (considere que não serão informados valores iguais) e escrever o maior deles. 

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
n4 = int(input("Digite o quarto número: "))
n5 = int(input("Digite o quinto número: "))
n6 = int(input("Digite o sexto número: "))
n7 = int(input("Digite o sétimo número: "))
n8 = int(input("Digite o oitavo número: "))
n9 = int(input("Digite o nono número: "))
n10 = int(input("Digite o decimo número: "))

if n1 > n2 and n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5 and n1 > n6 and n1 > n7 and n1 > n8 and n1 > n9 and n1 > n10:
    print(n1)
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5 and n2 > n6 and n2 > n7 and n2 > n8 and n2 > n9 and n2 > n10:
    print(n2)
elif n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5 and n3 > n6 and n3 > n7 and n3 > n8 and n3 > n9 and n3 > n10:
    print(n3)
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5 and n4 > n6 and n4 > n7 and n4 > n8 and n4 > n9 and n4 > n10:
    print(n4)
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4 and n5 > n6 and n5 > n7 and n5 > n8 and n5 > n9 and n5 > n10:
    print(n5)
elif n6 > n1 and n6 > n2 and n6 > n3 and n6 > n4 and n6 > n5 and n6 > n7 and n6 > n8 and n6 > n9 and n6 > n10:
    print(n6)
elif n7 > n1 and n7 > n2 and n7 > n3 and n7 > n4 and n7 > n5 and n7 > n6 and n7 > n8 and n7 > n9 and n7 > n10:
    print(n7)
elif n8 > n1 and n8 > n2 and n8 > n3 and n8 > n4 and n8 > n5 and n8 > n6 and n8 > n7 and n8 > n9 and n8 > n10:
    print(n8)
elif n9 > n1 and n9 > n2 and n9 > n3 and n9 > n4 and n9 > n5 and n9 > n6 and n9 > n7 and n9 > n8 and n9 > n10:
    print(n9)
else:
    print(n10)

# 14-  Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores válidos durante a leitura (0 a 10) para cada nota.

p1 = int(input("Digite sua nota 1a: "))
p2 = int(input("Digite sua nota 2a: "))

while p1 < 0 or p1 > 10 or p2 < 0 or p2 > 10:
    print("Sua nota não pode ter sido menor que zero ou maior que 10")
    p1 = int(input("Digite novamente sua nota 1a: "))
    p2 = int(input("Digite novamente sua nota 2a: "))

mediana = (p1 + p2) / 2

print(f"Sua média foi: {mediana}")

# 15- Ler 10 valores e após a leitura de todos, escrever quais desses valores lidos são NEGATIVOS. 

# 16-  Sendo a sequência Fibonacci: 1,2,3,5,8,13,21, escreva um algoritmo que imprima os 10 primeiros números da sequência

x = 0
y = 1
z = x + y

for i in range(1, 11, 1):
    print(z)
    y = x
    x = z
    z = x + y