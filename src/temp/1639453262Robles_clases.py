class empleado():
    retencion = 0
    neto = 0
    def __init__(self,codigo, sueldo_base,pagoxhora,horas_extras,estado_civil,cantidad_hijos):
        self.cod = codigo
        self.sldo = sueldo_base
        self.pgo_hora = pagoxhora
        self.extras = horas_extras
        self.estado = estado_civil
        self.hijos = cantidad_hijos

    def calculo_sueldo(self):
        self.sldo = self.sldo + (self.pgo_hora * self.extras)
    
    def calculo_retenciones(self):
        if(self.estado == 'casado'):
            empleado.retencion = empleado.retencion + (self.sldo * 0.05)
        for i in range (self.hijos):
            empleado.retencion = empleado.retencion + (self.sldo * 0.05)

    def calculo_neto(self):
        empleado.neto = self.sldo - empleado.retencion

    def detalle_pago(self):
        print('-----------------Detalle de pago----------------')
        print('Cálculo de sueldo: ' + str(self.sldo))
        print('Retención: '+ str(empleado.retencion))
        print('Sueldo neto: ' + str(empleado.neto))
    
codigo = int(input("Código: "))
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

