from behave import *
from src.Jornadas import *


#Condiciones antes de empezar cualquier STEP
def before_scenario(context, scenario):
	context = {}


@given("que se cumplen los requisitos")
def step_impl(context):
	pass

@when("se ejecute una accion")
def step_impl(context):
	pass

@then("genera el siguiente resultado '{variable}'")
def step_impl(context, variable):
	print(variable)
	pass

@then("tambien ocurre lo siguiente (si es necesario)")
def step_impl(context):
	pass

@given("que mi horario de trabajo es '{horario}' y es '{dia}'")
def step_impl(context, horario, dia):
	context.horario = horario
	context.dia = dia

@when("ingrese mi hora de entrada como '{entrada}'")
def step_impl(context, entrada):
	fecha = entrada.split(":")
	context.horas = fecha[0]
	context.minutos = fecha[1]
	context.segundos = fecha[2]

@when("ingrese mi codigo de trabajador '{codigo}'")
def step_impl(context, codigo):
	context.codigo = codigo

@then("se buscara mi nombre en la lista de trabajadores y aparecerá el siguiente mensaje '{mensaje}'")
def step_impl(context, mensaje):
	result = marcar_hora_entrada(context.codigo, context.dia, int(context.horas), int(context.minutos), int(context.segundos))[0] == mensaje
	assert result

@then("aparecerá el siguiente mensaje '{mensaje}'")
def step_impl(context, mensaje):
	datos = marcar_hora_entrada(context.codigo, context.dia, int(context.horas), int(context.minutos), int(context.segundos))[0].split(".")
	if len(datos)> 1:
		# cuando llega atrasado retorna con HH:MM:SS.xxxxx. al final
		assert datos[0]+ "." == mensaje
	else:
		result = marcar_hora_entrada(context.codigo, context.dia, int(context.horas), int(context.minutos), int(context.segundos))[0] == mensaje
		assert result


@then("cuya jornada laboral es '{horario}'")
def step_impl(context, horario):
	assert horario == marcar_hora_entrada(context.codigo, context.dia, int(context.horas), int(context.minutos), int(context.segundos))[1]

@then("aparecerá el mensaje '{mensaje}'")
def step_impl(context, mensaje):
	pass

@then("Y cuya jornada laboral es '{horario}'")
def step_impl(context, mensaje):
	assert horario == marcar_hora_entrada(context.codigo, context.dia, int(context.horas), int(context.minutos), int(context.segundos))[1]
