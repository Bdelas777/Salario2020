def prima(sal,respuesta):

	if respuesta=="m" or respuesta=="M":
		sal=sal/30.4
		sal=round(sal,2)
		sal=sal*.25
		sal=round(sal,2)
		return sal
	if respuesta=="q" or respuesta=="Q":
		sal=sal/14
		sal=round(sal,2)
		sal=sal*.25
		sal=round(sal,2)
		return sal
	if respuesta=="s" or respuesta=="S":
		sal=sal/7
		sal=round(sal,2)
		sal=sal*.25
		sal=round(sal,2)
		return sal
