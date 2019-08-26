from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}

# @given("que se cumplen los requisitos")
# def step_impl(context):
# 	pass

# @when("se ejecute una accion")
# def step_impl(context):
# 	pass

# @then("genera el siguiete resultado '{variable}'")
# def step_impl(context, variable):
# 	print(variable)
# 	pass



@given("que mi horario de trabajo puede ser diurno o nocturno")
def step_impl(context):
	pass

@when("ingrese mi hora de entrada: {dia} {hora}:{minuto}:{segundo}")
def step_impl(context, dia, hora, minuto, segundo):
	context.dia = dia
	context.hora = int(hora)
	context.minuto = int(minuto)
	context.segundo = int(segundo)

@when("ingrese mi codigo de trabajador {codigo}")
def step_impl(context, codigo):
	context.codigo = codigo

@then("se buscará mi nombre en la lista de trabajadores")
def step_impl(context):
	mensaje, jornada = marcar_hora_entrada(context.codigo, context.dia, context.hora, context.minuto, context.segundo)
	context.mensaje = mensaje
	context.jornada = jornada

@then("aparecerá el mensaje '{mensaje}'")
def step_impl(context, mensaje):
	assert context.mensaje == mensaje

@then("devolverá el tipo de jornada '{jornada}'")
def step_impl(context, jornada):
	assert context.jornada == jornada