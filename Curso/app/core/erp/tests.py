from app.wsgi import *
from core.erp.models import TipoEmpleado

#Listar
#query=TipoEmpleado.objects.all()
#print(query)

#isercion
#TipoEmpleado(tiṕo_empleado='Galletitas').save()

#edicion
for i in TipoEmpleado.objects.filter(empleado__nombre__startswith='B'):
    print(i.tiṕo_empleado)