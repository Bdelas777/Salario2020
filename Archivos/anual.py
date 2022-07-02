def anual(Base_IMP,Retiene,salarioanual,gastoanual,deducciones_autorizadas,salariogastos):
	print("El ciclo solo se dentendra al pulsar 0")
	p=float(input("Ingresa tu PP "))
	PP=0
	while(p!=0):
		PP=PP+p
		PP=round(PP,2)
		p=float(input())
	print("$ ",salarioanual,"Salario sin restar gastos","\n")
	print("$ ",gastoanual," gastos","\n")
	print("$ ",salariogastos," Ingresos acumulables","\n")
	print("$ ",deducciones_autorizadas," Deducciones personales","\n")
	print("$ ",Base_IMP," Base de IMP","\n")
	print("$ ",Retiene," ISR anual","\n")
	print("$ ",PP," PP","\n")
	saldo=Retiene-PP
	saldo=round(saldo,2)
	print("$ ",saldo," saldo en contra","\n")
	salario=Base_IMP-saldo
	salario=round(salario,2)
	#print("$ ",salario," salario anual","\n")


