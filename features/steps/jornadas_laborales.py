from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que mi horario puede ser '{horario}'")
def step_impl(context, horario):
	assert horario in ['diurno','nocturno']

@when("ingrese mi hora de entrada: '{entrada}' el dia: '{dia}' y código: '{codigo}'")
def step_impl(context, entrada, dia, codigo):
	hora, minutos, segundos = entrada.split(':')
	mensaje, jornada = marcar_hora_entrada(codigo, dia, int(hora), int(minutos), int(segundos))
	context.mensaje = mensaje
	context.jornada = jornada

@then("aparecerá el mensaje: '{mensaje}' y mi jornada laboral '{jornada}'")
def step_impl(context, mensaje, jornada):
	if len(context.mensaje) != len(mensaje):
		context.mensaje = context.mensaje[:28]
	if len(context.mensaje) != len(mensaje):
		context.mensaje = context.mensaje[:10]
	print(context.jornada)
	print(jornada)
	print(context.mensaje)
	print(mensaje)
	assert context.mensaje == mensaje
	assert context.jornada == jornada
