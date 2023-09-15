#1
def e_primo(num):
    for div in range(2, num):
        while div < num:
            if num % div == 0:
                print("não é primo")
                print(div)
            break
    else:
        print("é primo")

e_primo(80)


#2
def calcular_parcela(valor_divida, num_parcelas, taxa_juros):
    valor_total_com_juros = valor_divida * (1 + taxa_juros)
    valor_parcela = valor_total_com_juros / num_parcelas
    return valor_parcela, valor_total_com_juros


def mostrar_opcoes_parcelamento(valor_divida):
    print("Opções de Parcelamento:")
    print("Número de Parcelas - Juros - Valor Total - Valor da Parcela")
    
    for num_parcelas in [1, 3, 6, 9, 12]:
        if num_parcelas == 1:
            taxa_juros = 0.0
        elif num_parcelas == 3:
            taxa_juros = 0.10
        elif num_parcelas == 6:
            taxa_juros = 0.15
        elif num_parcelas == 9:
            taxa_juros = 0.20
        elif num_parcelas == 12:
            taxa_juros = 0.25

        valor_parcela, valor_total = calcular_parcela(valor_divida, num_parcelas, taxa_juros)
        print(f"{num_parcelas}x - {taxa_juros * 100}% - {valor_total} - {valor_parcela}")


valor_divida = float(input("Digite o valor da dívida: "))

# Mostra as opções de parcelamento
mostrar_opcoes_parcelamento(valor_divida)

#3
intervalo_0_25 = 0
intervalo_26_50 = 0
intervalo_51_75 = 0
intervalo_76_100 = 0

numero = int(input("Digite um número positivo (ou um número negativo para sair):"))

while numero >= 0:
    if 0 <= numero <= 25:
        intervalo_0_25 += 1
    elif 26 <= numero <= 50:
        intervalo_26_50 += 1
    elif 51 <= numero <= 75:
        intervalo_51_75 += 1
    elif 76 <= numero <= 100:
        intervalo_76_100 += 1
    
    numero = int(input("Digite um número positivo (ou um número negativo para sair):"))


print("Quantidade de números nos intervalos:")
print("0-25:", intervalo_0_25)
print("26-50:", intervalo_26_50)
print("51-75:", intervalo_51_75)
print("76-100:", intervalo_76_100)