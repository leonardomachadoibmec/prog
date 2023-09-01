#1
def salario(valor_horas, horas_trabalhadas):
 s = valor_horas * horas_trabalhadas
 print(f'o valor a ser recebido é {s}')


v = float(input("quanto vale a hora trabalhada: "))
h = float(input("quantas horas foram trabalhadas: "))
salario(v, h)

######################################################

#2
n1 = float(input("digite um valor: "))
n2 = float(input("digite outro valor: "))
n3 = float(input("ditite o ultimo valor: " ))

print((n1*2) * (n2/2))
print((3*n1) + n3)
print(n3 ** 3)

#####################################################

#3
def num(n1,n2,n3):
 a1 = (n1*2) * (n2/2)
 a2 = (3*n1) + n3
 a3 = n3 ** 3
 print(f"os valores são: {a1}, {a2}, {a3}")


a = float(input("digite um número: ")) 
b = float(input("digite outro valor: "))
c = float(input("digite o ultimo valor: "))
num =(a, b ,c)

##################################################### 

#4
def verificar_ano_bissexto(ano):
 a = ano
 print(f"{a}")


anoA = int(input("informe o ano: "))
BIS = (anoA % 4 == 0 and (anoA % 100 != 0 or anoA % 400 == 0))
verificar_ano_bissexto(BIS)




