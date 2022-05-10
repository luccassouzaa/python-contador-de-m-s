#criar um contador que vê o valor do salario no final do mês



#criar a variavel do salario diario

hora = int(input("Salario por hora: "))
horatrabalho = int(input("Quantas horas por dia você trabalha: "))
salariodia = hora * horatrabalho
print(f"Seu salario diario será R$ {salariodia:,.2f}")

#semanal

diasemana = int(input("Quantos dias da semana você trabalha: "))
salariosemana = diasemana * salariodia
print(f"Seu salario semanal será de aproximadamente R$: {salariosemana:,.2f}")
#mensal

salariosemanal = int(input("Quantas semanas por mês você trabalha: "))
salariomes = salariosemanal * salariosemana
print(f"Seu salario mensal será de aproximadamente R$: {salariomes:,.2f}")

if salariomes<=3000.00:
    print("Salario classe baixa")

elif (salariomes<=7000):
    print("Salario classe média")

else:
    print("Salario Classe Alta")