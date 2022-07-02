def vacaciones(sal,respuesta,antiguedad,prima_vacacional):
	if antiguedad==1:
		dias=6
	if antiguedad==2:
		dias=8
	if antiguedad==3:
		dias=10
	if antiguedad==4:
		dias=12
	if antiguedad>=5 and antiguedad<9:
		dias=14
	if antiguedad>=10 and antiguedad<15:
		dias=16
	if antiguedad>=15 and antiguedad<20:
		dias=18
	if antiguedad>=20 and antiguedad<25:
		dias=20
	if antiguedad>=25 and antiguedad<30:
		dias=22
	if antiguedad>=30 and antiguedad<35:
		dias=24
	if antiguedad>=35 and antiguedad<40:
		dias=28
	if antiguedad>=40 and antiguedad<45:
		dias=30
	if antiguedad>=50 and antiguedad<55:
		dias=32
	prima_vacacional=prima_vacacional/100
	if respuesta=="m" or respuesta=="M":
		vaca=sal/30.4
		vaca=round(vaca,2)
		vaca=vaca*dias
		vaca=round(vaca,2)
		prima=vaca*prima_vacacional
		prima=round(prima,2)
		sal_vaca=prima
		sal_vaca=round(sal_vaca,2)
		return sal_vaca
	if respuesta=="q" or respuesta=="Q":
		vaca=sal/14
		vaca=round(vaca,2)
		vaca=vaca*dias
		vaca=round(vaca,2)
		prima=vaca*prima_vacacional
		prima=round(prima,2)
		sal_vaca=prima
		sal_vaca=round(sal_vaca,2)
		return sal_vaca
	if respuesta=="s" or respuesta=="S":
		vaca=sal/7
		vaca=round(vaca,2)
		vaca=vaca*dias
		vaca=round(vaca,2)
		prima=vaca*prima_vacacional
		prima=round(prima,2)
		sal_vaca=prima
		sal_vaca=round(sal_vaca,2)
		return sal_vaca
