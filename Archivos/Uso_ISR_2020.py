from aumento import *
from resultados import *
from horas_extra import *
from umas_2020 import *
from vacacioness import *
from Aguinaldo import *
from prima_dominical import *
from anual import *
print("Calculadora de sueldos 2020")
duda=input("¿es anual(anual)? sino pon (diario): ")
if duda in ("diario"):
	salario=float(input("Introduce tu salario: "))
	salario2=salario
elif duda in("anual"):	
	print("Salarios es sueldo/salario+pv+ga+honorario+arrendamiento")
	print("El ciclo solo se dentendra al pulsar 0")
	o=float(input("Introduce tus ingresos: "))
	salario=0
	while(o!=0):
		salario=salario+o
		salario=round(salario,2)
		o=float(input())
	salarioanual=salario
	print("El ciclo solo se dentendra al pulsar 0")
	print("Gastos es lo exento menos lo que gastaste menos deducciones a ciegas")
	e=float(input("Introduce tus gastos + deducciones autorizadas + deduccion ciega, si hay: "))
	gastos=0
	while(e!=0):
		gastos=gastos+e
		gastos=round(gastos,2)
		e=float(input())
	gastosanuales=gastos
	salario=salario-gastos
	salariogastos=salario
	salario=round(salario,2)
	print(salario)
	print("El ciclo solo se dentendra al pulsar 0")
	d=float(input("Ingresa tus deducciones autorizadas "))
	deducciones=0
	while(d!=0):
		deducciones=deducciones+d
		deducciones=round(deducciones,2)
		d=float(input())
	deducciones_autorizadas=deducciones
	salario=salario-deducciones
	salario=round(salario,2)
	print(salario)
	
	salario2=salario

dias=input("es  semanal(s)/quincenal(q)/mensual(m)/anual(anual) ")
dia_extra=input("Hizo un día extra:(si/no) ")
aumento=0
if(dia_extra=="SI" or dia_extra=="Si" or dia_extra=="sI" or dia_extra=="si"):
	resultado=aumentar(salario,aumento,dias)
	salario=resultado
hora_extra=input("Hizo un horas extra:(si/no) ")	
if(hora_extra=="SI" or hora_extra=="Si" or hora_extra=="sI" or hora_extra=="si"):
	resultado2=horas_extra(salario2,aumento,dias)
	salario=salario+resultado2
	salario=round(salario,2)
print("El sueldo neto sin ISR es: ")
print(salario)
salario3=salario

if duda in ("diario"):
	limite_inferior=float(input("Introduce el limite inferior: "))
	cuota_fija=float(input("Introduce la cuota fija: "))
	porcentaje=float(input("Introduce el porcentaje: "))
	subsidio=float(input("Introduce el subsidio: "))
	print("$ ",cuota_fija," Cuota Fija","\n")
	porcentaje=porcentaje/100
	Excedente=float((salario-limite_inferior)*porcentaje)
	Excedente=round(Excedente,2)
	print("$ ",Excedente," Excedente","\n")
	Excedente=round(Excedente,2)
	ISR=Excedente+cuota_fija
	ISR=round(ISR,2)
	print("$ ",ISR," ISR","\n")
	print("$ ",subsidio," subsidio","\n")
	Retiene=ISR-subsidio
	Retiene=round(Retiene,2)
	print("$ ",Retiene," Retiene","\n")
elif duda in("anual"):
	limite_inferior=float(input("Introduce el limite inferior: "))
	cuota_fija=float(input("Introduce la cuota fija: "))
	porcentaje=float(input("Introduce el porcentaje: "))
	print("$ ",cuota_fija," Cuota Fija","\n")
	porcentaje=porcentaje/100
	Excedente=float((salario-limite_inferior)*porcentaje)
	Excedente=round(Excedente,2)
	print("$ ",Excedente," Excedente","\n")
	Excedente=round(Excedente,2)
	ISR=Excedente+cuota_fija
	ISR=round(ISR,2)
	print("$ ",ISR," ISR","\n")
	Retiene=ISR
	Retiene=round(Retiene,2)
	print("$ ",Retiene," Retiene","\n")
	anual(salario, Retiene,salarioanual,gastosanuales,deducciones_autorizadas,salariogastos)


extra=input("¿algun extra?(si/no) ")
sueldo_imss=sueldo_neto(salario,extra,Retiene,dias,duda)
print("calculamos su descuento del IMSS(si/no): ")
respuesta5=input()
if(respuesta5=="SI" or respuesta5=="Si" or respuesta5=="sI" or respuesta5=="si"):
	descuento_patron=patron(salario3,dias)
	descuento_patron=round(descuento_patron,2)
	print("Cuota patronal",descuento_patron)
	descuento_empleado=empleado(salario3,dias)
	descuento_empleado=round(descuento_empleado,2)
	print("Cuota Obrero",descuento_empleado)
	sueldo_imss=sueldo_imss-descuento_empleado
	sueldo_imss=round(sueldo_imss,2)
	if duda=="d" or duda=="D":
		print("EL sueldo neto es de: ")
		print(sueldo_imss)
'''
c=input("Quieres calcular la prima dominical(si/no): ")
if(c=="SI" or c=="Si" or c=="sI" or c=="si"):
	primas=prima(salario2,dias)
	print("Su prima dominical es: ")
	print(primas)

a=input("Quieres calcular el pago de vacaciones(si/no): ")
if(a=="SI" or a=="Si" or a=="sI" or a=="si"):
	antiguedad=int(input("Introduzca su antiguedad: "))
	prima_vacacional=int(input("Introduzca su prima_vacacional: "))
	Vacaciones=vacaciones(salario2,dias,antiguedad,prima_vacacional)
	print("se le pagará en sus vacaciones: ")
	print(Vacaciones)

b=input("Quieres calcular el aguinaldo(si/no): ")
if(b=="SI" or b=="Si" or b=="sI" or b=="si"):
	aguinaldo2=aguinaldo(salario2,dias)
	print("Su aguinaldo es: ")
	print(aguinaldo2)
	'''