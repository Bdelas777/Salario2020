def horas_extra(sal,aum,respuesta):
	horas=int(input("¿Cuantas horas extra trabajo? "))
	if respuesta=="m" or respuesta=="M":
		aum=sal/30.4
		aum=round(aum,2)
		jornada=input("¿Cual es su jornada?(d/n/m) ")
		if jornada=="d":
			aum=aum/8
			aum=round(aum,2)
		elif jornada=="n":
			aum=aum/7
			aum=round(aum,2)
		elif jornada=="m":
			aum=aum/7.5
			aum=round(aum,2)
		aum=aum*2
		aum=round(aum,2)
		aum=aum*horas
		aum=round(aum,2)
		salario2=aum
		return salario2
		
	if respuesta=="q" or respuesta=="Q":
		aum=sal/14
		aum=round(aum,2)
		jornada=input("¿Cual es su jornada?(d/n/m) ")
		if jornada=="d":
			aum=aum/8
			aum=round(aum,2)
		elif jornada=="n":
			aum=aum/7
			aum=round(aum,2)
		elif jornada=="m":
			aum=aum/7.5
			aum=round(aum,2)
		aum=aum*2
		aum=round(aum,2)
		aum=aum*horas
		aum=round(aum,2)
		salario2=aum
		return salario2

	if respuesta=="s" or respuesta=="S":
		aum=sal/7
		aum=round(aum,2)
		jornada=input("¿Cual es su jornada?(d/n/m) ")
		if jornada=="d":
			aum=aum/8
			aum=round(aum,2)
		elif jornada=="n":
			aum=aum/7
			aum=round(aum,2)
		elif jornada=="m":
			aum=aum/7.5
			aum=round(aum,2)
		aum=aum*2
		aum=round(aum,2)
		aum=aum*horas
		aum=round(aum,2)
		salario2=aum
		return salario2
		
	if respuesta=="a" or respuesta=="A":
		pass