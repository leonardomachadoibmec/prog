a = float(input("valor de a: "))
b = float(input("valor de b: "))
c = float(input("valor de c: "))


delta = (b**2) - 4 * a * c

#calcular formula de bhaskara
num1 = ((-b + (delta ** 1/2)) / 2 * a)
num2 = ((-b - (delta ** 1/2)) / 2 * a)



print(num1 , num2)


#########################################################################


ano = int(input("informe o ano: "))

n = (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))


print(n)







