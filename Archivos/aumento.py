def aumentar(sal,aum,respuesta):
	dias=int(input("¿Cuantos dias inhabiles? "))
	if respuesta=="m" or respuesta=="M":
		aum=sal/30.4
		aum=round(aum,2)
		aum=aum*2
		aum=round(aum,2)
		aum=aum*dias
		aum=round(aum,2)
		salario2=sal+aum
		return salario2

	if respuesta=="q" or respuesta=="Q":
		aum=sal/14
		aum=round(aum,2)
		aum=aum*2
		aum=round(aum,2)
		aum=aum*dias
		aum=round(aum,2)
		salario2=sal+aum
		return salario2

	if respuesta=="s" or respuesta=="S":
		aum=sal/7
		aum=round(aum,2)
		aum=aum*2
		aum=round(aum,2)
		aum=aum*dias
		aum=round(aum,2)
		salario2=sal+aum
		return salario2
		
	if respuesta=="a" or respuesta=="A":
		aum=sal/52
		aum=round(aum,2)
		aum=aum*2
		aum=round(aum,2)
		aum=aum*dias
		aum=round(aum,2)
		salario2=sal+aum
		return salario2