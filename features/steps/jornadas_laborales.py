from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

@given("que mi horario es '{horario}'")
def step_impl(context, horario):
	assert horario in ['diurno','nocturno']

@when("ingreso mi hora de entrada: '{entrada}' el dia: '{dia}' y código: '{codigo}'")
def step_impl(context, entrada, dia, codigo):
	hora, minutos, segundos = entrada.split(':')
	mensaje, jornada = marcar_hora_entrada(codigo, dia, int(hora), int(minutos), int(segundos))
	context.mensaje = mensaje
	context.jornada = jornada

@then("se buscarán mis datos y aparecerá el siguiente mensaje '{mensaje}'")
def step_impl(context, mensaje):
	result = marcar_hora_entrada(context.codigo, context.dia, int(context.horas), int(context.minutos), int(context.segundos))[0] == mensaje
	assert result

@then("aparecerá el mensaje: '{mensaje}'")
def step_impl(context, mensaje):
	context.mensaje = context.mensaje[:len(mensaje)]
	assert context.mensaje == mensaje

@then("la jornada laboral es '{horario}'")
def step_impl(context, horario):
	assert horario == marcar_hora_entrada(context.codigo, context.dia, int(context.horas), int(context.minutos), int(context.segundos))[1]
