
def patron(sueldo,respuesta):
	print("descuentos del patron")
	x=input("revasa las umas (si/no) ")
	uma=260.64
	y=input("Cobramos Infonavit (si/no) ")
	if respuesta=="m" or respuesta=="M":
		sueldo=sueldo/30.4
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		CF=86.88*30.4*.204
		CF=round(CF,2)
		print("Cuota Fija ",CF)
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*30.4*.011
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*30.4*.007
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*30.4*.0105
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*30.4*.0175
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*30.4*.0315
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		G=sueldo*30.4*.01
		G=round(G,2)
		print("Guarderia ",G)
		R=sueldo*30.4*.02
		R=round(R,2)
		print("Retiro ",R)
		if y=="SI" or y=="Si" or y=="sI" or y=="si":
			I=sueldo*30.4*.05
		else:
			I=0
		I=round(I,2)
		print("Infonavit ",I)
		total=CF+Exc+PE+GMP+IyV+G+R+I+CyV
		return total

	if respuesta=="q" or respuesta=="Q":
		sueldo=sueldo/14
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		CF=86.88*14*.204
		CF=round(CF,2)
		print("Cuota Fija ",CF)
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*14*.011
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*14*.007
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*14*.0105
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*14*.0175
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*14*.0315
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		G=sueldo*14*.01
		G=round(G,2)
		print("Guarderia ",G)
		R=sueldo*14*.02
		R=round(R,2)
		print("Retiro ",R)
		if y=="SI" or y=="Si" or y=="sI" or y=="si":
			I=sueldo*14*.05
		else:
			I=0
		I=round(I,2)
		print("Infonavit ",I)
		total=CF+Exc+PE+GMP+IyV+G+R+I+CyV
		return total

	if respuesta=="s" or respuesta=="S":
		sueldo=sueldo/7
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		CF=86.88*7*.204
		CF=round(CF,2)
		print("Cuota Fija ",CF)
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*7*.011
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*7*.007
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*7*.0105
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*7*.0175
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*7*.0315
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		G=sueldo*7*.01
		G=round(G,2)
		print("Guarderia ",G)
		R=sueldo*7*.02
		R=round(R,2)
		print("Retiro ",R)
		if y=="SI" or y=="Si" or y=="sI" or y=="si":
			I=sueldo*7*.05
		else:
			I=0
		I=round(I,2)
		print("Infonavit ",I)
		total=CF+Exc+PE+GMP+IyV+G+R+I+CyV
		return total

	if respuesta=="a" or respuesta=="A":
		sueldo=sueldo/52
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		CF=86.88*52*.204
		CF=round(CF,2)
		print("Cuota Fija ",CF)
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*52*.011
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*52*.007
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*52*.0105
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*52*.0175
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*52*.0315
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		G=sueldo*52*.01
		G=round(G,2)
		print("Guarderia ",G)
		R=sueldo*52*.02
		R=round(R,2)
		print("Retiro ",R)
		if y=="SI" or y=="Si" or y=="sI" or y=="si":
			I=sueldo*52*.05
		else:
			I=0
		I=round(I,2)
		print("Infonavit ",I)
		total=CF+Exc+PE+GMP+IyV+G+R+I+CyV
		return total

def empleado(sueldo,respuesta):
	x=input("revasa las umas (si/no) ")
	uma=260.64
	
	if respuesta=="m" or respuesta=="M":
		sueldo=sueldo/30.4
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*30.4*.004
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*30.4*.0025
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*30.4*.0038
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*30.4*.0063
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*30.4*.0113
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		total=Exc+PE+GMP+IyV+CyV
		return total

	if respuesta=="q" or respuesta=="Q":
		sueldo=sueldo/14
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*14*.004
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*14*.0025
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*14*.0038
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*14*.0063
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*14*.0113
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		total=Exc+PE+GMP+IyV+CyV
		return total	

	if respuesta=="s" or respuesta=="S":
		sueldo=sueldo/7
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*7*.004
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*7*.0025
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*7*.0038
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*7*.0063
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*7*.0113
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		total=Exc+PE+GMP+IyV+CyV
		return total
		
	if respuesta=="a" or respuesta=="A":
		sueldo=sueldo/52
		sueldo=round(sueldo,2)
		excendente=sueldo-uma
		if x=="SI" or x=="Si" or x=="sI" or x=="si":
			Exc=excendente*52*.004
		else:
			Exc=0
		Exc=round(Exc,2)
		print("Excedente ",Exc)
		PE=sueldo*52*.0025
		PE=round(PE,2)
		print("Prestaciones en dinero ",PE)
		GMP=sueldo*52*.0038
		GMP=round(GMP,2)
		print("Gastos médicos ",GMP)
		IyV=sueldo*52*.0063
		IyV=round(IyV,2)
		print("Invalidez y vida ",IyV)
		CyV=sueldo*52*.0113
		CyV=round(CyV,2)
		print("Vejez ",CyV)
		total=Exc+PE+GMP+IyV+CyV
		return total