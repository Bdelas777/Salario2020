from prestamo import *
def sueldo_neto(sal,ext,Ret,dia,duda):
	if(ext=="SI" or ext=="Si" or ext=="sI" or ext=="si"):
		respuesta2=input("¿algun anticipo?(si/no) ")
		if(respuesta2=="SI" or respuesta2=="Si" or respuesta2=="sI" or respuesta2=="si"):
			anticipo=int(input("Introduce tu anticipo: "))
		else:
			anticipo=0
		respuesta3=input("¿algun prestamo?(si/no) ")
		if(respuesta3=="SI" or respuesta3=="Si" or respuesta3=="sI" or respuesta3=="si"):
			prestamo3=prestamos(respuesta3,dia)
			prestamo3=round(prestamo3,2)
		else:
			prestamo3=0
		extras= prestamo3+anticipo+Ret
		sal=sal-extras
		sal=round(sal,2)
		if duda=="d" or duda=="D":
			print("Sueldo sin restar la cuota obrero-patronal")
			print("$ ",sal," Sueldo neto")
		return sal
	else:
		sal=sal-Ret
		sal=round(sal,2)
		if duda=="d" or duda=="D":
			print("Sueldo sin restar la cuota obrero-patronal")
			print("$ ",sal," Sueldo neto")
		return sal