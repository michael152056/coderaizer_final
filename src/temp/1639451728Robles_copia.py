sueldo_base = int(input("Sueldo base: "))
pagoxhora = float(input("Pago por hora: "))
horas_extras = int(input("Cantidad de horas: "))
estado_civil = str(input("Estado civil: "))
cantidad_hijos = int(input("Cantidad de hijos: "))

emp = empleado(codigo, sueldo_base,pagoxhora,horas_extras,estado_civil,cantidad_hijos)
emp.calculo_sueldo()
emp.calculo_retenciones()
emp.calculo_neto()
emp.detalle_pago()

