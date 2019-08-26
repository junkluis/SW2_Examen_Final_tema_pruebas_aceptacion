from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que mi horario de trabajo puede ser diurno o nocturno")
def step_impl(context):
	pass

@when("se ingrese mi hora de entrada '{hora}' hora '{minuto}' minutos '{segundo}' el dia '{dia}' hasta con un retraso de 14 minutos con 59 segundos a mi hora de marcado e ingrese mi codigo de trabajador '{codigo}'")
def step_impl(context,hora,minuto,segundo,dia,codigo):
	mensaje,turno = marcar_hora_entrada(codigo, dia, int(hora), int(minuto), int(segundo))
	context.mensaje=mensaje
	context.turno=turno
	

@then("se buscara mi nombre en la lista")
def step_impl(context):
        context.nombre='Tyrion Lannister'

@then("aparecera el siguiente mensaje '{mensaje}'")
def step_impl(context,mensaje):
        print(context.mensaje)
        assert context.mensaje == mensaje
	
@then("devolvera el tipo de jornada laboral '{turno}'")
def step_impl(context,turno):
        print(context.turno)
        assert context.turno == turno

@when("se ingrese mi hora de entrada '{hora}' hora '{minuto}' minutos '{segundo}' segundos un dia que no este '{dia}' en mi horario e ingrese mi codigo de trabajador '{codigo}'")
def step_impl(context,hora,minuto,segundo,dia,codigo):
	mensaje,turno = marcar_hora_entrada(codigo, dia, int(hora),int(minuto), int(segundo))
	context.mensaje=mensaje
	context.turno=turno

@when("se ingrese mi hora de entrada '{hora}' hora '{minuto}' minutos '{segundo}' el dia '{dia}' con un retraso mayor o igual a 15 minutos, pero menor a 1 hora, e ingrese mi codigo de trabajador '{codigo}'")
def step_impl(context,hora,minuto,segundo,dia,codigo):
	mensaje,turno = marcar_hora_entrada(codigo, dia, int(hora),int(minuto), int(segundo))
	context.mensaje=mensaje
	context.turno=turno

@when("se ingrese mi hora de entrada '{hora}' hora '{minuto}' minutos '{segundo}' el dia '{dia}' antes de lo esperado (20 minutos antes de mi hora de entrada) e ingrese mi codigo de trabajador '{codigo}'")
def step_impl(context,hora,minuto,segundo,dia,codigo):
	mensaje,turno = marcar_hora_entrada(codigo, dia, int(hora),int(minuto), int(segundo))
	context.mensaje=mensaje
	context.turno=turno
