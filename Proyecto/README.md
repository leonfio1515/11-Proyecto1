inicio de sesion.

user:	admin
pass:	1234

se recomienda leer manual de uso tras inicio de sesion

http://localhost:8000/Cybe/cajas/manuales_list


------------------------------------------------------------------------------------------------------------------
[Descipcion General]

	Proyecto es una interfaz empresarial la cual brinda distintas soluciones para la realizacion
y optimizacion de distintas tareas.

Entre ellos se podran encontrar 2 grandes modulos.


Solicitudes desde Sucursales:

. Solicitudes por formulario:
	Donde el usuario podra realizar distintas solicitudes hacia la Administracion.

. Confeccion e impresion de documentos:
	Elaboracion e impresion de documentacion, inherente a la tarea diaria de la sucursal.	

. Visualizacion de informacion y documentacion:
	Podra ver y consultar documentacion referente al desarrollo de la tarea.



Gestiones administrativas:

. Registro de informacion:
	Podran ingresar informacion referente al area de desempeño.

. Consultar informacion:
	Podran consultar y emitir reporte de disntita informacion registrada.

. Gestionar solicitudes:
	Podran gestionar y administrar las solicitudes recibidas desde sucursales.


------------------------------------------------------------------------------------------------------------------


------------------------------------------------------------------------------------------------------------------

[Requisitos de entorno]

Python == Version 3.9.13
Django == Version 4.0.5
PostgreSQL == Version 13.8

------------------------------------------------------------------------------------------------------------------

[Implementacion]

. Instalacion de librerias
pip install -r requirements.txt

. Deploy cambios en Heroku
heroku run bash -a intranet-stadium
Luego se podran ingresar comandos Python

------------------------------------------------------------------------------------------------------------------

[Especificaciones del desarrollo]
